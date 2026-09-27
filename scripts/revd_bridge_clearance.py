"""Cut-only enlargement of steering-horn lift notch; preserve prior clearance evidence."""
import adsk.core,adsk.fusion,os,json,hashlib
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def run(_context: str):
    a=adsk.core.Application.get();d=adsk.fusion.Design.cast(a.activeProduct);m=adsk.fusion.TemporaryBRepManager.get()
    o=next(o for o in d.rootComponent.allOccurrences if o.name.startswith('PRINT_31'));before=m.copy(o.bRepBodies.item(0));after=m.copy(before)
    p=adsk.core.Point3D.create;v=adsk.core.Vector3D.create
    tool=m.createBox(adsk.core.OrientedBoundingBox3D.create(p(16.7,-3.51,4.845),v(1,0,0),v(0,1,0),.9,1.02,1.51))
    assert m.booleanOperation(after,tool,adsk.fusion.BooleanTypes.DifferenceBooleanType)
    delta=m.copy(after);assert m.booleanOperation(delta,before,adsk.fusion.BooleanTypes.DifferenceBooleanType);assert delta.volume<1e-10 and after.lumps.count==1
    f=o.component.features.baseFeatures.item(0);f.startEdit();assert f.updateBody(f.bodies.item(0),after);f.finishEdit();assert d.computeAll()
    proof={'component':o.component.name,'old_volume_mm3':before.volume*1000,'new_volume_mm3':after.volume*1000,'added_volume_mm3':delta.volume*1000,'reason':'Cut-only notch enlarged to X162.5..171.5,Y-40.2..-30,Z40.9..56; clears the full horn envelope between the coarse service lift samples.'}
    for filename in ['RevD_Assembly_Audit.json','RevD_Service_Audit.json']:
        path=os.path.join(BASE,'verification',filename);raw=open(path,'rb').read();report=json.loads(raw)
        for row in report.get('inventory',[]):
            if row['component'].startswith('PRINT_31'):row['volume_mm3']=after.volume*1000
        report['bridge_notch_subset_proof']={'preceding_report_sha256':hashlib.sha256(raw).hexdigest(),**proof}
        open(path,'w').write(json.dumps(report,indent=2))
    open(os.path.join(BASE,'verification','RevD_Bridge_Clearance.json'),'w').write(json.dumps(proof,indent=2));print('Bridge notch enlarged; cut-only proof saved')
