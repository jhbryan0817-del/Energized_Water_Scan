"""One-time Rev-B.4 -> Rev-C.1 concept migration, executed in Fusion via MCP.
Fixed geometry is in mm. Four angle parameters drive native rotate features.
Purchased interfaces marked HOLD are allocations, never fabricated stock parts.
"""
import adsk.core, adsk.fusion, math, os, json
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run(_context: str):
    app=adsk.core.Application.get(); d=adsk.fusion.Design.cast(app.activeProduct); root=d.rootComponent
    assert app.activeDocument.name=='Energized_Water_Scanner' and d.timeline.count==1250
    assert d.exportManager.execute(d.exportManager.createFusionArchiveExportOptions(os.path.join(os.path.dirname(BASE),'RevB4_before_RevC.f3d')))
    m=adsk.fusion.TemporaryBRepManager.get(); P=lambda x,y,z:adsk.core.Point3D.create(x/10,y/10,z/10); V=adsk.core.Vector3D.create
    def box(x0,y0,z0,x1,y1,z1):
        return m.createBox(adsk.core.OrientedBoundingBox3D.create(P((x0+x1)/2,(y0+y1)/2,(z0+z1)/2),V(1,0,0),V(0,1,0),(x1-x0)/10,(y1-y0)/10,(z1-z0)/10))
    def cyl(a,b,diam):return m.createCylinderOrCone(P(*a),diam/20,P(*b),diam/20)
    def boolean(a,b,kind):
        assert m.booleanOperation(a,b,kind);return a
    def union(a,b):return boolean(a,b,adsk.fusion.BooleanTypes.UnionBooleanType)
    def cut(a,b):return boolean(a,b,adsk.fusion.BooleanTypes.DifferenceBooleanType)
    def comp(prefix):return next(o.component for o in root.allOccurrences if o.name.startswith(prefix))
    def addcomp(name, bodies):
        c=root.occurrences.addNewComponent(adsk.core.Matrix3D.create()).component;c.name=name
        f=c.features.baseFeatures.add();f.name='RevC_'+name;assert f.startEdit()
        for name,b in bodies:c.bRepBodies.add(b,f).name=name
        assert f.finishEdit();return c
    def modify(c,t,name,join=False):
        target=c.bRepBodies.item(0);f=c.features.baseFeatures.add();f.name=name+'_tool';assert f.startEdit();c.bRepBodies.add(t,f);assert f.finishEdit()
        oc=adsk.core.ObjectCollection.create();oc.add(f.bodies.item(0));i=c.features.combineFeatures.createInput(target,oc)
        i.operation=adsk.fusion.FeatureOperations.JoinFeatureOperation if join else adsk.fusion.FeatureOperations.CutFeatureOperation
        c.features.combineFeatures.add(i).name=name
    removed=[]
    for o in list(root.occurrences):
        if any(k in o.name.lower() for k in ['magnetometer','sen19921','electrode_e']):
            removed.append(o.name);root.features.removeFeatures.add(o).name='RevC_remove_'+o.component.name
    hull=comp('PRINT_01')
    # Eliminate the former wet electrode penetrations and obsolete blind bow rail pilots.
    for x,y in [(-100,0),(40,0),(-30,-55),(-30,55)]:
        modify(hull,cyl((x,y,0),(x,y,10),4.5),'RevC_close_legacy_electrode',True)
    for x in [-108,-98]:modify(hull,cyl((x,0,59),(x,0,71),2.5),'RevC_close_bow_rail_pilot',True)
    for n,e,u,desc in [('probe_hinge_drop','18 mm','mm','Reference only; fixed geometry requires migration to change'),('probe_tip_radius','132 mm','mm','Reference only; tip center radius'),('probe_deployed_depth','probe_hinge_drop + probe_tip_radius','mm','150 mm below flat hull bottom at 90 degrees')]:
        d.userParameters.add(n,adsk.core.ValueInput.createByString(e),u,desc)
    stations=[('E1',-75,-1,90),('E2',90,-1,30),('E3',-75,1,30),('E4',90,1,90)]
    for idx,(label,x,s,angle) in enumerate(stations):
        # Generate in local x and positive transverse y, mirror y for the port modules.
        def tr(b):
            t=adsk.core.Matrix3D.create();t.setWithArray([1,0,0,x/10,0,s,0,0,0,0,1,0,0,0,0,1]);assert m.transform(b,t);return b
        def B(*v):return tr(box(*v))
        def C(a,b,diam):return tr(cyl(a,b,diam))
        def cy(y0,y1,diam,xx=0,zz=-18):return C((xx,y0,zz),(xx,y1,zz),diam)
        # Flat hull land and 20x20 dry wiring aperture; underside blind fastening bosses.
        pad=B(-35,13,-3,21,65,3)
        modify(hull,pad,'RevC_'+label+'_gasket_land',True)
        modify(hull,B(-16,25,-3.1,4,45,11),'RevC_'+label+'_dry_wire_aperture')
        mounts=[(-31,19),(17,19),(-31,59),(17,59)]
        for xx,yy in mounts:
            modify(hull,C((xx,yy,-3),(xx,yy,8),8),'RevC_'+label+'_blind_boss',True)
            modify(hull,C((xx,yy,-3.1),(xx,yy,5),2.5),'RevC_'+label+'_M3_pilot')
        # Open-top dry pod, 3 mm minimum walls, 4 mm mounting flange.
        pod=union(B(-28,17,-36,14,64,-3.75),B(-35,13,-7.75,21,65,-3.75))
        cut(pod,B(-25,20,-33,11,60,-3.65))
        # Reinforced service-cartridge seat, fitted from outboard.
        union(pod,B(-19,58,-32,19,64,-4.5))
        cut(pod,cy(55,65,22.2))
        for xx in [-14,14]:
            for zz in [-26,-10]:cut(pod,cy(57,64.1,2.5,xx,zz))
        # Servo lug rails, retaining middle mounting holes from manufacturer drawing.
        for x0,x1,hx in [(-25,-18.3,-20),(6.3,14,8.6)]:
            union(pod,B(x0,30,-26,x1,37,-10))
            cut(pod,cy(30,37.1,1.7,hx,-18))
        for xx,yy in mounts:
            cut(pod,C((xx,yy,-8),(xx,yy,-3.6),3.4))
            # Compression stops are outside the continuous gasket perimeter.
            union(pod,cut(C((xx,yy,-3.75),(xx,yy,-3),6),C((xx,yy,-3.8),(xx,yy,-2.9),3.4)))
        # Separate potted electrode lead entry; cable/bond qualification is mandatory.
        union(pod,cy(57,67,10,-20,-28))
        cut(pod,cy(56.9,67.1,4,-20,-28))
        pc=addcomp('PRINT_'+str(22+idx)+'_'+label+'_dry_servo_pod',[('Pod',pod)])
        gasket=cut(B(-27,18,-3.75,13,62,-3),B(-24,21,-3.9,10,59,-2.9))
        addcomp('SEAL_'+label+'_pod_1mm_silicone_compressed_0p75',[('Continuous_face_gasket',gasket)])
        # Nominal machined POM-C seal/bearing cartridge; precision seats are not FDM.
        cartridge=union(cy(56,71.75,22),B(-18,64.75,-31,18,67.75,-5))
        cut(cartridge,cy(55.9,64.75,8));cut(cartridge,cy(62.75,64.75,12.1));cut(cartridge,cy(64.75,71.85,16))
        for xx in [-14,14]:
            for zz in [-26,-10]:cut(cartridge,cy(64.6,67.9,3.4,xx,zz))
        addcomp('MACHINE_'+label+'_POM_C_seal_cartridge',[('Machined_cartridge_nominal',cartridge)])
        cg=cut(B(-18,64,-31,18,64.75,-5),cy(63.9,64.85,22.2))
        for xx in [-14,14]:
            for zz in [-26,-10]:cut(cg,cy(63.9,64.9,3.4,xx,zz))
        addcomp('SEAL_'+label+'_cartridge_face_gasket',[('1mm_sheet_compressed_0p75',cg)])
        seal=cut(cy(64.75,71.75,16),cy(64.6,71.9,6))
        bush=union(cy(57.75,63.75,8),cy(62.75,63.75,12));cut(bush,cy(57.6,63.9,6.02))
        addcomp('PROCURE_'+label+'_SKF_6x16x7_and_igus_GFM060806',[('SKF_seal_NOMINAL_ENVELOPE',seal),('igus_flanged_bush_nominal',bush)])
        # Servo drawing: use 26 mm base-to-horn datum, not the rounded 24 mm headline.
        servo=B(-17.8,20,-23.8,5.8,46,-12.2)
        lugs=B(-21.85,37,-23.8,10.45,39,-12.2)
        cut(lugs,cy(36.9,39.1,2,-20));cut(lugs,cy(36.9,39.1,2,8.6))
        union(servo,lugs)
        addcomp('PROCURE_'+label+'_HS65HB_drawing_envelope',[('Case_and_lugs_26mm_datum',servo),('M25T_spline_envelope',cy(46,49.1,5))])
        # Coupling intentionally left as a visible hold envelope until stock horn is measured.
        coupling=cut(cy(50.5,56.5,14),cy(51,56.6,6.2))
        cc=addcomp('INTERFACE_HOLD_'+label+'_horn_to_shaft_adapter',[('Unreleased_adapter_space',coupling)])
        cc.attributes.add('RevC','Hold','Requires measured supplied M25T horn, axial retention and torque proof; not a released printable part')
        shaft=cy(51,81.5,6)
        # A cross-pin transmits torque beyond the sealing track, no flats under seal.
        cut(shaft,C((-3.1,77,-18),(3.1,77,-18),2.0))
        arm=union(cy(73,81,24),B(0,73,-22,132,81,-14))
        union(arm,cy(68,81,12,132))
        cut(arm,cy(72.9,81.1,6.2))
        cut(arm,C((-12.1,77,-18),(12.1,77,-18),2.2))
        # Recessed conductor groove on inboard face, bed and encapsulate the wire.
        cut(arm,B(15,72.9,-19.5,127,75.5,-16.5))
        cut(arm,cy(67.9,81.1,4.5,132))
        # Inner terminal potting pocket; only outer M4 head is exposed electrically.
        cut(arm,cy(67.9,74.5,9,132))
        pin=C((-11,77,-18),(11,77,-18),2)
        electrode=union(cy(69,81,4,132),cy(81,83.6,7,132))
        # Electrode fasteners/nut/lug/potting omitted from this packaging body; documented hold.
        moving=addcomp('PROBE_'+label+'_MOVING',[('PRINT_'+str(26+idx)+'_'+label+'_insulated_arm',arm),('SHAFT_316_D6_L30p5',shaft),('PIN_316_D2_L22',pin),('ELECTRODE_'+label+'_M4x12_A4_tip',electrode)])
        par=d.userParameters.add('probe_'+label+'_angle',adsk.core.ValueInput.createByString(str(angle)+' deg'),'deg','0=parallel aft, 90=down; allowed range 0..90. Use revc_set_pose.py for checked input.')
        # Fixed axis in a base feature; native rotate is driven by the named angle parameter.
        # Sketch on XY offset down 18 mm gives a stable parametric linear rotation entity.
        pi=moving.constructionPlanes.createInput();pi.setByOffset(moving.xYConstructionPlane,adsk.core.ValueInput.createByString('-18 mm'))
        plane=moving.constructionPlanes.add(pi);plane.isLightBulbOn=False
        sk=moving.sketches.add(plane);sk.name=label+'_hinge_axis_sketch'
        axis=sk.sketchCurves.sketchLines.addByTwoPoints(P(x,-1,0),P(x,1,0));axis.isConstruction=True;axis.isFixed=True
        sk.isVisible=False
        oc=adsk.core.ObjectCollection.create()
        mo=next(o for o in root.occurrences if o.component==moving)
        for b in moving.bRepBodies:oc.add(b.createForAssemblyContext(mo))
        mi=root.features.moveFeatures.createInput2(oc);assert mi.defineAsRotate(axis.createForAssemblyContext(mo),adsk.core.ValueInput.createByString(par.name))
        root.features.moveFeatures.add(mi).name='RevC_'+label+'_angle_driven_rotation'
    # The new servo power supply is separate from logic and steering BEC rails.
    tray=comp('PRINT_03');holes=[(81.2,-52.8),(94.7,-36.8)]
    for xx,yy in holes:
        modify(tray,cyl((xx,yy,19),(xx,yy,24),4),'RevC_servo_regulator_standoff',True)
        modify(tray,cyl((xx,yy,20),(xx,yy,24.1),1.7),'RevC_servo_regulator_M2_pilot')
    pcb=box(79,-55,24,96.8,-34.7,25.57)
    for xx,yy in holes:cut(pcb,cyl((xx,yy,23.9),(xx,yy,25.7),2.18))
    # Conservative upper/lower allocations spare mounting-head columns.
    top=box(79.5,-54.5,25.57,96.3,-35.2,31.67)
    for xx,yy in holes:cut(top,cyl((xx,yy,25.5),(xx,yy,31.8),5))
    addcomp('PROCURE_D24V50F5_probe_5V_supply_envelope',[('PCB_17p8x20p3',pcb),('Upper_components_6p1',top),('Lower_components_1p1',box(84,-49,22.9,92,-41,24))])
    for o in root.allOccurrences:
        if o.name.startswith(('DATUM','REFERENCE','OPTION','CLEARANCES','INTERFACE_HOLD')):o.isLightBulbOn=False
        else:o.isLightBulbOn=True
    assert d.computeAll()
    result={'revision':'Rev-C.1','baseline_timeline':1250,'timeline':d.timeline.count,'removed':removed,'stations':stations,'hinge_drop_mm':18,'tip_radius_mm':132,'assembly_release_passed':False,'status':'mechanical concept; supplier horn adapter, seal qualification and harness unfinished'}
    with open(os.path.join(BASE,'verification','RevC_Migration.json'),'w') as f:json.dump(result,f,indent=2)
    print(json.dumps(result))
