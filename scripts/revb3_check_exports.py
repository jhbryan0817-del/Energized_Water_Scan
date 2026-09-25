"""Verify Rev-B.3 export consistency; run after Fusion audits and mesh export."""
from pathlib import Path
import hashlib,json,re,zipfile
from revb3_check_stl import check

ROOT=Path(__file__).resolve().parents[1]
def main():
    audit=json.loads((ROOT/'verification/RevB3_Assembly_Audit.json').read_text())
    meshes=json.loads((ROOT/'verification/RevB3_STL_Check.json').read_text())
    native=json.loads((ROOT/'verification/RevB3_Native_Roundtrip.json').read_text())
    step=(ROOT/'cad/Energized_Water_Scanner_RevB3.step').read_text()
    count=len(re.findall(r'=\s*MANIFOLD_SOLID_BREP\s*\(',step))
    checks=[]
    for mesh in meshes:
        name=mesh['file'][:-4]
        body=next(b for b in audit['inventory'] if b['component'].split(':')[0]==name)
        extent=[b-a for a,b in zip(body['min_mm'],body['max_mm'])]
        error=max(abs(a-b) for a,b in zip(extent,mesh['extent_mm']))
        volume_error=abs(mesh['signed_volume_mm3']-body['volume_cm3']*1000)/(body['volume_cm3']*1000)
        checks.append(dict(file=mesh['file'],max_extent_error_mm=error,relative_volume_error=volume_error))
        assert mesh['passed'] and error<.05 and volume_error<.001
    with zipfile.ZipFile(ROOT/'prints/Print_STLs.zip') as z:
        assert set(z.namelist())=={m['file'] for m in meshes}
        assert all(z.read(m['file'])==(ROOT/'prints'/m['file']).read_bytes() for m in meshes)
    assert count==audit['body_count'] and native['passed']
    coupon=check(ROOT/'coupons/COUPON_01_E2_motor_mount_hull_section.stl')
    assert coupon['passed']
    files=[*ROOT.glob('cad/*RevB3*'),*ROOT.glob('prints/*.stl'),ROOT/'prints/Print_STLs.zip',*ROOT.glob('previews/RevB3*'),*ROOT.glob('coupons/*.stl')]
    result=dict(step_solid_count=count,f3d_fusion_roundtrip=native,print_zip_matches_individual_stls=True,stl_matches_current_brep=checks,sha256={str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in files})
    result['coupon_mesh']=coupon
    (ROOT/'verification/RevB3_Export_Check.json').write_text(json.dumps(result,indent=2)+'\n')
    print(f'PASS: {count} STEP solids, native roundtrip, {len(meshes)} meshes and print ZIP consistency')
if __name__=='__main__':main()

