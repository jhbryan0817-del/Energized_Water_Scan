"""One-time Rev-B.3 -> Rev-B.4 supplier-interface correction through Fusion MCP.
All explicit coordinates are assembly mm; do not rerun after migration.
"""
import adsk.core, adsk.fusion, json, os
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run(_context: str):
 a=adsk.core.Application.get();d=adsk.fusion.Design.cast(a.activeProduct);r=d.rootComponent
 assert a.activeDocument.name=='Energized_Water_Scanner' and d.timeline.count==1236
 backup=os.path.join(os.path.dirname(BASE),'RevB3_before_supplier_audit.f3d')
 assert d.exportManager.execute(d.exportManager.createFusionArchiveExportOptions(backup))
 m=adsk.fusion.TemporaryBRepManager.get();P=lambda x,y,z:adsk.core.Point3D.create(x/10,y/10,z/10);V=adsk.core.Vector3D.create
 def box(x0,y0,z0,x1,y1,z1):return m.createBox(adsk.core.OrientedBoundingBox3D.create(P((x0+x1)/2,(y0+y1)/2,(z0+z1)/2),V(1,0,0),V(0,1,0),(x1-x0)/10,(y1-y0)/10,(z1-z0)/10))
 def cyl(x,y,z0,z1,diam):return m.createCylinderOrCone(P(x,y,z0),diam/20,P(x,y,z1),diam/20)
 def comp(pre):return next(o.component for o in r.allOccurrences if o.name.startswith(pre))
 def modify(c,target,t,name,join=False):
  f=c.features.baseFeatures.add();f.name=name+'_tool';assert f.startEdit();c.bRepBodies.add(t,f);assert f.finishEdit()
  oc=adsk.core.ObjectCollection.create();oc.add(f.bodies.item(0));i=c.features.combineFeatures.createInput(target,oc)
  i.operation=adsk.fusion.FeatureOperations.JoinFeatureOperation if join else adsk.fusion.FeatureOperations.CutFeatureOperation
  c.features.combineFeatures.add(i).name=name
 # Preserve screw seats and the rear capture span; bypass the five-pin connection row.
 c=comp('PRINT_20');target=c.bRepBodies.item(0)
 bypass=box(63.4,29,28.316,74,32.5,31.316)
 for t in [box(71,29,28.316,74,41.5,31.316),box(63.4,38,28.316,74,41.5,31.316)]:assert m.booleanOperation(bypass,t,adsk.fusion.BooleanTypes.UnionBooleanType)
 modify(c,target,bypass,'RevB4_regulator_pin_row_bypass',True)
 modify(c,c.bRepBodies.item(0),box(56.5,33.3,28.216,70.5,37.5,31.416),'RevB4_regulator_pin_row_window')
 modify(c,c.bRepBodies.item(0),cyl(63.5,30,28.2,31.5,3.4),'RevB4_preserve_front_M3_clearance')
 assert c.bRepBodies.count==1 and c.bRepBodies.item(0).lumps.count==1
 # A D7 cylinder missed the corners of a 7-AF hex nut. D8.1 bounds all rotations.
 for prefix,x,y in [('ELECTRODE_E1',-100,0),('ELECTRODE_E2',40,0),('ELECTRODE_E3',-30,-55),('ELECTRODE_E4',-30,55)]:
  c=comp(prefix);target=next(b for b in c.bRepBodies if b.name=='Nut_envelope')
  ring=cyl(x,y,11,14.2,8.1);assert m.booleanOperation(ring,cyl(x,y,10.9,14.3,4),adsk.fusion.BooleanTypes.DifferenceBooleanType)
  modify(c,target,ring,'RevB4_M4_DIN934_nut_corner_envelope',True)
  next(b for b in c.bRepBodies if b.name=='Nut_envelope').name='Nut_DIN934_7AF_D8p1_rotation_envelope'
 c=comp('D24V10F5_PACKAGE_PROXY');c.name='D24V10F5_OFFICIAL_D24V10Fx_FAMILY_STEP'
 c.attributes.add('SupplierAudit','Source','https://www.pololu.com/product/2831/resources ; shared D24V10Fx STEP, downloaded and geometrically compared 2026-09-26')
 assert d.computeAll()
 result={'revision':'Rev-B.4','timeline_items':d.timeline.count,'changed_prints':['PRINT_20'],'nut_envelope_diameter_mm':8.1,'backup':backup,'assembly_release_passed':False}
 with open(os.path.join(BASE,'verification','RevB4_Migration.json'),'w') as f:json.dump(result,f,indent=2)
 print(json.dumps(result))
