"""Read-only rigid service access and wiring corridor audit, not harness qualification."""
import adsk.core,adsk.fusion,json,os
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def run(_context: str):
    a=adsk.core.Application.get();d=adsk.fusion.Design.cast(a.activeProduct);m=adsk.fusion.TemporaryBRepManager.get()
    P=lambda q:adsk.core.Point3D.create(*[v/10 for v in q]);V=adsk.core.Vector3D.create
    solids=[(o.name,b) for o in d.rootComponent.allOccurrences if not o.name.startswith(('DATUM','REFERENCE','OPTION','CLEARANCES','INTERFACE_HOLD')) for b in o.bRepBodies if b.isSolid]
    hits=[];fail=[];tests=[]
    def cylinder(p,q,diam):return m.createCylinderOrCone(P(p),diam/20,P(q),diam/20)
    def test(name,t,exclude):
        tests.append(name)
        for n,b in solids:
            if n.startswith(tuple(exclude)) or not t.boundingBox.intersects(b.boundingBox):continue
            q=m.copy(t)
            if not m.booleanOperation(q,m.copy(b),adsk.fusion.BooleanTypes.IntersectionBooleanType):fail.append([name,n]);continue
            if q.volume*1000>.001:hits.append(dict(test=name,obstacle=n+'/'+b.name,mm3=q.volume*1000))
    for x in [-30,59]:
        for y in [-58.5,58.5]:test('main tray screw '+str((x,y)),cylinder((x,y,35.1),(x,y,100),6),['PRINT_02'])
    for x in [154,184]:
        for y in [-35,35]:test('controller bridge screw '+str((x,y)),cylinder((x,y,44.1),(x,y,100),6),['PRINT_02'])
    for s in [-1,1]:
        for x,y in [(-104,s*17),(-64,s*17),(-104,s*54),(-64,s*54)]:
            test('forward cover angled tool '+str((x,y)),cylinder((x,y,61.1),(x+14,y,100),6),['PRINT_02'])
    # Remove hatch, controller bridge and its controller/capture bridge first.
    for prefixes,exclude,label in [
        (('PRINT_31','ESP32','PRINT_18'),['PRINT_02','PRINT_31','ESP32','PRINT_18'],'controller bridge'),
        (('BATTERY',),['PRINT_02','PRINT_31','ESP32','PRINT_18','BATTERY'],'battery alone'),
        (('PRINT_03','FRONT_END','ADS1115','ESC_','PROCURE_ESC','PRINT_19','PRINT_20','PRINT_21','D24V10F5','PROCURE_D24V50'),['PRINT_02','PRINT_03','FRONT_END','ADS1115','ESC_','PROCURE_ESC','PRINT_19','PRINT_20','PRINT_21','D24V10F5','PROCURE_D24V50'],'main cassette')]:
        for dz in range(0,81,10):
            t=adsk.core.Matrix3D.create();t.translation=V(0,0,dz/10)
            for n,b in solids:
                if n.startswith(prefixes):
                    q=m.copy(b);assert m.transform(q,t);test(label+' lift '+str(dz)+' '+n+'/'+b.name,q,exclude)
    # Dry bundle centerline allocations above the roofs and outside the shelves.
    routes={'port_analog':[(-40,-66,33),(55,-66,33),(55,-66,45)],'starboard_power':[(-40,70,33),(116,70,33),(116,70,48)]}
    for label,pts in routes.items():
        for i,(p,q) in enumerate(zip(pts,pts[1:])):test(label+str(i),cylinder(p,q,4),['PRINT_02'])
    out={'revision':'Rev-D','timeline':d.timeline.count,'intersections':hits,'boolean_failures':fail,'tested_allocations':tests,'dry_routes_mm':routes,'assembly_release_passed':False,'limits':'Sampled 10mm rigid lift; explicit disassembly exclusions. Does not test cables, actual connectors, strap release, hand/tool ergonomics, lid flex, wet lead loop, or installed fastener tolerances.'}
    with open(os.path.join(BASE,'verification','RevD_Service_Audit.json'),'w') as f:json.dump(out,f,indent=2)
    print('Service report saved: %d intersections'%len(hits))
