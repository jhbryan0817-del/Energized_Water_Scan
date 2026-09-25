import adsk.core,adsk.fusion,json,os
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def run(context):
 a=adsk.core.Application.get();d=adsk.fusion.Design.cast(a.activeProduct);r=d.rootComponent;mgr=adsk.fusion.TemporaryBRepManager.get()
 bodies=[(o.fullPathName,b) for o in r.allOccurrences if not o.component.name.startswith(('DATUM','REFERENCE','OPTION','CLEARANCES')) for b in o.bRepBodies if b.isSolid]
 failures=[];hits=[]
 def test(label,body,exclude):
  for n,b in bodies:
   if n.startswith(tuple(exclude)) or not body.boundingBox.intersects(b.boundingBox):continue
   t=mgr.copy(body)
   if not mgr.booleanOperation(t,mgr.copy(b),adsk.fusion.BooleanTypes.IntersectionBooleanType):failures.append(label+'/'+n);continue
   if t.volume*1000>.001:hits.append(dict(check=label,obstacle=n+'/'+b.name,volume_mm3=round(t.volume*1000,5)))
 def cyl(x,y,z1,z2,diam):return mgr.createCylinderOrCone(adsk.core.Point3D.create(x/10,y/10,z1/10),diam/20,adsk.core.Point3D.create(x/10,y/10,z2/10),diam/20)
 for x in [-70,140]:
  for y in [-55,55]:test('tray screw D8 tool '+str((x,y)),cyl(x,y,20,110,8),['PRINT_02','PRINT_03','PRINT_04','BATTERY_'])
 for x,y in [(-86,-71),(42.5,-71),(171,-71),(171,0),(171,71),(42.5,71),(-86,71),(-86,0)]:test('hatch screw D12 tool '+str((x,y)),cyl(x,y,73.1,110,12),['PRINT_02'])
 test('battery pull-loop D25 hand allocation',cyl(-52.5,0,36,110,25),['PRINT_02'])
 moving_prefix=('PRINT_03','ESP32_','FRONT_END_','ADS1115_','D24V10F5_','ESC_','PROCURE_ESC','SERVO_','PRINT_18','PRINT_19','PRINT_20','PRINT_21')
 # Disconnect and remove horn/linkage, battery and its loose strap tray before lifting.
 excludes=list(moving_prefix)+['PRINT_02','BATTERY_','PRINT_04','PROCURE_Servo_horn']
 for dz in range(0,101,5):
  for n,b in bodies:
   if n.startswith(moving_prefix):
    t=mgr.copy(b);m=adsk.core.Matrix3D.create();m.translation=adsk.core.Vector3D.create(0,0,dz/10);assert mgr.transform(t,m)
    test('tray lift '+str(dz)+' mm / '+n+'/'+b.name,t,excludes)
 metrics={}
 for prefix in ['PRINT_01','PRINT_02','PRINT_03','PRINT_04','BATTERY_','ESP32_','FRONT_END_','ADS1115_','SENSOR_']:
  o=next(o for o in r.allOccurrences if o.name.startswith(prefix));bb=o.boundingBox
  metrics[prefix]=dict(min_mm=[round(v*10,3) for v in bb.minPoint.asArray()],max_mm=[round(v*10,3) for v in bb.maxPoint.asArray()])
 result=dict(revision='Rev-B.2',timeline_items=d.timeline.count,method='Exact temporary BRep intersections for tool/grip allocations; tray lift sampled every 5 mm from 0 to 100 mm. Cables, fasteners and flexible retainers not fully modeled; this is not a physical assembly trial.',prerequisites=['Remove hatch.','Unplug and remove battery and battery strap tray.','Disconnect and remove servo horn/linkage and unplug tray wiring before lifting electronics tray.','USB insertion requires battery and battery tray removal.'],intersections=hits,boolean_failures=failures,metrics=metrics)
 with open(os.path.join(BASE,'verification','RevB2_Service_Audit.json'),'w') as f:json.dump(result,f,indent=2)
 print(json.dumps(result))
 assert not hits and not failures, 'Service audit failed; inspect the saved report'
