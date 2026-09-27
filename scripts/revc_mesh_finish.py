"""Resolve old entry's tangent internal contact; remove obsolete rail fill projections."""
import adsk.core,adsk.fusion,os,json
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def run(_context: str):
    app=adsk.core.Application.get();d=adsk.fusion.Design.cast(app.activeProduct);r=d.rootComponent
    assert d.timeline.count==1487
    m=adsk.fusion.TemporaryBRepManager.get();P=lambda x,y,z:adsk.core.Point3D.create(x/10,y/10,z/10);V=adsk.core.Vector3D.create
    def box(x0,y0,z0,x1,y1,z1):return m.createBox(adsk.core.OrientedBoundingBox3D.create(P((x0+x1)/2,(y0+y1)/2,(z0+z1)/2),V(1,0,0),V(0,1,0),(x1-x0)/10,(y1-y0)/10,(z1-z0)/10))
    def cyl(a,b,diam):return m.createCylinderOrCone(P(*a),diam/20,P(*b),diam/20)
    def comp(pre):return next(o.component for o in r.allOccurrences if o.name.startswith(pre))
    def modify(c,t,name,join=False):
        target=c.bRepBodies.item(0);f=c.features.baseFeatures.add();f.name=name+'_tool';assert f.startEdit();c.bRepBodies.add(t,f);assert f.finishEdit()
        oc=adsk.core.ObjectCollection.create();oc.add(f.bodies.item(0));i=c.features.combineFeatures.createInput(target,oc);i.operation=adsk.fusion.FeatureOperations.JoinFeatureOperation if join else adsk.fusion.FeatureOperations.CutFeatureOperation;c.features.combineFeatures.add(i).name=name
    for label,x,s,num in [('E1',-75,-1,22),('E2',90,-1,23),('E3',-75,1,24),('E4',90,1,25)]:
        def tr(b):
            t=adsk.core.Matrix3D.create();t.setWithArray([1,0,0,x/10,0,s,0,0,0,0,1,0,0,0,0,1]);assert m.transform(b,t);return b
        c=comp('PRINT_'+str(num))
        modify(c,tr(box(-25.01,56.9,-33,-14.9,60,-22.9)),'RevC_'+label+'_remove_tangent_entry_stub')
        modify(c,tr(cyl((-23,57,-28),(-23,69,-28),8)),'RevC_'+label+'_continuous_entry_web',True)
        modify(c,tr(cyl((-23,56.9,-28),(-23,69.1,-28),4)),'RevC_'+label+'_restore_entry_bore')
    hull=comp('PRINT_01')
    for x in [-108,-98]:modify(hull,cyl((x,0,68),(x,0,71.1),2.6),'RevC_flush_obsolete_rail_fill')
    assert d.computeAll()
    result={'revision':'Rev-C.1','timeline':d.timeline.count,'fixes':['Remove tangential old entry stub at pod floor; rejoin offset entry','Trim obsolete rail bore fills flush to deckZ68'],'assembly_release_passed':False}
    with open(os.path.join(BASE,'verification','RevC_Mesh_Finish.json'),'w') as f:json.dump(result,f,indent=2)
    print(json.dumps(result))
