"""Finish the head reliefs as open corners; remove 0.5 mm peripheral slivers.
Run after revb3_assembly_fixes.py, before audits/exports.
"""
import adsk.core,adsk.fusion
def run(_context: str):
 a=adsk.core.Application.get();d=adsk.fusion.Design.cast(a.activeProduct)
 assert a.activeDocument.name=='Energized_Water_Scanner' and d.timeline.count==1232
 c=next(o.component for o in d.rootComponent.allOccurrences if o.name.startswith('PRINT_04'))
 m=adsk.fusion.TemporaryBRepManager.get();P=lambda x,y,z:adsk.core.Point3D.create(x/10,y/10,z/10);V=adsk.core.Vector3D.create
 for y in [-55.5,55.5]:
  t=m.createBox(adsk.core.OrientedBoundingBox3D.create(P(-70.5,y,22.5),V(1,0,0),V(0,1,0),.9,.9,.8))
  target=c.bRepBodies.item(0);f=c.features.baseFeatures.add();f.name='RevB3_open_head_relief_tool';assert f.startEdit();c.bRepBodies.add(t,f);assert f.finishEdit()
  oc=adsk.core.ObjectCollection.create();oc.add(f.bodies.item(0));i=c.features.combineFeatures.createInput(target,oc);i.operation=adsk.fusion.FeatureOperations.CutFeatureOperation
  c.features.combineFeatures.add(i).name='RevB3_remove_thin_corner_lands'
 assert d.computeAll() and c.bRepBodies.count==1 and c.bRepBodies.item(0).lumps.count==1
 print('Open 9x9 corner reliefs; timeline',d.timeline.count)
