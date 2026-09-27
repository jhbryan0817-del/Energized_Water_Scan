"""Reopen Rev-C.1 F3D and compare physical BRep volumes, parameters and timeline."""
import adsk.core,adsk.fusion,json,os
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def run(_context: str):
    a=adsk.core.Application.get();original=a.activeDocument;d=adsk.fusion.Design.cast(a.activeProduct)
    def inv(d):return {o.fullPathName+'/'+b.name:round(b.volume*1000,5) for o in d.rootComponent.allOccurrences if not o.name.startswith(('DATUM','REFERENCE','OPTION','CLEARANCES','INTERFACE_HOLD')) for b in o.bRepBodies if b.isSolid}
    expected=inv(d);timeline=d.timeline.count;params={p.name:p.expression for p in d.userParameters}
    doc=a.importManager.importToNewDocument(a.importManager.createFusionArchiveImportOptions(os.path.join(BASE,'cad','Energized_Water_Scanner_RevC1.f3d')));assert doc
    new=adsk.fusion.Design.cast(a.activeProduct);actual=inv(new)
    issues=[dict(index=i,name=new.timeline.item(i).name,message=new.timeline.item(i).errorOrWarningMessage) for i in range(new.timeline.count) if new.timeline.item(i).healthState in (adsk.fusion.FeatureHealthStates.WarningFeatureHealthState,adsk.fusion.FeatureHealthStates.ErrorFeatureHealthState)]
    result={'revision':'Rev-C.1','timeline':new.timeline.count,'body_count':len(actual),'parameters':len(params),'feature_issues':issues,'volumes_match':actual==expected,'passed':actual==expected and new.timeline.count==timeline and {p.name:p.expression for p in new.userParameters}==params and not issues}
    with open(os.path.join(BASE,'verification','RevC_Native_Roundtrip.json'),'w') as f:json.dump(result,f,indent=2)
    assert result['passed'],result
    doc.close(False);original.activate()
    assert original.save('Rev-C.1: four0-90deg articulated probes,150mm reach; no magnetometer; dry pods and replaceable seal cartridges; first-iteration holds documented')
    print(json.dumps(result));print('Original scanner cloud design saved')
