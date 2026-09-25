"""Resolve exact-tangent rail bosses and a tie-slot/pedestal edge junction."""
import adsk.core,adsk.fusion
def run(_context: str):
 d=adsk.fusion.Design.cast(adsk.core.Application.get().activeProduct);r=d.rootComponent;m=adsk.fusion.TemporaryBRepManager.get()
 P=lambda x,y,z:adsk.core.Point3D.create(x/10,y/10,z/10)
 V=adsk.core.Vector3D.create
 def comp(pre):return next(o.component for o in r.allOccurrences if o.name.startswith(pre))
 def box(x0,y0,z0,x1,y1,z1):return m.createBox(adsk.core.OrientedBoundingBox3D.create(P((x0+x1)/2,(y0+y1)/2,(z0+z1)/2),V(1,0,0),V(0,1,0),(x1-x0)/10,(y1-y0)/10,(z1-z0)/10))
 def modify(c,t,name,join):
  b=c.bRepBodies.item(0);f=c.features.baseFeatures.add();f.name=name+'_tool';f.startEdit();c.bRepBodies.add(t,f);f.finishEdit()
  oc=adsk.core.ObjectCollection.create();oc.add(f.bodies.item(0));i=c.features.combineFeatures.createInput(b,oc);i.operation=adsk.fusion.FeatureOperations.JoinFeatureOperation if join else adsk.fusion.FeatureOperations.CutFeatureOperation;c.features.combineFeatures.add(i).name=name
 # A short web between the two rail bosses replaces their zero-width tangent.
 modify(comp('PRINT_01'),box(-106,-2,60,-100,2,65),'RevB2_rail_boss_connecting_web',True)
 for x in [76,84]:
  modify(comp('PRINT_03'),box(x-1.5,42,16,x+1.5,46,19),'RevB2_close_old_power_tie_slot',True)
  modify(comp('PRINT_03'),box(x-1.5,48,15,x+1.5,52,20),'RevB2_power_tie_slot_at_Y50',False)
 print('Resolved two tangent mesh edges; timeline',d.timeline.count)
