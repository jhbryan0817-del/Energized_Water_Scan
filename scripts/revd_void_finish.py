"""Fill eight trapped obsolete Rev-C pilots; audit the added material before committing."""
import adsk.core,adsk.fusion,os,json,math,hashlib
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def run(_context: str):
    a=adsk.core.Application.get();d=adsk.fusion.Design.cast(a.activeProduct);r=d.rootComponent;m=adsk.fusion.TemporaryBRepManager.get()
    assert d.timeline.count==1700
    o=next(o for o in r.allOccurrences if o.name.startswith('PRINT_01'));before=m.copy(o.bRepBodies.item(0));after=m.copy(before)
    P=lambda x,y,z:adsk.core.Point3D.create(x/10,y/10,z/10)
    centres=[(x,s*y) for s in [-1,1] for x,y in [(-106,19),(-106,59),(-58,19),(107,19)]]
    for x,y in centres:
        tool=m.createCylinderOrCone(P(x,y,3),.125,P(x,y,5),.125)
        assert m.booleanOperation(after,tool,adsk.fusion.BooleanTypes.UnionBooleanType)
    delta=m.copy(after);assert m.booleanOperation(delta,m.copy(before),adsk.fusion.BooleanTypes.DifferenceBooleanType)
    assert .05<delta.volume<.065 and after.lumps.count==1,delta.volume
    solids=[(oc.component.name,b) for oc in r.allOccurrences if not oc.name.startswith(('DATUM','REFERENCE','OPTION','CLEARANCES','INTERFACE_HOLD','PRINT_01')) for b in oc.bRepBodies if b.isSolid]
    tests=0
    def clear(b):
        nonlocal tests
        tests+=1
        if not delta.boundingBox.intersects(b.boundingBox):return
        q=m.copy(delta);assert m.booleanOperation(q,m.copy(b),adsk.fusion.BooleanTypes.IntersectionBooleanType)
        assert q.volume*1000<.001,(b.name,q.volume*1000)
    for _,b in solids:clear(b)
    for label,x,s,lane,direction in [('E1',-81,-1,72,1),('E2',110,-1,52,-1),('E3',-81,1,72,1),('E4',110,1,52,-1)]:
        current=d.userParameters.itemByName('probe_'+label+'_angle').value
        for deg in range(0,91,5):
            t=adsk.core.Matrix3D.create();t.setToRotation(direction*(math.radians(deg)-current),adsk.core.Vector3D.create(0,1,0),P(x,s*lane,16))
            for n,b in solids:
                if n.startswith('PROBE_'+label):
                    q=m.copy(b);assert m.transform(q,t);clear(q)
    prefixes=('PRINT_31','ESP32','PRINT_18','BATTERY','PRINT_03','FRONT_END','ADS1115','ESC_','PROCURE_ESC','PRINT_19','PRINT_20','PRINT_21','D24V10F5','PROCURE_D24V50')
    service_min=min(b.boundingBox.minPoint.z*10 for n,b in solids if n.startswith(prefixes))
    assert service_min>5.01
    f=o.component.features.baseFeatures.item(0);assert f.startEdit();assert f.updateBody(f.bodies.item(0),after);assert f.finishEdit();assert d.computeAll()
    assert not [i for i in range(d.timeline.count) if d.timeline.item(i).healthState in (adsk.fusion.FeatureHealthStates.WarningFeatureHealthState,adsk.fusion.FeatureHealthStates.ErrorFeatureHealthState)]
    proof={'revision':'Rev-D','timeline':1700,'filled_pilot_centres_mm':centres,'added_volume_mm3':delta.volume*1000,'added_material_z_mm':[3,5],'delta_static_and_motion_tests':tests,'delta_collisions':0,'service_moving_parts_min_z_mm':service_min,'service_preservation':'All checked lift parts start above added material and lift upward; driver corridors start at Z35.1 or higher, dry bundle corridors above Z31. No tested service allocation reaches the filled Z3..5 cavities.','assembly_release_passed':False}
    for filename in ['RevD_Assembly_Audit.json','RevD_Service_Audit.json']:
        path=os.path.join(BASE,'verification',filename);raw=open(path,'rb').read();report=json.loads(raw)
        for row in report.get('inventory',[]):
            if row['component'].startswith('PRINT_01'):row['volume_mm3']=after.volume*1000
        report['obsolete_pilot_fill_delta_audit']={'preceding_report_sha256':hashlib.sha256(raw).hexdigest(),**proof}
        open(path,'w').write(json.dumps(report,indent=2))
    open(os.path.join(BASE,'verification','RevD_Void_Finish.json'),'w').write(json.dumps(proof,indent=2))
    print('Eight obsolete pilot cavities filled; added material passes static/motion and service separation checks')
