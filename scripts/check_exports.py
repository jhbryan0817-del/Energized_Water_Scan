"""Verify current Rev-E print/export set; fail on topology or geometry regressions."""
from pathlib import Path
import hashlib,json,re,zipfile
from check_mesh import check
ROOT=Path(__file__).resolve().parents[1]
def main():
    manifest=json.loads((ROOT/'verification/RevE_Export_Manifest.json').read_text())
    audit=json.loads((ROOT/'verification/RevE_Assembly_Audit.json').read_text())
    native=json.loads((ROOT/'verification/RevE_Native_Roundtrip.json').read_text())
    service=json.loads((ROOT/'verification/RevE_Service_Audit.json').read_text())
    poses=json.loads((ROOT/'verification/RevE_Native_Pose_Audit.json').read_text())
    assert poses['passed'] and len(poses['checks'])==16
    assert manifest['timeline']==audit['timeline']==native['timeline']==service['timeline']
    checks=[]
    for row in manifest['prints']:
        c=check(ROOT/'prints'/row['file']);c['extent_error_mm']=max(abs(a-b) for a,b in zip(c['extent_mm'],row['extent_mm']));c['volume_relative_error']=abs(c['signed_volume_mm3']-row['volume_mm3'])/row['volume_mm3'];checks.append(c)
    (ROOT/'verification/RevE_STL_Check.json').write_text(json.dumps(checks,indent=2)+'\n')
    assert len(checks)==23 and all(c['passed'] and c['extent_error_mm']<.05 and c['volume_relative_error']<.001 for c in checks),[(c['file'],c['passed'],c['extent_error_mm'],c['volume_relative_error']) for c in checks if not c['passed'] or c['extent_error_mm']>=.05 or c['volume_relative_error']>=.001]
    assert {p.name for p in (ROOT/'prints').glob('*.stl')}=={c['file'] for c in checks}
    with zipfile.ZipFile(ROOT/'prints/Print_STLs.zip') as z:
        assert set(z.namelist())=={c['file'] for c in checks}
        assert all(z.read(c['file'])==(ROOT/'prints'/c['file']).read_bytes() for c in checks)
    count=len(re.findall(r'=\s*MANIFOLD_SOLID_BREP\s*\(', (ROOT/'cad/Energized_Water_Scanner_RevE.step').read_text()))
    assert count==manifest['step_solids']==audit['body_count']
    assert native['passed'] and not audit['interferences'] and not audit['sampled_motion_collisions'] and not audit['feature_issues'] and not audit['boolean_failures']
    assert not service['boolean_failures'] and not service['intersections']
    assert max(v['error_mm'] for v in audit['tip_position_checks'])<1e-6
    hull=next(b for b in audit['inventory'] if b['component'].startswith('PRINT_01'))
    assert abs(hull['max_mm'][0]-hull['min_mm'][0]-320)<.01 and abs(hull['max_mm'][1]-hull['min_mm'][1]-176)<.01
    for b in audit['inventory']:
        if b['component'].startswith('PROBE_'):assert b['min_mm'][2]>=-.01
    paths=[*ROOT.glob('cad/*RevE*'),*ROOT.glob('prints/*'),*ROOT.glob('previews/RevE*')]
    result={'revision':'Rev-E','passed':True,'timeline':manifest['timeline'],'mesh_count':len(checks),'step_solid_count':count,'hull_footprint_mm':[320,176],'stowed_probe_solids_above_bottom':True,'native_roundtrip_passed':True,'zip_equals_individual_meshes':True,'assembly_pose':[0,0,0,0],'service_report_intersections':len(service['intersections']),'sha256':{str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths if p.is_file()},'assembly_release_passed':False}
    (ROOT/'verification/RevE_Export_Check.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS:23 connected manifold meshes; ZIP, STEP, F3D, footprint, stowage, sampled probe motion and tip coordinates')
if __name__=='__main__':main()
