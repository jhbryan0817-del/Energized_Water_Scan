"""Check Rev-C.1 meshes, ZIP, STEP count, native roundtrip and file hashes."""
from pathlib import Path
import hashlib,json,re,zipfile
from revb4_check_stl import check
ROOT=Path(__file__).resolve().parents[1]
def main():
    manifest=json.loads((ROOT/'verification/RevC_Export_Manifest.json').read_text())
    audit=json.loads((ROOT/'verification/RevC_Assembly_Audit.json').read_text())
    native=json.loads((ROOT/'verification/RevC_Native_Roundtrip.json').read_text())
    assert manifest['timeline']==audit['timeline']==native['timeline']==1523
    baseline=json.loads((ROOT/'verification/RevB4_Assembly_Audit.json').read_text())
    retained=[]
    for part_id in [2,4,9,11,14,16,17,18,19,20,21]:
        prefix='PRINT_'+str(part_id).zfill(2)+'_'
        old=next(b for b in baseline['inventory'] if b['component'].startswith(prefix))
        current=next(b for b in audit['inventory'] if b['component'].startswith(prefix))
        assert abs(old['volume_cm3']*1000-current['volume_mm3'])<1e-5, prefix
        assert all(abs(a-b)<1e-4 for key in ['min_mm','max_mm'] for a,b in zip(old[key],current[key])), prefix
        retained.append(part_id)
    checks=[]
    for row in manifest['prints']:
        c=check(ROOT/'prints'/row['file']);c['extent_error_mm']=max(abs(a-b) for a,b in zip(c['extent_mm'],row['extent_mm']));c['volume_relative_error']=abs(c['signed_volume_mm3']-row['volume_mm3'])/row['volume_mm3'];checks.append(c)
    (ROOT/'verification/RevC_STL_Check.json').write_text(json.dumps(checks,indent=2)+'\n')
    assert len(checks)==21 and all(c['passed'] and c['extent_error_mm']<.05 and c['volume_relative_error']<.001 for c in checks)
    assert {p.name for p in (ROOT/'prints').glob('*.stl')}=={c['file'] for c in checks}
    with zipfile.ZipFile(ROOT/'prints/Print_STLs.zip') as z:
        assert set(z.namelist())=={c['file'] for c in checks}
        assert all(z.read(c['file'])==(ROOT/'prints'/c['file']).read_bytes() for c in checks)
    count=len(re.findall(r'=\s*MANIFOLD_SOLID_BREP\s*\(', (ROOT/'cad/Energized_Water_Scanner_RevC1.step').read_text()))
    assert count==manifest['step_solids']==audit['body_count']
    assert native['passed'] and not audit['interferences'] and not audit['sampled_motion_collisions'] and not audit['feature_issues'] and not audit['boolean_failures']
    assert max(v['error_mm'] for v in audit['tip_position_checks'])<1e-6
    paths=[*ROOT.glob('cad/*RevC1*'),*ROOT.glob('prints/*'),*ROOT.glob('previews/RevC*')]
    result={'revision':'Rev-C.1','passed':True,'timeline':manifest['timeline'],'mesh_count':len(checks),'step_solid_count':count,'retained_print_ids_with_unchanged_bounds_and_volume':retained,'native_roundtrip_passed':True,'zip_equals_individual_meshes':True,'stl_pose':'stowed; compared with stowed BRep export manifest','assembly_pose':'90,30,30,90 deg','sha256':{str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths if p.is_file()},'assembly_release_passed':False}
    (ROOT/'verification/RevC_Export_Check.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS:21 manifold connected meshes, ZIP identity, STEP count, F3D roundtrip, rigid clearance and tip coordinates')
if __name__=='__main__':main()
