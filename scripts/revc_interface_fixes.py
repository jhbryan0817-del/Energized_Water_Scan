"""Apply once after revc_build.py (1439 timeline items)."""
import adsk.core,adsk.fusion,json,os
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def run(_context: str):
    app=adsk.core.Application.get();d=adsk.fusion.Design.cast(app.activeProduct);r=d.rootComponent
    assert d.timeline.count==1439
    m=adsk.fusion.TemporaryBRepManager.get();P=lambda x,y,z:adsk.core.Point3D.create(x/10,y/10,z/10);V=adsk.core.Vector3D.create
    def box(x0,y0,z0,x1,y1,z1):return m.createBox(adsk.core.OrientedBoundingBox3D.create(P((x0+x1)/2,(y0+y1)/2,(z0+z1)/2),V(1,0,0),V(0,1,0),(x1-x0)/10,(y1-y0)/10,(z1-z0)/10))
    def cyl(a,b,diam):return m.createCylinderOrCone(P(*a),diam/20,P(*b),diam/20)
    def comp(pre):return next(o.component for o in r.allOccurrences if o.name.startswith(pre))
    def modify(c,t,name,join=False):
        target=c.bRepBodies.item(0);f=c.features.baseFeatures.add();f.name=name+'_tool';assert f.startEdit();c.bRepBodies.add(t,f);assert f.finishEdit()
        oc=adsk.core.ObjectCollection.create();oc.add(f.bodies.item(0));i=c.features.combineFeatures.createInput(target,oc);i.operation=adsk.fusion.FeatureOperations.JoinFeatureOperation if join else adsk.fusion.FeatureOperations.CutFeatureOperation;c.features.combineFeatures.add(i).name=name
    hull=comp('PRINT_01')
    for s in [-1,1]:
        # Only the two inboard forward bosses of the aft pods conflict with the motor foot.
        modify(hull,cyl((59,s*19,2),(59,s*19,8.01),2.5),'RevC_motor_foot_pilot_floor',True)
        modify(hull,cyl((59,s*19,3),(59,s*19,8.1),8.01),'RevC_motor_foot_flush_boss')
    for label,x,s,num in [('E1',-75,-1,22),('E2',90,-1,23),('E3',-75,1,24),('E4',90,1,25)]:
        c=comp('PRINT_'+str(num))
        def tr(b):
            t=adsk.core.Matrix3D.create();t.setWithArray([1,0,0,x/10,0,s,0,0,0,0,1,0,0,0,0,1]);assert m.transform(b,t);return b
        def B(*v):return tr(box(*v))
        def C(a,b,diam):return tr(cyl(a,b,diam))
        # Close old entry, clear its external boss, leave a flat full cartridge gasket land.
        modify(c,C((-20,57,-28),(-20,67,-28),4),'RevC_'+label+'_close_old_entry',True)
        modify(c,B(-28,64,-33,-14,69,-22),'RevC_'+label+'_remove_old_entry_boss')
        modify(c,B(-18.2,64,-31.2,18.2,66,-4.9),'RevC_'+label+'_cartridge_flange_relief')
        modify(c,C((-23,57,-28),(-23,69,-28),8),'RevC_'+label+'_offset_entry_boss',True)
        modify(c,C((-23,56.9,-28),(-23,69.1,-28),4),'RevC_'+label+'_offset_potted_entry')
    assert d.computeAll()
    report={'revision':'Rev-C.1','timeline':d.timeline.count,'fixes':['Two aft-pod forward/inboard hull bosses flush atZ3; closed pilot floorZ2; use M3x8 here','Cartridge flange clears pod flange; electrode entry moves to localx=-23'],'assembly_release_passed':False}
    with open(os.path.join(BASE,'verification','RevC_Interface_Fixes.json'),'w') as f:json.dump(report,f,indent=2)
    print(json.dumps(report))
