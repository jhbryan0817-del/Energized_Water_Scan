"""Run once through Fusion MCP on the 1216-item Rev-B.2 scanner.
Fixed assembly coordinates in mm. See RevB3_Assembly_Readiness.md for limits.
"""
import adsk.core, adsk.fusion, json

def run(_context: str):
 a=adsk.core.Application.get();d=adsk.fusion.Design.cast(a.activeProduct);r=d.rootComponent
 assert a.activeDocument.name=='Energized_Water_Scanner'
 assert d.timeline.count==1216, 'Requires unchanged Rev-B.2 baseline'
 m=adsk.fusion.TemporaryBRepManager.get();P=lambda x,y,z:adsk.core.Point3D.create(x/10,y/10,z/10)
 V=adsk.core.Vector3D.create
 def box(x0,y0,z0,x1,y1,z1):
  return m.createBox(adsk.core.OrientedBoundingBox3D.create(P((x0+x1)/2,(y0+y1)/2,(z0+z1)/2),V(1,0,0),V(0,1,0),(x1-x0)/10,(y1-y0)/10,(z1-z0)/10))
 def cyl(x,y,z0,z1,diam):return m.createCylinderOrCone(P(x,y,z0),diam/20,P(x,y,z1),diam/20)
 def comp(pre):return next(o.component for o in r.allOccurrences if o.name.startswith(pre))
 def modify(c,t,name,join=False):
  target=c.bRepBodies.item(0);f=c.features.baseFeatures.add();f.name=name+'_tool';assert f.startEdit()
  c.bRepBodies.add(t,f);assert f.finishEdit()
  oc=adsk.core.ObjectCollection.create();oc.add(f.bodies.item(0));i=c.features.combineFeatures.createInput(target,oc)
  i.operation=adsk.fusion.FeatureOperations.JoinFeatureOperation if join else adsk.fusion.FeatureOperations.CutFeatureOperation
  c.features.combineFeatures.add(i).name=name
  assert c.bRepBodies.count==1 and c.bRepBodies.item(0).lumps.count==1
 # Clearance for real tray screw heads (D5.5 x 3); open edge scallops also permit a D8 driver.
 for y in [-55,55]:modify(comp('PRINT_04'),cyl(-70,y,18.9,26.1,8),'RevB3_battery_tray_M3_head_relief_'+str(y))
 # Open the upper ESP32 header row. Reinforce the remaining crossbar on its inboard side.
 bridge=comp('PRINT_18')
 modify(bridge,box(-28,48.5,36.1,42,50.6,39.1),'RevB3_ESP_bridge_inboard_reinforcement',True)
 modify(bridge,box(-21,54,35.9,29,59,39.3),'RevB3_ESP_header_connection_window')
 # Increase tip margin for M3x8 from 0.2 to 2 mm, retaining a nominal 2 mm hull floor.
 for x,ys in [(26,[-23,23]),(60,[-27,27])]:
  for y in ys:modify(comp('PRINT_01'),cyl(x,y,2,9.1,2.5),'RevB3_motor_M3_pilot_depth_'+str((x,y)))
 assert d.computeAll()
 print(json.dumps({'revision':'Rev-B.3','timeline_items':d.timeline.count,'changed_prints':['PRINT_01','PRINT_04','PRINT_18']}))
