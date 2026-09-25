"""Open driver/head access through the upper bracket gussets for the M3 pair."""
import adsk.core,adsk.fusion
def run(_context: str):
 d=adsk.fusion.Design.cast(adsk.core.Application.get().activeProduct);m=adsk.fusion.TemporaryBRepManager.get()
 c=next(o.component for o in d.rootComponent.allOccurrences if o.name.startswith('PRINT_09'))
 for y in [-.9,.9]:
  b=c.bRepBodies.item(0);t=m.createCylinderOrCone(adsk.core.Point3D.create(20.4,y,5.8),.32,adsk.core.Point3D.create(33,y,5.8),.32)
  f=c.features.baseFeatures.add();f.name='RevB2_transom_driver_access_tool';f.startEdit();c.bRepBodies.add(t,f);f.finishEdit()
  oc=adsk.core.ObjectCollection.create();oc.add(f.bodies.item(0));i=c.features.combineFeatures.createInput(b,oc);i.operation=adsk.fusion.FeatureOperations.CutFeatureOperation;c.features.combineFeatures.add(i).name='RevB2_transom_upper_M3_D6_4_driver_access'
 assert c.bRepBodies.count==1 and c.bRepBodies.item(0).lumps.count==1
 print('Upper transom screws now have D6.4 driver/head bores; timeline',d.timeline.count)
