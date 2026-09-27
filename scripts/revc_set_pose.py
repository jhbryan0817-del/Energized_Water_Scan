"""Set POSE to stowed, deployed, measurement, or a four-angle list before running.
Native Fusion user parameters drive arm geometry; no rebuild or occurrence drag.
"""
import adsk.core, adsk.fusion, math
POSE='measurement'
def run(_context: str):
    presets={'stowed':[0,0,0,0],'deployed':[90,90,90,90],'measurement':[90,30,30,90]}
    angles=presets[POSE] if isinstance(POSE,str) else POSE
    assert len(angles)==4 and all(math.isfinite(v) and 0<=v<=90 for v in angles),'Four angles in0..90 required'
    d=adsk.fusion.Design.cast(adsk.core.Application.get().activeProduct)
    for i,v in enumerate(angles,1):d.userParameters.itemByName('probe_E'+str(i)+'_angle').expression=str(v)+' deg'
    assert d.computeAll();print('Probe angles:',angles)
