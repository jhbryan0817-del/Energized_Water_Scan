"""Read-only supplier-interface regression; use temporary bodies, never alter CAD.
Nominal fits and explicit allocations are separate from physical acceptance.
"""
import adsk.core,adsk.fusion,json,os,math
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run(_context: str):
 a=adsk.core.Application.get();d=adsk.fusion.Design.cast(a.activeProduct);r=d.rootComponent;m=adsk.fusion.TemporaryBRepManager.get()
 P=lambda x,y,z:adsk.core.Point3D.create(x/10,y/10,z/10);V=adsk.core.Vector3D.create
 def box(x0,y0,z0,x1,y1,z1):return m.createBox(adsk.core.OrientedBoundingBox3D.create(P((x0+x1)/2,(y0+y1)/2,(z0+z1)/2),V(1,0,0),V(0,1,0),(x1-x0)/10,(y1-y0)/10,(z1-z0)/10))
 def cylinder(x,y,z0,z1,diam):return m.createCylinderOrCone(P(x,y,z0),diam/20,P(x,y,z1),diam/20)
 printed=[(o.name,b) for o in r.allOccurrences if o.name.startswith('PRINT_') for b in o.bRepBodies]
 tests=[]
 def test(name,t):
  hits=[]
  for n,b in printed:
   if not t.boundingBox.intersects(b.boundingBox):continue
   c=m.copy(t);assert m.booleanOperation(c,m.copy(b),adsk.fusion.BooleanTypes.IntersectionBooleanType)
   if c.volume*1000>.001:hits.append({'component':n,'overlap_mm3':c.volume*1000})
  tests.append({'name':name,'intersections':hits});return hits
 test('Pololu PCB edges expanded 0.3 mm in every XY direction; drawing tolerance',box(56.7,33.7,24,70,52.08,25.016))
 test('Regulator connection allocation, not a supplied connector model; X56.5..70.2 Y33.5..37 Z25.02..38',box(56.5,33.5,25.02,70.2,37,38))
 for x in [58.27,60.81,63.35,65.89,68.43]:test('Regulator pin axis upward D1mm '+str(x),cylinder(x,35.27,25.02,45,1))
 nuts=[]
 for o in r.allOccurrences:
  if o.name.startswith('ELECTRODE'):
   b=next(b for b in o.bRepBodies if b.name.startswith('Nut_'));bb=b.boundingBox
   nuts.append({'name':o.name,'diameter_mm':(bb.maxPoint.x-bb.minPoint.x)*10,'height_mm':(bb.maxPoint.z-bb.minPoint.z)*10})
   assert abs((bb.maxPoint.x-bb.minPoint.x)*10-8.1)<1e-5
 adc=next(o for o in r.allOccurrences if o.name.startswith('ADS1115'))
 holes=[]
 for f in adc.bRepBodies.item(0).faces:
  g=f.geometry
  if isinstance(g,adsk.core.Cylinder) and abs(g.radius-.125)<1e-6:holes.append([round(g.origin.x*10,3),round(g.origin.y*10,3)])
 expected=[[37.54,-50.46],[37.54,-37.76],[57.86,-50.46],[57.86,-37.76]]
 assert sorted(holes)==sorted(expected)
 axis=V(math.cos(math.radians(15)),0,-math.sin(math.radians(15)));origin=P(55,0,30)
 driveline=[]
 for o in r.allOccurrences:
  if o.name.startswith('DRIVELINE'):
   for b in o.bRepBodies:
    ss=[origin.vectorTo(v.geometry).dotProduct(axis)*10 for v in b.vertices]
    driveline.append({'body':b.name,'axial_min_mm':min(ss),'axial_max_mm':max(ss),'axial_length_mm':max(ss)-min(ss)})
 result={'revision':'Rev-B.4','timeline_items':d.timeline.count,'tests':tests,'M4_nut_envelopes':nuts,'adc_hole_centres_mm':holes,'driveline_along_axis_from_motor_face':driveline,'regression_passed':all(not t['intersections'] for t in tests),'assembly_release_passed':False,'limits':['No manufacturer tolerance inferred from CAD decimal precision.','Regulator connection space is an allocation; actual connector body and wire bending remain a fit trial.','Driveline dimensions measured along shaft, not assembly bounding boxes. Bore fits, threads, thrust washers and insertion depths need actual parts.','E1 access is builder-accepted; seal compression and final leak test remain unverified.','SG90 horn and mounting are not verified; proposed Hitec substitution has not been implemented.']}
 with open(os.path.join(BASE,'verification','RevB4_Supplier_Interface_Audit.json'),'w') as f:json.dump(result,f,indent=2)
 print(json.dumps(result));assert result['regression_passed']
