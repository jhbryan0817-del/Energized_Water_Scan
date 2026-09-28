"""Reopen Rev-E F3D and compare physical BRep volumes, parameters and timeline."""
import adsk.core,adsk.fusion,json,os
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def run(_context: str):
    a=adsk.core.Application.get();original=a.activeDocument;d=adsk.fusion.Design.cast(a.activeProduct)
    def inv(d):return {o.fullPathName+'/'+b.name:round(b.volume*1000,5) for o in d.rootComponent.allOccurrences if not o.name.startswith(('DATUM','REFERENCE','OPTION','CLEARANCES','INTERFACE_HOLD')) for b in o.bRepBodies if b.isSolid}
    expected_transform={o.fullPathName:o.transform2.asArray() for o in d.rootComponent.allOccurrences};expected=inv(d);timeline=d.timeline.count;params={p.name:p.expression for p in d.userParameters}
    def drivers(design):return {(o.component.name,f.timelineObject.index):f.definition.angle.expression for o in design.rootComponent.allOccurrences if o.name.startswith('PROBE_') for f in o.component.features.moveFeatures if 'angle_driven_rotation' in f.name}
    expected_drivers=drivers(d)
    audited=json.loads(open(os.path.join(BASE,'verification','RevE_Assembly_Audit.json')).read())
    live={(o.component.name,b.name):b for o in d.rootComponent.allOccurrences for b in o.bRepBodies if b.isSolid}
    for row in audited['inventory']:
        b=live[(row['component'],row['body'])]
        assert abs(b.volume*1000-row['volume_mm3'])<1e-4
        assert max(abs(v*10-w) for v,w in zip(b.boundingBox.minPoint.asArray(),row['min_mm']))<1e-4
        assert max(abs(v*10-w) for v,w in zip(b.boundingBox.maxPoint.asArray(),row['max_mm']))<1e-4
    doc=a.importManager.importToNewDocument(a.importManager.createFusionArchiveImportOptions(os.path.join(BASE,'cad','Energized_Water_Scanner_RevE.f3d')));assert doc
    new=adsk.fusion.Design.cast(a.activeProduct);actual=inv(new)
    assert {o.fullPathName:o.transform2.asArray() for o in new.rootComponent.allOccurrences}==expected_transform
    assert next(o for o in new.rootComponent.allOccurrences if o.name.startswith('PRINT_01')).isGrounded
    issues=[dict(index=i,name=new.timeline.item(i).name,message=new.timeline.item(i).errorOrWarningMessage) for i in range(new.timeline.count) if new.timeline.item(i).healthState in (adsk.fusion.FeatureHealthStates.WarningFeatureHealthState,adsk.fusion.FeatureHealthStates.ErrorFeatureHealthState)]
    result={'revision':'Rev-E','timeline':new.timeline.count,'body_count':len(actual),'parameters':len(params),'feature_issues':issues,'volumes_match':actual==expected,'audited_stowed_geometry_matches':True,'native_rotation_expressions_match':drivers(new)==expected_drivers,'passed':actual==expected and new.timeline.count==timeline and {p.name:p.expression for p in new.userParameters}==params and drivers(new)==expected_drivers and not issues}
    with open(os.path.join(BASE,'verification','RevE_Native_Roundtrip.json'),'w') as f:json.dump(result,f,indent=2)
    assert result['passed'],result
    doc.close(False);original.activate()
    assert original.save('Rev-E: grounded aligned hull, reinforced walls/arms/covers/mounts/cradle and explicit potted wire entries; fit prototype with sealing and transmission holds')
    print(json.dumps(result));print('Original scanner cloud design saved')
