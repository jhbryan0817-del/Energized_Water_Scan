"""Check omitted fastener/connection volumes; allocations, not supplier CAD.
Does not claim actual connector mating, thread strength, wrench usability or torque.
"""
import adsk.core, adsk.fusion, json, os
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def run(_context: str):
 a=adsk.core.Application.get();d=adsk.fusion.Design.cast(a.activeProduct);r=d.rootComponent;m=adsk.fusion.TemporaryBRepManager.get()
 P=lambda x,y,z:adsk.core.Point3D.create(x/10,y/10,z/10)
 V=adsk.core.Vector3D.create
 bs=[(o.name,b) for o in r.allOccurrences if not o.name.startswith(('OPTION','REFERENCE','CLEARANCES','DATUM')) for b in o.bRepBodies if b.isSolid]
 hits=[];failures=[];tests=[];known=[]
 def cylinder(p,q,diam):return m.createCylinderOrCone(P(*p),diam/20,P(*q),diam/20)
 def box(x0,y0,z0,x1,y1,z1):return m.createBox(adsk.core.OrientedBoundingBox3D.create(P((x0+x1)/2,(y0+y1)/2,(z0+z1)/2),V(1,0,0),V(0,1,0),(x1-x0)/10,(y1-y0)/10,(z1-z0)/10))
 def test(label,t,exclude=(),expected=False):
  tests.append({'name':label,'excluded_prefixes':exclude,'expected_blocked':expected})
  for n,b in bs:
   if n.startswith(exclude) or not t.boundingBox.intersects(b.boundingBox):continue
   c=m.copy(t)
   if not m.booleanOperation(c,m.copy(b),adsk.fusion.BooleanTypes.IntersectionBooleanType):failures.append(label+'/'+n);continue
   if c.volume*1000>.001:(known if expected else hits).append({'test':label,'obstacle':n+'/'+b.name,'overlap_mm3':round(c.volume*1000,4)})
 def cyltest(label,p,q,diam,exclude=(),expected=False):test(label,cylinder(p,q,diam),exclude,expected)
 for x,ys in [(26,[-23,23]),(60,[-27,27])]:
  for y in ys:cyltest('motor M3 head '+str((x,y)),(x,y,12),(x,y,15),5.5)
 for x in [-70,140]:
  for y in [-55,55]:cyltest('tray M3 head '+str((x,y)),(x,y,19),(x,y,22),5.5)
 for x in [37.54,57.86]:
  for y in [-37.76,-50.46]:cyltest('ADC M2 head '+str((x,y)),(x,y,25.57),(x,y,27.57),3.8)
 for x in [127,156]:cyltest('servo M2 head '+str(x),(x,-39,45.5),(x,-39,47.5),3.8)
 for label,x,y,z in [('ESP_L',-24,54.5,39.1),('ESP_R',38,54.5,39.1),('FE_L',-24,-45,39.5),('FE_R',24,-45,39.5),('reg_F',63.5,30,31.316),('reg_B',63.5,55.78,31.316),('ESC_F',88,42,39.5),('ESC_B',130,42,39.5)]:cyltest(label+' head',(x,y,z),(x,y,z+3),5.5)
 test('ESP upper header continuous access allocation',box(-20,54.5,35.7,28.3,59,60))
 test('ESP lower header continuous access allocation',box(-20,29,35.7,28.3,33.5,60))
 removed=('ELECTRODE','PRINT_02','PRINT_03','PRINT_04','BATTERY','DRIVELINE','PRINT_11','PRINT_14','PROCURE_Motor','PRINT_18','PRINT_19','PRINT_20','PRINT_21','ESP32','FRONT_END','ADS1115','ESC','D24V10','SERVO')
 for i,x,y in [(1,-100,0),(2,40,0),(3,-30,-55),(4,-30,55)]:cyltest('E%d vertical D12 socket'%i,(x,y,14.3),(x,y,85),12,removed,i==1)
 # This candidate also clips the bow: keep it as an explicit unresolved failure,
 # not a passed tool path or a reason to thin the watertight shell blindly.
 test('E1 low-profile wrench allocation before tray',box(-108,-8,19,-60,8,27),removed,True)
 cyltest('E1 short socket allocation',(-100,0,14.3),(-100,0,23),12,removed)
 result={'revision':'Rev-B.3','timeline_items':d.timeline.count,'tests':tests,'unexpected_intersections':hits,'known_blocked_access':known,'assembly_release_passed':not hits and not known and not failures,'boolean_failures':failures,'limits':'Head envelopes D5.5x3 M3 and D3.8x2 M2; washers and actual fastener tolerances unmodeled. Continuous header access boxes are allocations, not verified connector CAD. E1 straight-down access and the candidate low-profile wrench are blocked; actual installation tooling remains a release blocker.'}
 with open(os.path.join(BASE,'verification','RevB3_Fastener_Access_Audit.json'),'w') as f:json.dump(result,f,indent=2)
 print(json.dumps(result))
 assert not hits and not failures, 'Additional assembly audit failed'
