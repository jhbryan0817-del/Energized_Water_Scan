"""Neutralize superseded component-owned rotations; retain one live driver per probe."""
import adsk.core,adsk.fusion,json,os
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def run(_context: str):
    a=adsk.core.Application.get();d=adsk.fusion.Design.cast(a.activeProduct);rows=[]
    assert d.timeline.count==1700
    assert all(abs(d.userParameters.itemByName('probe_E'+str(i)+'_angle').value)<1e-10 for i in range(1,5))
    for o in d.rootComponent.allOccurrences:
        if not o.name.startswith('PROBE_'):continue
        moves=sorted([f for f in o.component.features.moveFeatures if f.name.startswith('RevD_') and 'angle_driven_rotation' in f.name],key=lambda f:f.timelineObject.index)
        assert len(moves) in (2,3)
        for f in moves[:-1]:
            old=f.definition.angle.expression;f.definition.angle.expression='0 deg'
            rows.append(dict(component=o.component.name,index=f.timelineObject.index,prior_expression=old,new_expression='0 deg'))
        live=moves[-1];rows.append(dict(component=o.component.name,index=live.timelineObject.index,live_expression=live.definition.angle.expression))
    assert len(rows)==10 and d.computeAll()
    assert not [i for i in range(d.timeline.count) if d.timeline.item(i).healthState in (adsk.fusion.FeatureHealthStates.WarningFeatureHealthState,adsk.fusion.FeatureHealthStates.ErrorFeatureHealthState)]
    open(os.path.join(BASE,'verification','RevD_Angle_Finish.json'),'w').write(json.dumps({'revision':'Rev-D','timeline':1700,'rotations':rows,'reason':'Fusion stores these root-requested body moves on the owning component. Earlier root-only deletion loops found none; six superseded rotations are now fixed at zero. Four final-axis moves remain parameter driven.'},indent=2))
    print('One live angle driver per probe; six superseded rotations fixed at zero')
