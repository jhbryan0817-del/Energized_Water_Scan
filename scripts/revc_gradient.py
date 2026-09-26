"""Geometry and local affine-gradient demonstrator; NOT instrument firmware.
Run with Python 3 + numpy: python scripts/revc_gradient.py
Coordinates: millimetres in CAD, metres in estimator. Electric field E=-grad(V).
"""
import json, math
from pathlib import Path
import numpy as np

HINGES_MM=np.array([[-75.,-77.,-18.],[90.,-77.,-18.],[-75.,77.,-18.],[90.,77.,-18.]])
RADIUS_MM=132.
RECOMMENDED_DEG=[90.,30.,30.,90.]

def tip_positions(angles_deg):
    a=np.asarray(angles_deg,dtype=float)
    if a.shape!=(4,) or not np.all(np.isfinite(a)) or np.any(a<0) or np.any(a>90):
        raise ValueError('Four finite angles in [0,90] degrees are required')
    a=np.deg2rad(a)
    p=HINGES_MM.copy();p[:,0]+=RADIUS_MM*np.cos(a);p[:,2]-=RADIUS_MM*np.sin(a)
    # Exposed head center is outboard of arm center; use each 82.3 mm Y datum.
    p[:,1]=np.sign(p[:,1])*82.3
    return p/1000.

def geometry(angles_deg):
    p=tip_positions(angles_deg)
    # ADS1115-supported pairs A0-A3, A1-A3, A2-A3; E4 is common reference.
    A=p[:3]-p[3]
    singular=np.linalg.svd(A,compute_uv=False)
    rank=int(np.linalg.matrix_rank(A))
    condition=float(singular[0]/singular[-1]) if rank==3 else None
    return p,A,rank,condition

def estimate_gradient(angles_deg, voltage_differences, max_condition=10.):
    _,A,rank,cond=geometry(angles_deg)
    if rank!=3 or cond>max_condition:
        raise ValueError('Unobservable or poorly conditioned pose; no 3D gradient reported')
    dv=np.asarray(voltage_differences)
    if dv.shape!=(3,) or not np.all(np.isfinite(dv)):
        raise ValueError('Require three coherent finite differences V1-V4,V2-V4,V3-V4')
    return np.linalg.solve(A,dv)

def verify():
    records=[]
    for label,a in [('stowed',[0]*4),('equal_45',[45]*4),('fully_down',[90]*4),('measurement',RECOMMENDED_DEG)]:
        p,A,rank,cond=geometry(a)
        records.append(dict(pose=label,angles_deg=a,tip_positions_mm=(p*1000).tolist(),rank=rank,condition_number=cond,det_m3=float(np.linalg.det(A))))
        if label!='measurement':
            assert rank==2
            try:estimate_gradient(a,[0,0,0])
            except ValueError:pass
            else:raise AssertionError('Planar geometry was accepted')
    _,A,rank,cond=geometry(RECOMMENDED_DEG)
    assert rank==3 and cond<10
    for truth in [np.array([.3,-.2,1.1]),np.array([.3+1j,-.2+.4j,1.1-.7j])]:
        got=estimate_gradient(RECOMMENDED_DEG,A@truth)
        assert np.allclose(got,truth,rtol=1e-12,atol=1e-12)
    for bad in [[-1,0,0,0],[0,0,0,91],[0,0,0],[0,0,0,float('nan')]]:
        try:tip_positions(bad)
        except ValueError:pass
        else:raise AssertionError('Invalid angles accepted')
    # Common-reference differencing has correlated noise; independent electrode noise is assumed here.
    sigma=1e-3
    R=sigma*sigma*(np.eye(3)+np.ones((3,3)))
    Ai=np.linalg.inv(A);cov=Ai@R@Ai.T
    # One-sided 1-degree calibration-error examples for a unit vertical gradient; not worst-case bounds.
    truth=np.array([0.,0.,1.]);dv=A@truth;errors=[]
    for i in range(4):
        test=np.array(RECOMMENDED_DEG);test[i]+=(-1 if test[i]>=90 else 1)
        errors.append((estimate_gradient(test,dv)-truth).tolist())
    result={'revision':'Rev-C.1','poses':records,'synthetic_recovery_passed':True,'invalid_pose_rejection_passed':True,'one_mV_independent_electrode_noise_gradient_std_V_per_m':np.sqrt(np.diag(cov)).tolist(),'one_degree_calibration_error_examples_V_per_m':errors,'limitations':'Affine field only; synthetic math does not validate ADC, angle repeatability, conductivity boundaries, electrode offsets or moving water measurements'}
    dest=Path(__file__).resolve().parents[1]/'verification'/'RevC_Observability.json';dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    return result

if __name__=='__main__':verify()
