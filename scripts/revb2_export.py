"""Export the active validated Rev-B.2 model. No screenshots of optional bodies."""
import adsk.core,adsk.fusion,os,json,zipfile
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def run(_context: str):
 a=adsk.core.Application.get();doc=a.activeDocument;d=adsk.fusion.Design.cast(a.activeProduct);r=d.rootComponent
 assert doc.name=='Energized_Water_Scanner'
 def physical(o):return not o.name.startswith(('DATUM','REFERENCE','OPTION','CLEARANCES'))
 prints=[o for o in r.allOccurrences if o.name.startswith('PRINT_')]
 assert len(prints)==16
 for o in prints:
  assert o.bRepBodies.count==1 and o.bRepBodies.item(0).lumps.count==1
  opt=d.exportManager.createSTLExportOptions(o,os.path.join(BASE,'prints',o.component.name+'.stl'))
  opt.meshRefinement=adsk.fusion.MeshRefinementSettings.MeshRefinementHigh
  opt.unitType=adsk.fusion.DistanceUnits.MillimeterDistanceUnits
  opt.isBinaryFormat=True;assert d.exportManager.execute(opt)
 with zipfile.ZipFile(os.path.join(BASE,'prints','Print_STLs.zip'),'w',zipfile.ZIP_DEFLATED) as z:
  for o in sorted(prints,key=lambda o:o.component.name):z.write(os.path.join(BASE,'prints',o.component.name+'.stl'),o.component.name+'.stl')
 assert d.exportManager.execute(d.exportManager.createFusionArchiveExportOptions(os.path.join(BASE,'cad','Energized_Water_Scanner_RevB2.f3d')))
 # Build a disposable physical-only design for STEP, preserving full assembly coordinates.
 mgr=adsk.fusion.TemporaryBRepManager.get()
 copies=[(o.component.name,[(b.name,mgr.copy(b)) for b in o.bRepBodies if b.isSolid]) for o in r.allOccurrences if physical(o) and o.bRepBodies.count]
 tmp=a.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
 td=adsk.fusion.Design.cast(a.activeProduct);td.designType=adsk.fusion.DesignTypes.DirectDesignType
 for name,bs in copies:
  o=td.rootComponent.occurrences.addNewComponent(adsk.core.Matrix3D.create());o.component.name=name
  for bn,b in bs:o.component.bRepBodies.add(b).name=bn
 assert td.exportManager.execute(td.exportManager.createSTEPExportOptions(os.path.join(BASE,'cad','Energized_Water_Scanner_RevB2.step')))
 tmp.close(False);doc.activate()
 print(json.dumps({'prints':len(prints),'step_solids':sum(len(bs) for _,bs in copies),'timeline':d.timeline.count}))
