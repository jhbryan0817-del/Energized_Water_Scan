"""Add 0.8 mm below the E2 barrel for a 12 x 7 mm finished side exit."""
import adsk.core,adsk.fusion
def run(_context: str):
 d=adsk.fusion.Design.cast(adsk.core.Application.get().activeProduct);m=adsk.fusion.TemporaryBRepManager.get()
 c=next(o.component for o in d.rootComponent.allOccurrences if o.name.startswith('PRINT_14'));b=c.bRepBodies.item(0)
 t=m.createBox(adsk.core.OrientedBoundingBox3D.create(adsk.core.Point3D.create(4,-1.3,1.25),adsk.core.Vector3D.create(1,0,0),adsk.core.Vector3D.create(0,1,0),1.2,2.2,.7))
 f=c.features.baseFeatures.add();f.name='RevB2_E2_exit_margin_tool';f.startEdit();c.bRepBodies.add(t,f);f.finishEdit()
 oc=adsk.core.ObjectCollection.create();oc.add(f.bodies.item(0));i=c.features.combineFeatures.createInput(b,oc);i.operation=adsk.fusion.FeatureOperations.CutFeatureOperation;c.features.combineFeatures.add(i).name='RevB2_E2_final_exit_12x7mm'
 print('Final E2 exit enlarged to Z9...16 mm; timeline',d.timeline.count)
