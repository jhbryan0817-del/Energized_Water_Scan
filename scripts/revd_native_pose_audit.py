"""Exercise real Fusion angle parameters and verify resulting electrode positions."""
import adsk.core,adsk.fusion,json,os,math
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def run(_context: str):
    a=adsk.core.Application.get();d=adsk.fusion.Design.cast(a.activeProduct);rows=[]
    stations=[('E1',-81,-1,72,1),('E2',110,-1,52,-1),('E3',-81,1,72,1),('E4',110,1,52,-1)]
    try:
        for angles in [[0]*4,[30]*4,[90]*4,[60,20,20,45]]:
            for i,deg in enumerate(angles,1):d.userParameters.itemByName('probe_E'+str(i)+'_angle').expression=str(deg)+' deg'
            assert d.computeAll();adsk.doEvents()
            for (label,x,s,lane,direction),deg in zip(stations,angles):
                o=next(o for o in d.rootComponent.allOccurrences if o.name.startswith('PROBE_'+label))
                tip=next(b for b in o.bRepBodies if b.name.startswith('ELECTRODE_'))
                head=max([f for f in tip.faces if isinstance(f.geometry,adsk.core.Plane) and abs(f.geometry.normal.y)>.99],key=lambda f:abs(f.centroid.y))
                actual=[v*10 for v in head.centroid.asArray()];actual[1]-=s*1.3
                rad=math.radians(deg);expected=[x+direction*166*math.cos(rad),s*(lane+5.3),16-166*math.sin(rad)]
                rows.append(dict(pose=angles,probe=label,actual_mm=actual,expected_mm=expected,error_mm=math.dist(actual,expected)))
    finally:
        for i in range(1,5):d.userParameters.itemByName('probe_E'+str(i)+'_angle').expression='0 deg'
        d.computeAll()
    result={'revision':'Rev-D','timeline':d.timeline.count,'checks':rows,'passed':all(r['error_mm']<1e-5 for r in rows)}
    open(os.path.join(BASE,'verification','RevD_Native_Pose_Audit.json'),'w').write(json.dumps(result,indent=2))
    assert result['passed'],[(r['probe'],r['pose'],r['error_mm']) for r in rows if r['error_mm']>=1e-5]
    print('Native angle parameters passed all 16 electrode-position checks')
