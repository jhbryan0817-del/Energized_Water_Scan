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
    collisions=[];intentional=[]
    known={
      frozenset(['SERVO_TowerPro_SG90_Digital_ENVELOPE/Body','SERVO_TowerPro_SG90_Digital_ENVELOPE/Mount_lugs_VERIFY']):'Overlapping construction envelopes of one purchased servo; not separate assembled parts.',
      frozenset(['DRIVELINE_Mabuchi_and_Krick/Krick_65220_shaft_178mm','DRIVELINE_Mabuchi_and_Krick/Propeller_30mm_swept_volume']):'Shaft enters the nominal propeller swept-volume envelope; threaded hub not modeled.',
      frozenset(['PROCURE_Servo_horn_and_M2_linkage_ENVELOPES/Custom_horn_spline_fit_TBD','PROCURE_Servo_horn_and_M2_linkage_ENVELOPES/Horn_link_pin']):'Fixed horn pin embedded in its nominal horn envelope; fabrication/retention unresolved.'}
    for i,(an,ab) in enumerate(solids):
        for bn,bb in solids[i+1:]:
            if ab==bb:continue
            v=overlap(ab,bb)
            if v>0.001:
                row={'a':an+'/'+ab.name,'b':bn+'/'+bb.name,'volume_mm3':round(v,5)}
                reason=known.get(frozenset([row['a'],row['b']]))
                if reason:row['reason']=reason;intentional.append(row)
                else:collisions.append(row)
    # Temporary transforms move every solid in one probe; actual model is unchanged.
    static=[(n,b) for n,b in solids if not n.startswith('PROBE_')]
    motion=[];endpoint=[]
    for label,x,s,lane,direction in [('E1',-81,-1,72,1),('E2',110,-1,52,-1),('E3',-81,1,72,1),('E4',110,1,52,-1)]:
        moving=[(n,b) for n,b in solids if n.startswith('PROBE_'+label)]
        current=d.userParameters.itemByName('probe_'+label+'_angle').value
        for deg in range(0,91,2):
            t=adsk.core.Matrix3D.create();t.setToRotation(direction*(math.radians(deg)-current),adsk.core.Vector3D.create(0,1,0),adsk.core.Point3D.create(x/10,s*lane/10,1.6))
            for _,b in moving:
                mb=m.copy(b);assert m.transform(mb,t)
                for sn,sb in static:
                    v=overlap(mb,sb)
                    if v>.001:motion.append(dict(probe=label,angle=deg,moving=b.name,obstacle=sn+'/'+sb.name,volume_mm3=round(v,5)))
        tip=next(b for _,b in moving if b.name.startswith('ELECTRODE_'))
        q=tip.boundingBox;center=[(v+w)*5 for v,w in zip(q.minPoint.asArray(),q.maxPoint.asArray())]
        theta=current;expected=[x+direction*166*math.cos(theta),s*(lane+5.3),16-166*math.sin(theta)]
        # Full electrode body spans y69..83.6, so measure head using circular planar face.
        headfaces=[f for f in tip.faces if isinstance(f.geometry,adsk.core.Plane) and abs(f.geometry.normal.y)>.99]
        head=max(headfaces,key=lambda f:abs(f.centroid.y))
        # Outer face at y83.6; analytical centroid of exposed head at82.3 is1.3inboard.
        actual=[v*10 for v in head.centroid.asArray()];actual[1]-=s*1.3
        endpoint.append(dict(probe=label,actual_tip_mm=actual,expected_tip_mm=expected,error_mm=math.dist(actual,expected)))
    issues=[dict(index=i,name=d.timeline.item(i).name,message=d.timeline.item(i).errorOrWarningMessage) for i in range(d.timeline.count) if d.timeline.item(i).healthState in [adsk.fusion.FeatureHealthStates.WarningFeatureHealthState,adsk.fusion.FeatureHealthStates.ErrorFeatureHealthState]]
    def point(p):return [round(v*10,5) for v in p.asArray()]
    inventory=[dict(component=n,body=b.name,volume_mm3=b.volume*1000,lumps=b.lumps.count,min_mm=point(b.boundingBox.minPoint),max_mm=point(b.boundingBox.maxPoint)) for n,b in solids]
    result={'revision':'Rev-E1','timeline':d.timeline.count,'body_count':len(solids),'feature_issues':issues,'interferences':collisions,'sampled_motion_collisions':motion,'boolean_failures':errors,'tip_position_checks':endpoint,'inventory':inventory,'assembly_release_passed':False,'motion_scope':'Each arm 0..90 at2deg against static solids; separate lane-spacing proof covers other arms. Does not test cable loops, horn adapter, fasteners, seal drag, moving water or continuous swept volume.'}
    result['intentional_envelope_intersections']=intentional
    with open(os.path.join(BASE,'verification','RevE1_Assembly_Audit.json'),'w') as f:json.dump(result,f,indent=2)
    print('Audit saved; collisions=%d, motion=%d, errors=%d' % (len(collisions),len(motion),len(issues)))

