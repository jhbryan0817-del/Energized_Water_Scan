"""Add flush M2 cradle retention; prove this cut-only change preserves motion clearance."""
import adsk.core,adsk.fusion,os,json,hashlib
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def run(_context: str):
    a=adsk.core.Application.get();d=adsk.fusion.Design.cast(a.activeProduct);m=adsk.fusion.TemporaryBRepManager.get()
    path=os.path.join(BASE,'verification','RevD_Assembly_Audit.json');raw=open(path,'rb').read();audit=json.loads(raw)
    assert audit['timeline']==d.timeline.count==1700 and not audit['interferences'] and not audit['sampled_motion_collisions'] and not audit['feature_issues']
    P=lambda x,y,z:adsk.core.Point3D.create(x/10,y/10,z/10)
    def occ(pre):return next(o for o in d.rootComponent.allOccurrences if o.name.startswith(pre))
    before={pre:m.copy(occ(pre).bRepBodies.item(0)) for pre in ['PRINT_01','PRINT_04']}
    after={pre:m.copy(b) for pre,b in before.items()}
    def cut(b,t):assert m.booleanOperation(b,t,adsk.fusion.BooleanTypes.DifferenceBooleanType)
    holes=[(x,y) for x in [88,189] for y in [-13,13]]
    for x,y in holes:
        cut(after['PRINT_04'],m.createCylinderOrCone(P(x,y,22.9),.11,P(x,y,25.1),.11))
        cut(after['PRINT_04'],m.createCylinderOrCone(P(x,y,23.8),.11,P(x,y,25),.23))
        cut(after['PRINT_01'],m.createCylinderOrCone(P(x,y,18),.085,P(x,y,23.1),.085))
    proof=[]
    for pre,b in after.items():
        delta=m.copy(b);cut(delta,m.copy(before[pre]));assert delta.volume<1e-10
        assert b.lumps.count==1
        proof.append(dict(component=pre,old_volume_mm3=before[pre].volume*1000,new_volume_mm3=b.volume*1000,added_volume_mm3=delta.volume*1000))
        c=occ(pre).component;f=c.features.baseFeatures.item(0);f.startEdit();assert f.updateBody(f.bodies.item(0),b);f.finishEdit()
    assert d.computeAll()
    issues=[i for i in range(d.timeline.count) if d.timeline.item(i).healthState in [adsk.fusion.FeatureHealthStates.WarningFeatureHealthState,adsk.fusion.FeatureHealthStates.ErrorFeatureHealthState]];assert not issues
    for row in audit['inventory']:
        if row['component'].startswith(('PRINT_01','PRINT_04')):
            b=occ(row['component']).bRepBodies.item(0);row['volume_mm3']=b.volume*1000;row['lumps']=b.lumps.count;row['min_mm']=[round(v*10,5) for v in b.boundingBox.minPoint.asArray()];row['max_mm']=[round(v*10,5) for v in b.boundingBox.maxPoint.asArray()]
    audit['cut_only_clearance_preservation']={'baseline_report_sha256':hashlib.sha256(raw).hexdigest(),'proof':proof,'reason':'Only hull/cradle material removed; each final solid minus its fully motion-audited predecessor is empty. No new collision can be introduced by these cuts. No other body/pose changed.'}
    open(path,'w').write(json.dumps(audit,indent=2))
    open(os.path.join(BASE,'verification','RevD_Cradle_Retention.json'),'w').write(json.dumps({'revision':'Rev-D','timeline':d.timeline.count,'M2_flush_screw_centres_mm':holes,'countersink_top_diameter_mm':4.6,'pilot_diameter_mm':1.7,'pilot_bottom_z_mm':18,'proof':proof,'assembly_release_passed':False},indent=2));print('Flush cradle retention and subset proof saved')
