"""One-time 1523-item Rev-C.1 -> Rev-D packaging migration in Fusion.
Millimetres. Preserves the 320 x 170 hull, drive train and purchased servos.
Timing-drive solids are clearance allocations, not released tooth/horn geometry.
"""
import adsk.core, adsk.fusion, math, os, json
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIONS=[('E1',-70,-1,72,1),('E2',85,-1,52,-1),('E3',-70,1,72,1),('E4',85,1,52,-1)]
R=166.; H=16.
def run(_context: str):
    app=adsk.core.Application.get();d=adsk.fusion.Design.cast(app.activeProduct);root=d.rootComponent
    assert app.activeDocument.name=='Energized_Water_Scanner' and d.timeline.count==1523
    assert d.exportManager.execute(d.exportManager.createFusionArchiveExportOptions(os.path.join(os.path.dirname(BASE),'RevC1_before_RevD.f3d')))
    m=adsk.fusion.TemporaryBRepManager.get();P=lambda x,y,z:adsk.core.Point3D.create(x/10,y/10,z/10);V=adsk.core.Vector3D.create
    def box(x0,y0,z0,x1,y1,z1):return m.createBox(adsk.core.OrientedBoundingBox3D.create(P((x0+x1)/2,(y0+y1)/2,(z0+z1)/2),V(1,0,0),V(0,1,0),(x1-x0)/10,(y1-y0)/10,(z1-z0)/10))
    def cyl(a,b,diam):return m.createCylinderOrCone(P(*a),diam/20,P(*b),diam/20)
    def op(a,b,k):assert m.booleanOperation(a,b,k);return a
    def union(a,b):return op(a,b,adsk.fusion.BooleanTypes.UnionBooleanType)
    def cut(a,b):return op(a,b,adsk.fusion.BooleanTypes.DifferenceBooleanType)
    def inter(a,b):return op(a,b,adsk.fusion.BooleanTypes.IntersectionBooleanType)
    def transform(b,dx=0,dy=0,dz=0):
        t=adsk.core.Matrix3D.create();t.translation=V(dx/10,dy/10,dz/10);assert m.transform(b,t);return b
    def occ(prefix):return next(o for o in root.allOccurrences if o.name.startswith(prefix))
    def copy(prefix):return m.copy(occ(prefix).bRepBodies.item(0))
    oldtray=copy('PRINT_03');oldhull=copy('PRINT_01')
    # Preserve the existing stern tube sleeve and transom interfaces. Remove only
    # the four external pod lands, and close their obsolete wiring/pilot holes.
    hull=m.copy(oldhull)
    for xx in [-75,90]:
        for s in [-1,1]:
            cut(hull,box(xx-36,min(s*12,s*66),-4,xx+22,max(s*12,s*66),0))
            union(hull,box(xx-17,min(s*24,s*46),0,xx+5,max(s*24,s*46),3))
            for hx,hy in [(xx-31,s*19),(xx+17,s*19),(xx-31,s*59),(xx+17,s*59)]:
                union(hull,cyl((hx,hy,0),(hx,hy,3),2.6))
    # Old tray pillars are trimmed; motor feet remain at their original datums.
    for xx in [-70,140]:
        for yy in [-55,55]:cut(hull,box(xx-6,yy-6,3,xx+6,yy+6,20))
    parts=[];moving=[];retired=[]
    def add(name,bs):parts.append((name,bs))
    # Four long recesses with a 3 mm roof; hinge pocket has a locally higher roof.
    for index,(label,x,s,lane,direction) in enumerate(STATIONS):
        yshift=lane-77
        def local(b):
            t=adsk.core.Matrix3D.create();t.setWithArray([1,0,0,x/10,0,s,0,0,0,0,1,0,0,0,0,1]);assert m.transform(b,t);return b
        def B(x0,y0,z0,x1,y1,z1):return local(box(x0,y0,z0,x1,y1,z1))
        def C(a,b,diam):return local(cyl(a,b,diam))
        def cy(y0,y1,diam,xx=0,zz=H):return C((xx,y0,zz),(xx,y1,zz),diam)
        lo=min(0,direction*R)-7;hi=max(0,direction*R)+7
        gy0=lane-10;gy1=lane+7.6
        union(hull,B(lo-3,gy0-3,0,hi+3,gy1+3,27))
        union(hull,B(-16,gy0-3,0,16,gy1+3,32))
        cut(hull,B(lo,gy0,-1,hi,gy1,24))
        cut(hull,cy(gy0,gy1,26))
        front=direction==1
        # Front wells are full-height; rear wells step over the inner wet channel.
        if front:
            shell=B(-28,12,0,22,59,55)
            cut(shell,B(-25,15,3,19,56,56))
            seat=59;rail=[(-25,-18.3,-20),(6.3,22,8.6)]
            for xa,xb,hx in rail:
                union(shell,B(xa,25,36,xb,32,52));cut(shell,cy(25,32.1,1.7,hx,44))
            pulley_y=44.5;upper_bearing=(52,58)
            servo_dx=0;servo_dy=-5;servo_flip=False
            lid=B(-28,12,55,22,59,58)
            lidholes=[(-23,17),(17,17),(-23,54),(17,54)]
        else:
            shell=union(B(-19.5,20,0,28,39,32),B(-19.5,20,29,28,62,55))
            cut(shell,B(-16.5,23,3,25,36,56));cut(shell,B(-16.5,23,32,25,59,56))
            seat=39
            for xa,xb,hx in [(-19.5,-6.3,-8.6),(18.3,28,20)]:
                union(shell,B(xa,42,36,xb,49,52));cut(shell,cy(41.9,49.1,1.7,hx,44))
            pulley_y=22.5;upper_bearing=(16,22)
            servo_dx=0;servo_dy=79;servo_flip=True
            lid=B(-19.5,20,55,28,62,58)
            lidholes=[(-14.5,25),(23,25),(-14.5,57),(23,57)]
        # Service cartridge is unchanged nominal supplier geometry, relocated.
        cut(shell,cy(seat-8,seat+1,22.2))
        for hx in [-14,14]:
            for zz in [8,24]:cut(shell,cy(seat-7,seat+.1,2.5,hx,zz))
        # Upper idler journal takes belt radial load; stock horn adapter remains a hold.
        cut(shell,cy(upper_bearing[0]-.1,upper_bearing[1]+.1,8.2,0,44))
        for hx,hy in lidholes:
            union(shell,cut(C((hx,hy,48),(hx,hy,55),7),C((hx,hy,48),(hx,hy,55.1),2.5)))
            cut(lid,C((hx,hy,54.9),(hx,hy,58.1),3.4))
        # Small open internal dry harness exit; no new penetration into water.
        cut(shell,B(-8,20 if not front else 12,49,8,24 if not front else 16,55.1))
        union(hull,shell)
        # Re-cut wet channels after joining the well and cartridge landing block.
        cut(hull,B(lo,gy0,-1,hi,gy1,24));cut(hull,cy(gy0,gy1,26))
        cut(hull,cy(seat-8,seat+1,22.2))
        add('PRINT_'+str(22+index)+'_'+label+'_internal_servo_cover',[('Top_access_cover',lid)])
        # Reuse the documented seal/cartridge/gasket/servo envelopes by rigid transform.
        oldx=-75 if label in ['E1','E3'] else 90
        for prefix in ['MACHINE_'+label,'SEAL_'+label+'_cartridge','PROCURE_'+label+'_SKF']:
            oo=occ(prefix);bs=[]
            for b in oo.bRepBodies:bs.append((b.name,transform(m.copy(b),x-oldx,s*yshift,34)))
            add(oo.component.name,bs)
        # Case and lugs are copied in local positive-Y coordinates, then oriented.
        oo=occ('PROCURE_'+label+'_HS65HB');bs=[]
        for b in oo.bRepBodies:
            q=m.copy(b);t=adsk.core.Matrix3D.create()
            if front:t.translation=V((x-oldx)/10,s*yshift/10,62/10)
            else:t.setWithArray([-1,0,0,(x+oldx)/10,0,-1,0,s*79/10,0,0,1,62/10,0,0,0,1])
            assert m.transform(q,t);bs.append((b.name,q))
        add(oo.component.name,bs)
        # Lower pulley shaft, retained wet arm and tip; longer insulating arm.
        shaft=cy(pulley_y-1,lane+4.5,6)
        cut(shaft,C((-3.1,lane,H),(3.1,lane,H),2))
        arm=union(cy(lane-4,lane+4,24),B(min(0,direction*R),lane-4,H-4,max(0,direction*R),lane+4,H+4))
        union(arm,cy(lane-9,lane+4,12,direction*R))
        cut(arm,cy(lane-4.1,lane+4.1,6.2));cut(arm,C((-12.1,lane,H),(12.1,lane,H),2.2))
        a0,a1=sorted([direction*15,direction*(R+1)])
        cut(arm,B(a0,lane-4.1,H-1.5,a1,lane-1.5,H+1.5))
        cut(arm,cy(lane-9.1,lane+4.1,4.5,direction*R));cut(arm,cy(lane-9.1,lane-2.5,9,direction*R))
        pin=C((-11,lane,H),(11,lane,H),2)
        electrode=union(cy(lane-8,lane+4,4,direction*R),cy(lane+4,lane+6.6,7,direction*R))
        moving.append((label,x,s,lane,direction,[('PRINT_'+str(26+index)+'_'+label+'_insulated_arm',arm),('SHAFT_316_D6_extended',shaft),('PIN_316_D2_L22',pin),('ELECTRODE_'+label+'_M4x12_A4_tip',electrode)]))
        # Toothless pitch/clearance allocations: supplier geometry must replace them.
        pulleys=[]
        for zz in [H,44]:
            p=cut(cy(pulley_y,pulley_y+6,12.22,0,zz),cy(pulley_y-.1,pulley_y+6.1,6.2,0,zz))
            for yy in [pulley_y-1,pulley_y+6]:union(p,cut(cy(yy,yy+1,16,0,zz),cy(yy-.1,yy+1.1,6.2,0,zz)))
            pulleys.append(('20T_2mm_pulley_ALLOCATION_'+str(zz),p))
        belt=union(cy(pulley_y,pulley_y+6,14.8,0,H),cy(pulley_y,pulley_y+6,14.8,0,44))
        union(belt,B(-7.4,pulley_y,H,7.4,pulley_y+6,44))
        cut(belt,cy(pulley_y-.1,pulley_y+6.1,12.3,0,H));cut(belt,cy(pulley_y-.1,pulley_y+6.1,12.3,0,44))
        cut(belt,B(-6.15,pulley_y-.1,H,6.15,pulley_y+6.1,44))
        add('PROCURE_'+label+'_timing_drive_ALLOCATION',pulleys+[('96mm_pitch_6mm_belt_ALLOCATION',belt)])
        j0,j1=upper_bearing
        bush=cut(cy(j0,j1,8,0,44),cy(j0-.1,j1+.1,6.02,0,44))
        upper=cy(min(j0,pulley_y-1),max(j1,pulley_y+7),6,0,44)
        add('PROCURE_'+label+'_upper_journal_ALLOCATION',[('D8_D6_L6_bush',bush),('D6_upper_journal_shaft',upper)])
        adapter=cy(41 if front else 28.5,44.4 if front else 33,14,0,44)
        cut(adapter,cy(40 if front else 28,45 if front else 34,6.2,0,44))
        add('INTERFACE_HOLD_'+label+'_stock_horn_pulley_adapter',[('Survey_stock_horn_and_retention',adapter)])
    # Electronics cassette: low central battery, upper removable controller bridge,
    # separate port analog and starboard power shelves, steering at original height.
    tray=box(-34,-62,32,63,62,35);cut(tray,box(5,-24,31,64,24,36))
    def traypiece(bounds,shift):return transform(inter(m.copy(oldtray),box(*bounds)),*shift)
    union(tray,traypiece((-28,-59,19,28,-27,24),(0,0,16)))
    union(tray,traypiece((33,-55,19,63,-34,24),(0,0,16)))
    union(tray,traypiece((84,28,19,134,56,24),(-112,0,16)))
    union(tray,traypiece((59,25,19,75,60,24),(-24,0,16)))
    for xx,yy in [(-22.8,-12.8),(-9.3,3.2)]:
        union(tray,cyl((xx,yy,35),(xx,yy,40),4));cut(tray,cyl((xx,yy,36),(xx,yy,40.1),1.7))
    for xx in [-30,59]:
        for yy in [-58.5,58.5]:
            cut(tray,cyl((xx,yy,31.9),(xx,yy,35.1),3.4))
            union(hull,cut(cyl((xx,yy,3),(xx,yy,32),8),cyl((xx,yy,24),(xx,yy,32.1),2.5)))
    # Separate aft steering saddle avoids disturbing rudder linkage geometry.
    saddle=inter(m.copy(oldtray),box(120,-61,16,161,-25,44))
    for xx in [123,158]:
        for yy in [-57,-28]:
            union(saddle,box(xx-3,yy-3,16,xx+3,yy+3,19))
            cut(saddle,cyl((xx,yy,15.9),(xx,yy,19.1),3.4))
            union(hull,cut(cyl((xx,yy,3),(xx,yy,16),7),cyl((xx,yy,8),(xx,yy,16.1),2.5)))
    add('PRINT_03_Removable_electronics_tray',[('Analog_and_power_service_cassette',tray)])
    add('PRINT_30_Steering_service_saddle',[('Original_steering_datums',saddle)])
    battery=box(88,-20,24,196,20,26)
    for yy in [-19.25,18]:union(battery,box(88,yy,26,196,yy+1.25,30))
    for xx in [103,179]:
        for yy in [-17,15.5]:cut(battery,box(xx,yy,23.9,xx+10,yy+1.5,26.1))
    # Three bottom support rails; removable cradle retained by two straps.
    for xx in [91,140,193]:union(hull,box(xx-2,-19,3,xx+2,19,24))
    add('PRINT_04_Longitudinal_battery_cradle',[('Two_strap_battery_cradle',battery)])
    upper=box(118,-30,44,192,30,47)
    union(upper,traypiece((-28,27,19,42,61,25),(148,-44,28)))
    for xx in [121,189]:
        for yy in [-26,26]:
            cut(upper,cyl((xx,yy,43.9),(xx,yy,47.1),3.4))
            union(hull,cut(cyl((xx,yy,3),(xx,yy,44),8),cyl((xx,yy,36),(xx,yy,44.1),2.5)))
    # Header access, strap access and ties on the removable bridge.
    for xx in [123,181]:
        for yy in [-22,20]:cut(upper,box(xx,yy,43.9,xx+7,yy+2,47.1))
    add('PRINT_31_Upper_controller_bridge',[('Battery_overhead_controller_deck',upper)])
    # Persist a new hull as one native base feature, retaining old history removed.
    assert hull.isSolid and hull.lumps.count==1,('hull',hull.lumps.count)
    add('PRINT_01_Hull_shell',[('Hull_four_internal_wells_and_recessed_channels',hull)])
    for name,bs in parts:
        for bn,b in bs:assert b and b.isSolid and b.lumps.count==1,(name,bn,b.lumps.count if b else None)
    # Prepared geometry is complete before touching the model structure.
    remove_prefix=['PRINT_01','PRINT_03','PRINT_04','PROBE_']
    for label,_,_,_,_ in STATIONS:remove_prefix += ['MACHINE_'+label,'SEAL_'+label,'PROCURE_'+label,'INTERFACE_HOLD_'+label]
    remove_prefix += ['PRINT_22','PRINT_23','PRINT_24','PRINT_25']
    for o in list(root.occurrences):
        if o.name.startswith(tuple(remove_prefix)):
            retired.append(o.name);root.features.removeFeatures.add(o).name='RevD_retire_'+o.component.name
    def addcomp(name,bs):
        oo=root.occurrences.addNewComponent(adsk.core.Matrix3D.create());c=oo.component;c.name=name
        f=c.features.baseFeatures.add();f.name='RevD_'+name;assert f.startEdit()
        for bn,b in bs:c.bRepBodies.add(b,f).name=bn
        assert f.finishEdit();return oo
    for name,bs in parts:addcomp(name,bs)
    for label,x,s,lane,direction,bs in moving:
        oo=addcomp('PROBE_'+label+'_MOVING',bs);c=oo.component
        pi=c.constructionPlanes.createInput();pi.setByOffset(c.xYConstructionPlane,adsk.core.ValueInput.createByString('16 mm'));pl=c.constructionPlanes.add(pi);pl.isLightBulbOn=False
        sk=c.sketches.add(pl);sk.name='RevD_'+label+'_hinge_axis';axis=sk.sketchCurves.sketchLines.addByTwoPoints(P(x,-1,0),P(x,1,0));axis.isConstruction=True;axis.isFixed=True;sk.isVisible=False
        oc=adsk.core.ObjectCollection.create()
        for b in c.bRepBodies:oc.add(b.createForAssemblyContext(oo))
        mi=root.features.moveFeatures.createInput2(oc);mi.defineAsRotate(axis.createForAssemblyContext(oo),adsk.core.ValueInput.createByString(('-' if direction<0 else '')+'probe_'+label+'_angle'))
        root.features.moveFeatures.add(mi).name='RevD_'+label+'_angle_driven_rotation'
    def move(prefix,dx,dy,dz,rotate=False):
        oo=occ(prefix);oc=adsk.core.ObjectCollection.create()
        for b in oo.bRepBodies:oc.add(b)
        t=adsk.core.Matrix3D.create()
        if rotate:
            # Battery 104 mm dimension changes from transverse Y to longitudinal X.
            t.setWithArray([0,1,0,14.2,-1,0,0,-5.25,0,0,1,.5,0,0,0,1])
        else:t.translation=V(dx/10,dy/10,dz/10)
        mi=root.features.moveFeatures.createInput2(oc);mi.defineAsFreeMove(t);root.features.moveFeatures.add(mi).name='RevD_repackage_'+prefix
    move('BATTERY_',0,0,0,True)
    for prefix,delta in [('ESP32_',(148,-44,28)),('PRINT_18',(148,-44,28)),('FRONT_END_',(0,0,16)),('PRINT_19',(0,0,16)),('ADS1115_',(0,0,16)),('ESC_',(-112,0,16)),('PROCURE_ESC',(-112,0,16)),('PRINT_21',(-112,0,16)),('D24V10F5_OFFICIAL_D24',( -24,0,16)),('PRINT_20',(-24,0,16)),('PROCURE_D24V50',(-104,40,16))]:move(prefix,*delta)
    d.userParameters.itemByName('probe_hinge_drop').expression='-16 mm'
    d.userParameters.itemByName('probe_tip_radius').expression='166 mm'
    for label,_,_,_,_ in STATIONS:d.userParameters.itemByName('probe_'+label+'_angle').expression='0 deg'
    for n,e,u in [('revd_belt_centres','28 mm','mm'),('revd_belt_pitch_length','96 mm','mm'),('revd_hinge_above_bottom','16 mm','mm')]:d.userParameters.add(n,adsk.core.ValueInput.createByString(e),u,'Reference only; migration geometry, not a regenerating master dimension')
    assert d.computeAll()
    for o in root.allOccurrences:o.isLightBulbOn=not o.name.startswith(('DATUM','REFERENCE','OPTION','CLEARANCES','INTERFACE_HOLD'))
    occ('PRINT_02').isLightBulbOn=False
    out={'revision':'Rev-D','timeline':d.timeline.count,'hull_footprint_mm':[320,170],'hinge_height_mm':16,'radius_mm':166,'deployed_tip_depth_mm':150,'stations':STATIONS,'retired':retired,'assembly_release_passed':False}
    with open(os.path.join(BASE,'verification','RevD_Migration.json'),'w') as f:json.dump(out,f,indent=2)
    print(json.dumps(out))
