"""Read-only BRep clearance and sampled probe motion audit. Run inside Fusion.
Reports existing components and concept allocations separately; no physical release.
"""
import adsk.core, adsk.fusion, math, json, os
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def run(_context: str):
    a=adsk.core.Application.get();d=adsk.fusion.Design.cast(a.activeProduct);r=d.rootComponent;m=adsk.fusion.TemporaryBRepManager.get()
    def physical(o):return not o.name.startswith(('DATUM','REFERENCE','OPTION','CLEARANCES','INTERFACE_HOLD'))
    solids=[(o.component.name,b) for o in r.allOccurrences if physical(o) for b in o.bRepBodies if b.isSolid]
    errors=[]
    def overlap(a,b):
        if not a.boundingBox.intersects(b.boundingBox):return 0.
        c=m.copy(a)
        if not m.booleanOperation(c,m.copy(b),adsk.fusion.BooleanTypes.IntersectionBooleanType):
            errors.append([a.name,b.name]);return -1.
        return c.volume*1000
    collisions=[]
    for i,(an,ab) in enumerate(solids):
        for bn,bb in solids[i+1:]:
            if an==bn:continue
            v=overlap(ab,bb)
            if v>0.001:collisions.append({'a':an+'/'+ab.name,'b':bn+'/'+bb.name,'volume_mm3':round(v,5)})
    # Temporary transforms move every solid in one probe; actual model is unchanged.
    static=[(n,b) for n,b in solids if not n.startswith('PROBE_')]
    motion=[];endpoint=[]
    for label,x,s in [('E1',-75,-1),('E2',90,-1),('E3',-75,1),('E4',90,1)]:
        moving=[(n,b) for n,b in solids if n.startswith('PROBE_'+label)]
        current=d.userParameters.itemByName('probe_'+label+'_angle').value
        for deg in range(0,91,5):
            t=adsk.core.Matrix3D.create();t.setToRotation(math.radians(deg)-current,adsk.core.Vector3D.create(0,1,0),adsk.core.Point3D.create(x/10,s*7.7,-1.8))
            for _,b in moving:
                mb=m.copy(b);assert m.transform(mb,t)
                for sn,sb in static:
                    v=overlap(mb,sb)
                    if v>.001:motion.append(dict(probe=label,angle=deg,moving=b.name,obstacle=sn+'/'+sb.name,volume_mm3=round(v,5)))
        tip=next(b for _,b in moving if b.name.startswith('ELECTRODE_'))
        q=tip.boundingBox;center=[(v+w)*5 for v,w in zip(q.minPoint.asArray(),q.maxPoint.asArray())]
        theta=current;expected=[x+132*math.cos(theta),s*82.3,-18-132*math.sin(theta)]
        # Full electrode body spans y69..83.6, so measure head using circular planar face.
        headfaces=[f for f in tip.faces if isinstance(f.geometry,adsk.core.Plane) and abs(f.geometry.normal.y)>.99]
        head=max(headfaces,key=lambda f:abs(f.centroid.y))
        # Outer face at y83.6; analytical centroid of exposed head at82.3 is1.3inboard.
        actual=[v*10 for v in head.centroid.asArray()];actual[1]-=s*1.3
        endpoint.append(dict(probe=label,actual_tip_mm=actual,expected_tip_mm=expected,error_mm=math.dist(actual,expected)))
    issues=[dict(index=i,name=d.timeline.item(i).name,message=d.timeline.item(i).errorOrWarningMessage) for i in range(d.timeline.count) if d.timeline.item(i).healthState in [adsk.fusion.FeatureHealthStates.WarningFeatureHealthState,adsk.fusion.FeatureHealthStates.ErrorFeatureHealthState]]
    def point(p):return [round(v*10,5) for v in p.asArray()]
    inventory=[dict(component=n,body=b.name,volume_mm3=b.volume*1000,lumps=b.lumps.count,min_mm=point(b.boundingBox.minPoint),max_mm=point(b.boundingBox.maxPoint)) for n,b in solids]
    result={'revision':'Rev-C.1','timeline':d.timeline.count,'body_count':len(solids),'feature_issues':issues,'interferences':collisions,'sampled_motion_collisions':motion,'boolean_failures':errors,'tip_position_checks':endpoint,'inventory':inventory,'assembly_release_passed':False,'motion_scope':'Each arm 0..90 at5deg against static solids; separate lane-spacing proof covers other arms. Does not test cable loops, horn adapter, fasteners, seal drag, moving water or continuous swept volume.'}
    with open(os.path.join(BASE,'verification','RevC_Assembly_Audit.json'),'w') as f:json.dump(result,f,indent=2)
    print(json.dumps({k:v for k,v in result.items() if k!='inventory'}))
