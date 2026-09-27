"""Final aft lift-out aperture and battery-cradle tube clearance, once at 1700 items."""
import adsk.core,adsk.fusion,os,json
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def run(_context: str):
    app=adsk.core.Application.get();doc=app.activeDocument;d=adsk.fusion.Design.cast(app.activeProduct);assert d.timeline.count==1700
    m=adsk.fusion.TemporaryBRepManager.get();P=lambda x,y,z:adsk.core.Point3D.create(x/10,y/10,z/10);V=adsk.core.Vector3D.create
    def box(x0,y0,z0,x1,y1,z1):return m.createBox(adsk.core.OrientedBoundingBox3D.create(P((x0+x1)/2,(y0+y1)/2,(z0+z1)/2),V(1,0,0),V(0,1,0),(x1-x0)/10,(y1-y0)/10,(z1-z0)/10))
    def cy(x,y,z0,z1,di):return m.createCylinderOrCone(P(x,y,z0),di/20,P(x,y,z1),di/20)
    def cut(a,b):assert m.booleanOperation(a,b,adsk.fusion.BooleanTypes.DifferenceBooleanType);return a
    def occ(pre):return next(o for o in d.rootComponent.allOccurrences if o.name.startswith(pre))
    hull=m.copy(occ('PRINT_01').bRepBodies.item(0));cut(hull,box(-100,-65,55,193,65,74))
    tmp=app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType);td=adsk.fusion.Design.cast(app.activeProduct);td.designType=adsk.fusion.DesignTypes.DirectDesignType
    def prism(pts,z0,z1):
        sk=td.rootComponent.sketches.add(td.rootComponent.xYConstructionPlane)
        for p,q in zip(pts,pts[1:]+pts[:1]):sk.sketchCurves.sketchLines.addByTwoPoints(P(*p,0),P(*q,0))
        f=td.rootComponent.features.extrudeFeatures.addSimple(sk.profiles.item(0),adsk.core.ValueInput.createByReal((z1-z0)/10),adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        b=m.copy(f.bodies.item(0));t=adsk.core.Matrix3D.create();t.translation=V(0,0,z0/10);assert m.transform(b,t);return b
    opening=[(-109,-55),(-101,-65),(193,-65),(193,65),(-101,65),(-109,55)]
    hatch=prism([(-119,-60),(-107,-77),(200,-77),(200,77),(-107,77),(-119,60)],70,73)
    gasket=cut(prism([(-112,-57),(-104,-74),(199,-74),(199,74),(-104,74),(-112,57)],68,70),prism(opening,67,71))
    tmp.close(False);doc.activate()
    holes=[(-115.5,0),(-105,-70),(-105,70),(42.5,-71),(42.5,71),(171,-71),(171,71),(196.5,-60),(196.5,0),(196.5,60)]
    for x,y in holes:
        cut(hull,cy(x,y,62,68.1,2.5));cut(hatch,cy(x,y,69.9,73.1,3.4));cut(gasket,cy(x,y,67.9,70.1,3.4))
    # Round tube clearance starts ahead of the cradle nose and extends along the
    # true shaft axis; no contact with the rotating driveline in installed pose.
    cradle=m.copy(occ('PRINT_04').bRepBodies.item(0));tube=next(b for b in occ('DRIVELINE').bRepBodies if 'stern_tube' in b.name)
    pts=[e.geometry.center for e in tube.edges if isinstance(e.geometry,adsk.core.Circle3D)]
    p0=min(pts,key=lambda p:p.x);p1=max(pts,key=lambda p:p.x);cut(cradle,m.createCylinderOrCone(p0,.325,p1,.325))
    for pre,new in [('PRINT_01',hull),('PRINT_02',hatch),('SEAL_Main_hatch',gasket),('PRINT_04',cradle)]:
        assert new.isSolid and new.lumps.count==1,pre
        c=occ(pre).component;f=c.features.baseFeatures.item(0);f.startEdit();assert f.updateBody(f.bodies.item(0),new);f.finishEdit()
    assert d.computeAll()
    open(os.path.join(BASE,'verification','RevD_Access_Finish.json'),'w').write(json.dumps({'revision':'Rev-D','timeline':d.timeline.count,'hatch_fastener_centres_mm':holes,'hatch_aperture_aft_x_mm':193,'hatch_max_length_mm':319,'assembly_release_passed':False},indent=2));print('Lift-out access finished')
