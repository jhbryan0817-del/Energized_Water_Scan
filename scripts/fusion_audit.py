import adsk.core, adsk.fusion, json, math, os
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run(_context: str):
 app=adsk.core.Application.get(); d=adsk.fusion.Design.cast(app.activeProduct)
 assert app.activeDocument.name.startswith('Energized_Water_Scanner'), 'Open the scanner design first'
 root=d.rootComponent; mgr=adsk.fusion.TemporaryBRepManager.get()
 def pt(p):return [round(x*10,5) for x in p.asArray()]
 def physical(o):return not o.component.name.startswith(('DATUM','REFERENCE','OPTION','CLEARANCES'))
 bodies=[(o.fullPathName,b) for o in root.allOccurrences if physical(o) for b in o.bRepBodies if b.isSolid]
 failures=[]
 def overlap(a,b,label):
  if not a.boundingBox.intersects(b.boundingBox):return 0
  t=mgr.copy(a)
  if not mgr.booleanOperation(t,mgr.copy(b),adsk.fusion.BooleanTypes.IntersectionBooleanType):
   failures.append(label);return None
  return t.volume*1000
 collisions=[]
 for i,(an,a) in enumerate(bodies):
  for bn,b in bodies[i+1:]:
   if an==bn:continue
   v=overlap(a,b,an+' / '+bn)
   if v is not None and v>0.001:collisions.append(dict(a=an+'/'+a.name,b=bn+'/'+b.name,volume_mm3=v))
 issues=[]; other=[]
 for i in range(d.timeline.count):
  t=d.timeline.item(i)
  if t.healthState in [adsk.fusion.FeatureHealthStates.WarningFeatureHealthState,adsk.fusion.FeatureHealthStates.ErrorFeatureHealthState]:issues.append(dict(index=i,name=t.name,message=t.errorOrWarningMessage))
  elif t.healthState!=adsk.fusion.FeatureHealthStates.HealthyFeatureHealthState:other.append(dict(index=i,name=t.name,state=int(t.healthState)))
 clearance=[]
 for o in root.allOccurrences:
  if o.name.startswith('CLEARANCES'):
   for a in o.bRepBodies:
    for bn,b in bodies:
     v=overlap(a,b,a.name+' / '+bn)
     if v is not None and v>0.001:clearance.append(dict(envelope=a.name,component=bn,body=b.name,volume_mm3=round(v,4)))
 def find(prefix,name=None):
  return next(b for o in root.allOccurrences if o.name.startswith(prefix) for b in o.bRepBodies if name is None or b.name==name)
 def rotated(b,deg,x,y):
  t=mgr.copy(b);m=adsk.core.Matrix3D.create();m.setToRotation(math.radians(deg),adsk.core.Vector3D.create(0,0,1),adsk.core.Point3D.create(x/10,y/10,0));assert mgr.transform(t,m);return t
 def endpoints(phi,theta):
  p=math.radians(phi);t=math.radians(theta)
  return (147-17.9*math.sin(t),-38.9+17.9*math.cos(t)),(278+21*math.sin(p),-21*math.cos(p))
 def residual(phi,theta):
  a,b=endpoints(phi,theta);return math.hypot(a[0]-b[0],a[1]-b[1])-131
 motion=[]; solutions=[]
 static=[(n,b) for n,b in bodies if not n.startswith(('PRINT_16','PRINT_17','PROCURE_Servo_horn','PROCURE_Tiller_cross','PROCURE_Rudder_stock','SEAL_Steering'))]
 for phi in range(-35,36):
  lo,hi=-80.,80.
  assert residual(phi,lo)*residual(phi,hi)<0
  for j in range(45):
   mid=(lo+hi)/2
   if residual(phi,lo)*residual(phi,mid)<=0:hi=mid
   else:lo=mid
  theta=(lo+hi)/2;a,b=endpoints(phi,theta)
  solutions.append(dict(rudder_deg=phi,servo_deg=theta,rod_endpoints_mm=[[*a,60],[*b,60]]))
  moving=[('blade',rotated(find('PRINT_16'),phi,278,0)),('tiller',rotated(find('PRINT_17'),phi,278,0)),('cross_pin',rotated(find('PROCURE_Tiller_cross'),phi,278,0)),('horn',rotated(find('PROCURE_Servo_horn','Custom_horn_spline_fit_TBD'),theta,147,-38.9)),('horn_pin',rotated(find('PROCURE_Servo_horn','Horn_link_pin'),theta,147,-38.9)),('drop_pin',rotated(find('PROCURE_Servo_horn','Tiller_drop_link_pin'),phi,278,0))]
  rod=mgr.createCylinderOrCone(adsk.core.Point3D.create(a[0]/10,a[1]/10,6),0.1,adsk.core.Point3D.create(b[0]/10,b[1]/10,6),0.1);moving.append(('rod',rod))
  for mn,mb in moving:
   for sn,sb in static:
    v=overlap(mb,sb,str(phi)+' '+mn+' '+sn)
    if v is not None and v>0.001:motion.append(dict(rudder_deg=phi,moving=mn,obstacle=sn+'/'+sb.name,volume_mm3=round(v,4)))
 inventory=[dict(component=n,body=b.name,volume_cm3=b.volume,min_mm=pt(b.boundingBox.minPoint),max_mm=pt(b.boundingBox.maxPoint)) for n,b in bodies]
 result=dict(document=app.activeDocument.name,revision='Rev-B.1',date='2026-09-25',body_count=len(bodies),interferences_between_components=collisions,boolean_failures=failures,timeline_items=d.timeline.count,parameters=d.userParameters.count,feature_errors_and_warnings=issues,other_timeline_states=other,inventory=inventory,clearance_intersections=clearance,steering=dict(method='Rigid idealized linkage, rudder -35 to +35 degrees in 1-degree increments; flexible boot and unmodeled hardware excluded. No claim of continuous sweep or physical validation.',collisions=motion,solutions=solutions))
 with open(os.path.join(BASE,'verification','RevB1_Assembly_Audit.json'),'w') as f:json.dump(result,f,indent=2)
 print(json.dumps({k:result[k] for k in ['body_count','interferences_between_components','boolean_failures','timeline_items','parameters','feature_errors_and_warnings','other_timeline_states']}))
 print('motion collisions',json.dumps(motion));print('servo endpoints',solutions[0],solutions[-1]);print('clearances',json.dumps(clearance))
