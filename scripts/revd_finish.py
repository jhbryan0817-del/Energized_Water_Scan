"""One-time final packaging corrections after Rev-D refinement (1691 items)."""
import adsk.core,adsk.fusion,os,json
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def run(_context: str):
    app=adsk.core.Application.get();d=adsk.fusion.Design.cast(app.activeProduct);root=d.rootComponent
    assert d.timeline.count==1691
    m=adsk.fusion.TemporaryBRepManager.get();P=lambda x,y,z:adsk.core.Point3D.create(x/10,y/10,z/10);V=adsk.core.Vector3D.create
    def box(x0,y0,z0,x1,y1,z1):return m.createBox(adsk.core.OrientedBoundingBox3D.create(P((x0+x1)/2,(y0+y1)/2,(z0+z1)/2),V(1,0,0),V(0,1,0),(x1-x0)/10,(y1-y0)/10,(z1-z0)/10))
    def cy(a,b,di):return m.createCylinderOrCone(P(*a),di/20,P(*b),di/20)
    def op(a,b,k):assert m.booleanOperation(a,b,k);return a
    def union(a,b):return op(a,b,adsk.fusion.BooleanTypes.UnionBooleanType)
    def cut(a,b):return op(a,b,adsk.fusion.BooleanTypes.DifferenceBooleanType)
    def occ(pre):return next(o for o in root.allOccurrences if o.name.startswith(pre))
    def shift(b,x=0,y=0,z=0):
        t=adsk.core.Matrix3D.create();t.translation=V(x/10,y/10,z/10);assert m.transform(b,t);return b
    src=open(os.path.join(BASE,'scripts','revd_refine.py')).read();src=src[:src.index('    # Update existing source bodies')]
    src=src.replace('assert d.timeline.count==1664','assert d.timeline.count==1691').replace("('E1',-86,-1,72,1)","('E1',-81,-1,72,1)").replace("('E3',-86,1,72,1)","('E3',-81,1,72,1)")
    src+='\n    return partmap,moving,hatch,gasket\n'
    ns={'__file__':os.path.join(BASE,'scripts','revd_refine.py')};exec(compile(src,ns['__file__'],'exec'),ns);parts,moving,hatch,gasket=ns['run']('')
    hull=parts['PRINT_01_Hull_shell'][0][1]
    # Retrim all recesses after adding tray pillars, preserving the channel roofs.
    for s in [-1,1]:
        cut(hull,box(-63,min(s*42,s*59.6),-.1,117,max(s*42,s*59.6),24))
    # Extend bore ahead of the stern tube so no support touches its rotating shaft.
    shaft=next(b for b in occ('DRIVELINE').bRepBodies if 'shaft_178' in b.name)
    centres=[e.geometry.center for e in shaft.edges if isinstance(e.geometry,adsk.core.Circle3D)]
    p0=min(centres,key=lambda p:p.x);p1=max(centres,key=lambda p:p.x)
    cut(hull,m.createCylinderOrCone(p0,.325,p1,.325))
    # Remove only overlap introduced by added local interior packaging structures.
    for pre in ['PRINT_09','SEAL_Steering']:
        for b in occ(pre).bRepBodies:cut(hull,m.copy(b))
    # Lower aft electronics to clear the hatch ledge and upper-journal allocation.
    cradle=parts['PRINT_04_Longitudinal_battery_cradle'][0][1];shift(cradle,0,0,-2)
    for x in [88,140,189]:cut(hull,box(x-2.01,-19.01,23,x+2.01,19.01,25.1))
    upper=parts['PRINT_31_Upper_controller_bridge'][0][1];shift(upper,0,0,-3)
    for x in [142,184]:
        for y in [-35,35]:cut(hull,cy((x,y,41),(x,y,44.1),8.01))
    # Upper bridge skirts must not intersect rear-well cover or transom pad.
    cut(upper,box(130,-25,44,138.5,25,58));cut(upper,box(186.5,-25,40,189,25,50))
    # Offset steering base geometry protruding beyond the interior is trimmed,
    # while both M2 servo-lug columns remain intact.
    saddle=parts['PRINT_30_Steering_service_saddle'][0][1]
    cut(saddle,box(130,-80,15,185,-66,44))
    cut(saddle,m.copy(hull))
    for x in [143,178]:
        cut(hull,cy((x,-72,3),(x,-72,16.1),7.01))
        union(hull,cut(cy((x,-62,3),(x,-62,16),7),cy((x,-62,8),(x,-62,16.1),2.5)))
        cut(saddle,cy((x,-62,15.9),(x,-62,19.1),3.4))
    # The cover is the last assembly inserted; clip its outer bow corners to the
    # shell clearance (outside its screw holes), not the water boundary.
    for pre in ['PRINT_22_E1','PRINT_24_E3']:
        key=next(k for k in parts if k.startswith(pre));cut(parts[key][0][1],m.copy(hull))
    for name,bs in parts.items():
        for bn,b in bs:assert b.isSolid and b.lumps.count==1,(name,bn,b.lumps.count)
    for name,bs in parts.items():
        c=occ(name).component;f=c.features.baseFeatures.item(0);assert f.startEdit()
        for b,(bn,new) in zip(list(f.bodies),bs):assert f.updateBody(b,new);b.name=bn
        assert f.finishEdit()
    # Move the two forward arm source bodies and their fixed axis consistently.
    # Preserve staged component-owned drivers; revd_angle_finish fixes earlier
    # rotations at zero after the final axes have been created.
    for label,x,s,lane,direction,bs in moving:
        if label not in ['E1','E3']:continue
        o=occ('PROBE_'+label);c=o.component;f=c.features.baseFeatures.item(0);f.startEdit()
        for b,(bn,new) in zip(list(f.bodies),bs):assert f.updateBody(b,new);b.name=bn
        f.finishEdit();pi=c.constructionPlanes.createInput();pi.setByOffset(c.xYConstructionPlane,adsk.core.ValueInput.createByString('16 mm'));pl=c.constructionPlanes.add(pi);pl.isLightBulbOn=False
        sk=c.sketches.add(pl);sk.name='RevD_finished_'+label+'_axis';line=sk.sketchCurves.sketchLines.addByTwoPoints(P(x,-1,0),P(x,1,0));line.isConstruction=True;line.isFixed=True;sk.isVisible=False
        oc=adsk.core.ObjectCollection.create()
        for b in c.bRepBodies:oc.add(b.createForAssemblyContext(o))
        mi=root.features.moveFeatures.createInput2(oc);mi.defineAsRotate(line.createForAssemblyContext(o),adsk.core.ValueInput.createByString('probe_'+label+'_angle'));root.features.moveFeatures.add(mi).name='RevD_'+label+'_angle_driven_rotation'
    def move(pre,dz):
        oc=adsk.core.ObjectCollection.create()
        for b in occ(pre).bRepBodies:oc.add(b)
        t=adsk.core.Matrix3D.create();t.translation=V(0,0,dz/10);mi=root.features.moveFeatures.createInput2(oc);mi.defineAsFreeMove(t);root.features.moveFeatures.add(mi).name='RevD_lower_'+pre
    move('BATTERY',-2);move('ESP32',-3);move('PRINT_18',-3)
    # Resolve nominal linkage pin overlap with proper eye clearances. The joint
    # remains a fabrication allocation, rather than falsely reporting interference.
    o=occ('PROCURE_Steering_dogleg');b=m.copy(o.bRepBodies.item(0))
    cut(b,box(160,-45,57,172,-30,60))
    for x,y in [(167,-36),(278,-21)]:cut(b,cy((x,y,58),(x,y,63),2.2))
    assert b.lumps.count==1
    f=o.component.features.baseFeatures.item(0);f.startEdit();f.updateBody(f.bodies.item(0),b);f.finishEdit()
    # Existing moving pin exceeds ledge by 1 mm: only a local dry underside relief.
    h=occ('PRINT_01').component;f=h.features.baseFeatures.item(0);b=m.copy(h.bRepBodies.item(0));cut(b,box(165.5,-38,60,168.5,-34,62.5));f.startEdit();f.updateBody(f.bodies.item(0),b);f.finishEdit()
    assert d.computeAll()
    open(os.path.join(BASE,'verification','RevD_Finish.json'),'w').write(json.dumps({'revision':'Rev-D','timeline':d.timeline.count,'forward_station_x_mm':-81,'rear_station_x_mm':110,'assembly_release_passed':False},indent=2));print('Finish applied')
