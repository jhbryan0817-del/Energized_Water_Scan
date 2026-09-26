"""Focused Rev-B.4 route, support and fastener-access checks in Fusion."""
import adsk.core, adsk.fusion, json, os
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def run(_context: str):
 a=adsk.core.Application.get();d=adsk.fusion.Design.cast(a.activeProduct);r=d.rootComponent;m=adsk.fusion.TemporaryBRepManager.get()
 P=lambda x,y,z:adsk.core.Point3D.create(x/10,y/10,z/10)
 physical=[o for o in r.allOccurrences if o.bRepBodies.count and not o.name.startswith(('DATUM','REFERENCE','OPTION','CLEARANCES'))]
 bodies=[(o.fullPathName,b) for o in physical for b in o.bRepBodies if b.isSolid]
 failures=[];hits=[];tests=[]
 def cyl(p,q,diam):return m.createCylinderOrCone(P(*p),diam/20,P(*q),diam/20)
 def test(name,t,exclude=()):
  tests.append(name)
  for n,b in bodies:
   if n.startswith(exclude) or not t.boundingBox.intersects(b.boundingBox):continue
   c=m.copy(t)
   if not m.booleanOperation(c,m.copy(b),adsk.fusion.BooleanTypes.IntersectionBooleanType):failures.append(name+'/'+n)
   elif c.volume*1000>.001:hits.append({'test':name,'obstacle':n+'/'+b.name,'overlap_mm3':c.volume*1000})
 # D4 corridors represent conductor bundles, NOT connector passage. End the
 # riser above the tray; mating connectors and bend radii require actual parts.
 routes={
  'E1':[(-84,0,12.2),(-76,0,12.2),(-76,-18,12.2),(-25,-18,12.2),(-25,-23,12.2),(-25,-23,40)],
  'E2':[(40,-16,12.2),(40,-32,12.2),(0,-32,12.2),(-25,-23,12.2),(-25,-23,40)],
  'E3':[(-30,-39,12.2),(-30,-30,12.2),(-25,-23,12.2),(-25,-23,40)],
  'E4':[(-30,39,12.2),(-25,30,12.2),(-25,-23,12.2),(-25,-23,40)]}
 for label,points in routes.items():
  for j,(p,q) in enumerate(zip(points,points[1:])):test(label+'_D4_route_'+str(j),cyl(p,q,4),('PRINT_02',))
 # Top-access tool corridors after battery/tray removal for motor support work.
 for x,ys in [(26,[-23,23]),(60,[-27,27])]:
  for y in ys:test('M3_motor_support_D6_tool_'+str((x,y)),cyl((x,y,15),(x,y,100),6),('PRINT_02','PRINT_03','PRINT_18','PRINT_19','PRINT_20','PRINT_21','BATTERY','PRINT_04','ESP32','FRONT_END','D24V10F5','ADS1115','ESC','PROCURE_ESC','SERVO'))
 for label,x,y,z in [('ESP_left',-24,54.5,39.1),('ESP_right',38,54.5,39.1),('FE_left',-24,-45,39.5),('FE_right',24,-45,39.5),('reg_front',63.5,30,31.316),('reg_back',63.5,55.78,31.316),('ESC_front',88,42,39.5),('ESC_back',130,42,39.5)]:
  test('capture_M3_D6_tool_'+label,cyl((x,y,z+.1),(x,y,100),6),('PRINT_02',))
 for y in [-9,9]:
  for z in [50,58]:test('transom_M3_D6_tool_'+str((y,z)),cyl((204.1,y,z),(330,y,z),6))
 for x in [-108,-98]:test('rail_M3_D6_tool_before_pod_'+str(x),cyl((x,0,72.1),(x,0,110),6),('PRINT_07','PRINT_08','SENSOR_','PROCURE_Magnetometer'))
 # E2 nut socket corridor is deliberately checked ONLY with drive/mounts/tray removed.
 test('E2_D12_socket_before_motor',cyl((40,0,14.3),(40,0,85),12),('PRINT_02','PRINT_03','PRINT_04','BATTERY','DRIVELINE','PRINT_11','PRINT_14','PROCURE_Motor_cradle','ELECTRODE_E2'))
 # Full-solid component support graph. Bearings/clearance fits are documented
 # separately; proximity alone is not positive fastening.
 support=[]
 for o in physical:
  near=[]
  for p in physical:
   if o==p:continue
   dist=a.measureManager.measureMinimumDistance(o,p).value*10
   if dist<1.01:near.append({'component':p.fullPathName,'distance_mm':round(dist,4)})
  support.append({'component':o.fullPathName,'nearby':near})
 printed=[{'name':o.name,'solids':o.bRepBodies.count,'lumps':[b.lumps.count for b in o.bRepBodies]} for o in physical if o.name.startswith('PRINT_')]
 lug=next(b for o in physical if o.name.startswith('ELECTRODE_E2') for b in o.bRepBodies if 'ring_lug' in b.name)
 near_lug={o.name:round(a.measureManager.measureMinimumDistance(lug,o).value*10,4) for o in physical if o.name.startswith(('PRINT_14','PRINT_11','DRIVELINE','PRINT_03'))}
 result={'revision':'Rev-B.4','timeline_items':d.timeline.count,'E2_lug_to_obstacle_minimum_mm':near_lug,'route_diameter_mm':4,'routes_mm':routes,'tested_corridors':tests,'intersections':hits,'boolean_failures':failures,'support_proximity':support,'printed_connected_solids':printed,'limits':'Wire centerline corridors only: route bends, connectors, insulation and strain relief require physical dry assembly. Proximity is not proof of fastening. See the documented retention schedule and service sequence.'}
 with open(os.path.join(BASE,'verification','RevB4_Wiring_Support_Audit.json'),'w') as f:json.dump(result,f,indent=2)
 print(json.dumps({'intersections':hits,'boolean_failures':failures,'prints':printed,'isolated_components':[s for s in support if not s['nearby']]}))
 assert not hits and not failures, 'Wire/tool access audit failed; inspect the saved report'
 assert all(s['nearby'] for s in support), 'An isolated component needs a documented support path'
 assert all(p['solids']==1 and p['lumps']==[1] for p in printed), 'A print contains disconnected solid geometry'
