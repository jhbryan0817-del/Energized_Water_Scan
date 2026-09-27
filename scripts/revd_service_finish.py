"""Complete battery-only lift-out, upper bridge fastener access and rear drive lanes."""
import adsk.core,adsk.fusion,os,json
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def run(_context: str):
    a=adsk.core.Application.get();d=adsk.fusion.Design.cast(a.activeProduct);r=d.rootComponent;assert d.timeline.count==1700
    m=adsk.fusion.TemporaryBRepManager.get();P=lambda x,y,z:adsk.core.Point3D.create(x/10,y/10,z/10);V=adsk.core.Vector3D.create
    def box(x0,y0,z0,x1,y1,z1):return m.createBox(adsk.core.OrientedBoundingBox3D.create(P((x0+x1)/2,(y0+y1)/2,(z0+z1)/2),V(1,0,0),V(0,1,0),(x1-x0)/10,(y1-y0)/10,(z1-z0)/10))
    def cy(p,q,di):return m.createCylinderOrCone(P(*p),di/20,P(*q),di/20)
    def op(b,t,k):assert m.booleanOperation(b,t,k);return b
    def cut(b,t):return op(b,t,adsk.fusion.BooleanTypes.DifferenceBooleanType)
    def union(b,t):return op(b,t,adsk.fusion.BooleanTypes.UnionBooleanType)
    def shift(b,x=0,y=0,z=0):
        t=adsk.core.Matrix3D.create();t.translation=V(x/10,y/10,z/10);assert m.transform(b,t);return b
    def occ(pre):return next(o for o in r.allOccurrences if o.name.startswith(pre))
    def replace(pre,bodies):
        f=occ(pre).component.features.baseFeatures.item(0);f.startEdit()
        for old,(name,new) in zip(list(f.bodies),bodies):assert new.lumps.count==1,(pre,name,new.lumps.count);assert f.updateBody(old,new);old.name=name
        f.finishEdit()
    hull=m.copy(occ('PRINT_01').bRepBodies.item(0))
    cut(hull,box(185,-21,23,193,21,68.1))
    upper=m.copy(occ('PRINT_31').bRepBodies.item(0))
    for y in [-35,35]:
        cut(hull,cy((142,y,3),(142,y,41.1),8.01))
        union(hull,cut(cy((154,y,3),(154,y,41),8),cy((154,y,33),(154,y,41.1),2.5)))
        cut(upper,cy((154,y,40.9),(154,y,44.1),3.4))
    cut(upper,box(164,-40.1,40.9,170,-32,56))
    for label,s in [('E2',-1),('E4',1)]:
        x=110
        def B(x0,y0,z0,x1,y1,z1):return box(x+x0,min(s*y0,s*y1),z0,x+x1,max(s*y0,s*y1),z1)
        def C(y0,y1,di,xx=0,zz=44):return cy((x+xx,s*y0,zz),(x+xx,s*y1,zz),di)
        # Shift both belt planes 3 mm outboard, and the servo 5 mm. This keeps
        # shafts/journals outside the battery's +/-17.25 mm vertical lift lane.
        for pre,dy in [('PROCURE_'+label+'_timing',3),('PROCURE_'+label+'_upper_journal',3),('PROCURE_'+label+'_HS65',5),('INTERFACE_HOLD_'+label+'_stock',5)]:
            oo=occ(pre);bs=[(b.name,shift(m.copy(b),0,s*dy,0)) for b in oo.bRepBodies];replace(pre,bs)
        # Retain the lower bushing seat, trimming only the redundant cartridge nose
        # inboard of the bushing's Y=32.75 datum. New minimum nose is Y=32.7.
        oo=occ('MACHINE_'+label);b=m.copy(oo.bRepBodies.item(0));cut(b,B(-20,30.9,2,20,32.7,30));replace('MACHINE_'+label,[(oo.bRepBodies.item(0).name,b)])
        union(hull,B(-19.5,59,29,28,67,55));cut(hull,B(-16.5,23,32,25,64,55.1))
        for xa,xb,hx in [(-19.5,-6.3,-8.6),(18.3,28,20)]:
            cut(hull,B(xa,41.9,35.9,xb,49.1,52.1))
            union(hull,B(xa,47,36,xb,54,52));cut(hull,C(46.9,54.1,1.7,hx))
        # Add the bearing seat to the inner wall, clear the shifted flange/belt.
        union(hull,cut(C(18.5,24.5,12),C(18.4,24.6,8.2)))
        for z in [16,44]:cut(hull,C(24.3,32.7,16.4,0,z))
        cut(hull,B(-7.7,25.3,16,7.7,31.7,44));cut(hull,C(18.4,24.6,8.2))
        cut(hull,C(24.4,56.5,6.4,0,16))
        lid=B(-19.5,20,55,28,67,58)
        for hx,hy in [(-14.5,25),(23,25),(-14.5,62),(23,62)]:
            union(hull,cut(cy((x+hx,s*hy,48),(x+hx,s*hy,55),7),cy((x+hx,s*hy,48),(x+hx,s*hy,55.1),2.5)))
            cut(lid,cy((x+hx,s*hy,54.9),(x+hx,s*hy,58.1),3.4))
        cut(hull,B(-8,20,49,8,24,55.1))
        replace('PRINT_'+('23' if label=='E2' else '25'),[('Top_access_cover_wide_drive_bay',lid)])
    replace('PRINT_01',[('Hull_four_internal_wells_and_recessed_channels',hull)])
    replace('PRINT_31',[('Controller_bridge_with_driver_and_linkage_clearance',upper)])
    assert d.computeAll()
    open(os.path.join(BASE,'verification','RevD_Service_Finish.json'),'w').write(json.dumps({'revision':'Rev-D','timeline':d.timeline.count,'upper_bridge_screws_mm':[[x,y] for x in [154,184] for y in [-35,35]],'battery_removal':'Remove upper bridge, unstrap battery and lift battery alone. Cradle remains installed.','rear_upper_journal_min_abs_y_mm':18.5,'rear_servo_shift_outboard_mm':5,'rear_belt_shift_outboard_mm':3,'cartridge_nose_trim_mm':1.7,'assembly_release_passed':False},indent=2));print('Service refinements saved')
