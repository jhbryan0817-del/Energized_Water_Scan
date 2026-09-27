"""One-time clearance correction of the initial 1664-item Rev-D package.
Reconstructs native base-feature source bodies from the archived Rev-C inputs;
does not reinterpret modified intermediate geometry as supplier geometry.
"""
import adsk.core,adsk.fusion,os,json,math
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def run(_context: str):
    app=adsk.core.Application.get();original=app.activeDocument;d=adsk.fusion.Design.cast(app.activeProduct)
    assert d.timeline.count==1664
    m=adsk.fusion.TemporaryBRepManager.get();P=lambda x,y,z:adsk.core.Point3D.create(x/10,y/10,z/10);V=adsk.core.Vector3D.create
    def box(x0,y0,z0,x1,y1,z1):return m.createBox(adsk.core.OrientedBoundingBox3D.create(P((x0+x1)/2,(y0+y1)/2,(z0+z1)/2),V(1,0,0),V(0,1,0),(x1-x0)/10,(y1-y0)/10,(z1-z0)/10))
    def cy(a,b,diam):return m.createCylinderOrCone(P(*a),diam/20,P(*b),diam/20)
    def op(a,b,k):assert m.booleanOperation(a,b,k);return a
    def union(a,b):return op(a,b,adsk.fusion.BooleanTypes.UnionBooleanType)
    def cut(a,b):return op(a,b,adsk.fusion.BooleanTypes.DifferenceBooleanType)
    def inter(a,b):return op(a,b,adsk.fusion.BooleanTypes.IntersectionBooleanType)
    def shift(b,x=0,y=0,z=0):
        t=adsk.core.Matrix3D.create();t.translation=V(x/10,y/10,z/10);assert m.transform(b,t);return b
    def occ(pre):return next(o for o in d.rootComponent.allOccurrences if o.name.startswith(pre))
    # Generate corrected parts against the immutable native Rev-C.1 export.
    tmp=app.importManager.importToNewDocument(app.importManager.createFusionArchiveImportOptions(os.path.join(BASE,'cad','Energized_Water_Scanner_RevC1.f3d')))
    src=open(os.path.join(BASE,'scripts','revd_build.py')).read()
    src=src[:src.index('    # Prepared geometry is complete before touching the model structure.')]
    src=src.replace("assert app.activeDocument.name=='Energized_Water_Scanner' and d.timeline.count==1523","assert d.timeline.count==1523")
    src='\n'.join(line for line in src.splitlines() if 'createFusionArchiveExportOptions' not in line)
    src=src.replace("('E1',-70,-1,72,1),('E2',85,-1,52,-1),('E3',-70,1,72,1),('E4',85,1,52,-1)","('E1',-86,-1,72,1),('E2',110,-1,52,-1),('E3',-86,1,72,1),('E4',110,1,52,-1)")
    src=src.replace('pulley_y=44.5','pulley_y=43.5').replace('upper_bearing=(16,22)','upper_bearing=(15.5,21.5)')
    src+='\n    return parts,moving\n'
    ns={'__file__':os.path.join(BASE,'scripts','revd_build.py')};exec(compile(src,ns['__file__'],'exec'),ns)
    parts,moving=ns['run']('')
    baseline=adsk.fusion.Design.cast(app.activeProduct)
    oldtray=m.copy(next(o for o in baseline.rootComponent.allOccurrences if o.name.startswith('PRINT_03')).bRepBodies.item(0))
    tmp.close(False);original.activate()
    partmap={name:bs for name,bs in parts};hull=partmap['PRINT_01_Hull_shell'][0][1]
    # Remove obsolete support locations created by the initial preparation.
    for x in [121,189]:
        for y in [-26,26]:cut(hull,cy((x,y,3),(x,y,44.1),8.01))
    for x in [123,158]:
        for y in [-57,-28]:cut(hull,cy((x,y,3),(x,y,16.1),7.01))
    for x in [91,140,193]:cut(hull,box(x-2.01,-19.01,3,x+2.01,19.01,24.1))
    # Preserve full shell thickness at the aft battery pocket within original bounds.
    union(hull,box(187,-24,20,196,24,48));cut(hull,box(185,-21,23,193,21,45))
    # Relieve only the lower redundant rear-center hatch boss; sealing rim remains.
    cut(hull,box(165,-6,57,178,6,64.5))
    # Correct cartridge access pockets, shaft bores and belt flange reliefs.
    for label,x,s,lane,direction in ns['STATIONS']:
        front=direction==1;seat=59 if front else 39;py=43.5 if front else 22.5
        def B(x0,y0,z0,x1,y1,z1):return box(x+x0,min(s*y0,s*y1),z0,x+x1,max(s*y0,s*y1),z1)
        def C(y0,y1,diam,z=16):return cy((x,s*y0,z),(x,s*y1,z),diam)
        # A full 3 mm roof over the flange access pocket, continuous with channels.
        union(hull,B(-21,lane-13,24,21,lane+10.6,32))
        cut(hull,B(-18.2,seat,2.8,18.2,lane+8,29.2))
        cut(hull,C(seat-8,lane+8,22.2))
        cut(hull,C(py-1.1,lane+5,6.4))
        for z in [16,44]:cut(hull,C(py-1.2,py+7.2,16.4,z))
        cut(hull,B(-7.7,py-.2,16,7.7,py+6.2,44))
        # Retain pilot depth behind the continuous cartridge gasket land.
        for hx in [-14,14]:
            for z in [8,24]:cut(hull,cy((x+hx,s*(seat-7),z),(x+hx,s*(seat+.05),z),2.5))
        if front:
            upper=partmap['PROCURE_'+label+'_upper_journal_ALLOCATION'][1][1]
            cut(upper,C(42.4,44.3,7,44))
        # Dedicated wet-to-dry lead entry in the groove roof; potting remains a hold.
        wx=x+direction*30;wy=s*(lane-7)
        union(hull,cy((wx,wy,27),(wx,wy,31),8))
        cut(hull,cy((wx,wy,23.9),(wx,wy,31.1),3.3));cut(hull,cy((wx,wy,27),(wx,wy,31.1),5.5))
    # Shift the separate steering saddle aft/outboard; horn and pin follow it.
    saddle=partmap['PRINT_30_Steering_service_saddle'][0][1];shift(saddle,20,-15,0)
    for x in [143,178]:
        for y in [-72,-43]:union(hull,cut(cy((x,y,3),(x,y,16),7),cy((x,y,8),(x,y,16.1),2.5)))
    union(hull,box(174,-75.5,0,182,-60,4))
    battery=partmap['PRINT_04_Longitudinal_battery_cradle'][0][1];shift(battery,-3.5,0,1)
    cut(battery,box(192,-21,24,194,21,32))
    cut(battery,box(84,-10,24,86.4,10,28))
    for x in [88,140,189]:union(hull,box(x-2,-19,3,x+2,19,25))
    # Rotate the upper controller and its proven capture geometry through 90 deg.
    upper=box(139,-40,44,188,40,47)
    pads=inter(m.copy(oldtray),box(-28,27,19,42,61,25))
    t=adsk.core.Matrix3D.create();t.setWithArray([0,-1,0,19.794,1,0,0,-.413,0,0,1,2.8,0,0,0,1]);assert m.transform(pads,t);union(upper,pads)
    for x in [142,184]:
        for y in [-35,35]:
            cut(upper,cy((x,y,43.9),(x,y,47.1),3.4))
            union(hull,cut(cy((x,y,3),(x,y,44),8),cy((x,y,36),(x,y,44.1),2.5)))
    partmap['PRINT_31_Upper_controller_bridge']=[('Rotated_controller_over_battery',upper)]
    # New support rails must not obstruct the original stern tube or shaft.
    tube=next(b for b in occ('DRIVELINE').bRepBodies if 'stern_tube' in b.name)
    centers=[e.geometry.center for e in tube.edges if isinstance(e.geometry,adsk.core.Circle3D)]
    p0=min(centers,key=lambda p:p.x);p1=max(centers,key=lambda p:p.x)
    assert m.booleanOperation(hull,m.createCylinderOrCone(p0,.325,p1,.325),adsk.fusion.BooleanTypes.DifferenceBooleanType)
    # A larger shaped service opening gives access to the forward wells without
    # changing the hull's bounding footprint. The continuous gasket is replaced.
    temp=app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType);td=adsk.fusion.Design.cast(app.activeProduct);td.designType=adsk.fusion.DesignTypes.DirectDesignType
    def prism(points,z0,z1):
        sk=td.rootComponent.sketches.add(td.rootComponent.xYConstructionPlane)
        for p,q in zip(points,points[1:]+points[:1]):sk.sketchCurves.sketchLines.addByTwoPoints(P(p[0],p[1],0),P(q[0],q[1],0))
        f=td.rootComponent.features.extrudeFeatures.addSimple(sk.profiles.item(0),adsk.core.ValueInput.createByReal((z1-z0)/10),adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        return shift(m.copy(f.bodies.item(0)),0,0,z0)
    outer=[(-120,-62),(-108,-85),(200,-85),(200,85),(-108,85),(-120,62)]
    opening=[(-109,-55),(-101,-65),(165,-65),(165,65),(-101,65),(-109,55)]
    lidoutline=[(-119,-60),(-107,-77),(177,-77),(177,77),(-107,77),(-119,60)]
    gasketoutline=[(-112,-57),(-104,-74),(175,-74),(175,74),(-104,74),(-112,57)]
    ring=prism(outer,61,68);openingtool=prism(opening,54.9,74)
    hatch=prism(lidoutline,70,73);gasket=cut(prism(gasketoutline,68,70),m.copy(openingtool))
    temp.close(False);original.activate()
    cut(hull,box(-121,-86,68,201,86,74));union(hull,ring);cut(hull,openingtool)
    hatchholes=[(-115.5,0),(-105,-70),(-105,70),(42.5,-71),(42.5,71),(171,-71),(171,0),(171,71)]
    for x,y in hatchholes:
        cut(hull,cy((x,y,62),(x,y,68.1),2.5));cut(hatch,cy((x,y,69.9),(x,y,73.1),3.4));cut(gasket,cy((x,y,67.9),(x,y,70.1),3.4))
    for name,bs in partmap.items():
        for bn,b in bs:assert b.isSolid and b.lumps.count==1,(name,bn,b.lumps.count)
    # Update existing source bodies in place, preserving component identity/history.
    for name,bs in partmap.items():
        c=occ(name).component;f=c.features.baseFeatures.item(0);assert f.startEdit()
        old=list(f.bodies);assert len(old)==len(bs),(name,len(old),len(bs))
        for b,(bn,new) in zip(old,bs):assert f.updateBody(b,new);b.name=bn
        assert f.finishEdit()
    for name,bn,new in [('PRINT_02_Removable_hatch_cover','Extended_service_hatch',hatch),('SEAL_Main_hatch_continuous_gasket','RevD_continuous_sheet_gasket',gasket)]:
        old=occ(name);d.rootComponent.features.removeFeatures.add(old).name='RevD_replace_'+name
        oo=d.rootComponent.occurrences.addNewComponent(adsk.core.Matrix3D.create());oo.component.name=name
        f=oo.component.features.baseFeatures.add();f.startEdit();oo.component.bRepBodies.add(new,f).name=bn;f.finishEdit()
    # Existing rotation features reference fixed sketches: recreate the four axes
    # after replacing stowed source bodies, retaining the same user parameters.
    # These body moves belong to the probe components. Preserve the staged
    # timeline here; revd_angle_finish neutralizes all superseded drivers.
    for label,x,s,lane,direction,bs in moving:
        o=occ('PROBE_'+label);c=o.component;f=c.features.baseFeatures.item(0);assert f.startEdit()
        for b,(bn,new) in zip(list(f.bodies),bs):assert f.updateBody(b,new);b.name=bn
        assert f.finishEdit()
        pi=c.constructionPlanes.createInput();pi.setByOffset(c.xYConstructionPlane,adsk.core.ValueInput.createByString('16 mm'));pl=c.constructionPlanes.add(pi);pl.isLightBulbOn=False
        sk=c.sketches.add(pl);sk.name='RevD_final_'+label+'_axis';line=sk.sketchCurves.sketchLines.addByTwoPoints(P(x,-1,0),P(x,1,0));line.isConstruction=True;line.isFixed=True;sk.isVisible=False
        oc=adsk.core.ObjectCollection.create()
        for b in c.bRepBodies:oc.add(b.createForAssemblyContext(o))
        mi=d.rootComponent.features.moveFeatures.createInput2(oc);assert mi.defineAsRotate(line.createForAssemblyContext(o),adsk.core.ValueInput.createByString(('-' if direction<0 else '')+'probe_'+label+'_angle'));d.rootComponent.features.moveFeatures.add(mi).name='RevD_'+label+'_angle_driven_rotation'
    def move(pre,t):
        oc=adsk.core.ObjectCollection.create()
        for b in occ(pre).bRepBodies:oc.add(b)
        mi=d.rootComponent.features.moveFeatures.createInput2(oc);mi.defineAsFreeMove(t);d.rootComponent.features.moveFeatures.add(mi).name='RevD_clearance_'+pre
    t=adsk.core.Matrix3D.create();t.translation=V(-.35,0,.1);move('BATTERY',t)
    t=adsk.core.Matrix3D.create();t.setWithArray([0,-1,0,15.394,1,0,0,-15.213,0,0,1,0,0,0,0,1]);move('ESP32',t);move('PRINT_18',t)
    t=adsk.core.Matrix3D.create();t.translation=V(2,-1.5,0);move('SERVO_',t)
    # Bent M2 pushrod retains the original transom boot and tiller line. This is
    # a nominal bend envelope, requiring fabrication/steering travel validation.
    co=occ('PROCURE_Servo_horn');c=co.component
    for b in list(co.bRepBodies):
        if b.name.startswith(('Custom_horn','Horn_link')):
            oc=adsk.core.ObjectCollection.create();oc.add(b);mi=d.rootComponent.features.moveFeatures.createInput2(oc);mi.defineAsFreeMove(t);d.rootComponent.features.moveFeatures.add(mi).name='RevD_steering_horn_relocation'
    rod=next(b for b in co.bRepBodies if 'pushrod' in b.name)
    d.rootComponent.features.removeFeatures.add(rod).name='RevD_retire_straight_pushrod'
    rod=union(cy((167,-36,60),(185,-21,60),2),cy((185,-21,60),(278,-21,60),2))
    union(rod,m.createSphere(P(185,-21,60),.1))
    oo=d.rootComponent.occurrences.addNewComponent(adsk.core.Matrix3D.create());oo.component.name='PROCURE_Steering_dogleg_pushrod_ALLOCATION';f=oo.component.features.baseFeatures.add();f.startEdit();oo.component.bRepBodies.add(rod,f).name='M2_dogleg_bend_VERIFY';f.finishEdit()
    assert d.computeAll()
    result={'revision':'Rev-D','timeline':d.timeline.count,'stations':ns['STATIONS'],'changes':['Opposed arm stations separated from other shaft cartridges','Cartridge, belt flange and shaft access pockets','Fore-aft battery/transom and stern-tube rail relief','Rotated overhead controller; lower hatch boss clearance','Relocated steering servo with provisional dogleg pushrod','Four potted lead roof entries'],'assembly_release_passed':False}
    open(os.path.join(BASE,'verification','RevD_Refinement.json'),'w').write(json.dumps(result,indent=2));print('Refinement saved')
