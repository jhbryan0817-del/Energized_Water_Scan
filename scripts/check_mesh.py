"""Validate binary STL exports using only Python's standard library.
Usage: python scripts/check_stl.py
Checks topology after welding vertices to 1e-5 mm; does not prove printability.
"""
from pathlib import Path
import collections, json, math, struct

def check(path):
    data=path.read_bytes()
    count=struct.unpack_from('<I',data,80)[0]
    assert len(data)==84+50*count, f'{path}: invalid binary STL length'
    vertices={}; coords=[]; faces=[]; edges=collections.Counter(); directed=collections.Counter(); degenerate=0
    for i in range(count):
        row=struct.unpack_from('<12fH',data,84+50*i)
        pts=[tuple(row[k:k+3]) for k in (3,6,9)]
        assert all(math.isfinite(x) for p in pts for x in p), 'nonfinite coordinate'
        ids=[]
        for p in pts:
            key=tuple(round(v,5) for v in p)
            if key not in vertices: vertices[key]=len(coords);coords.append(key)
            ids.append(vertices[key])
        a,b,c=pts; ab=[b[k]-a[k] for k in range(3)]; ac=[c[k]-a[k] for k in range(3)]
        cross=[ab[1]*ac[2]-ab[2]*ac[1],ab[2]*ac[0]-ab[0]*ac[2],ab[0]*ac[1]-ab[1]*ac[0]]
        if len(set(ids))<3 or sum(v*v for v in cross)<1e-16:degenerate+=1
        faces.append(ids)
        for a,b in zip(ids,ids[1:]+ids[:1]):edges[tuple(sorted((a,b)))]+=1;directed[(a,b)]+=1
    adjacent=collections.defaultdict(set)
    for a,b in edges:adjacent[a].add(b);adjacent[b].add(a)
    unseen=set(range(len(coords)));components=0
    while unseen:
        components+=1; stack=[unseen.pop()]
        while stack:
            for v in adjacent[stack.pop()] & unseen:unseen.remove(v);stack.append(v)
    bad=sum(n!=2 for n in edges.values())
    winding=sum(directed[(a,b)]!=1 or directed[(b,a)]!=1 for a,b in edges)
    volume=0
    for ids in faces:
        a,b,c=[coords[i] for i in ids]
        volume+=(a[0]*(b[1]*c[2]-b[2]*c[1])+a[1]*(b[2]*c[0]-b[0]*c[2])+a[2]*(b[0]*c[1]-b[1]*c[0]))/6
    return dict(file=path.name,triangles=count,extent_mm=[round(max(p[i] for p in coords)-min(p[i] for p in coords),4) for i in range(3)],nonmanifold_edge_count=bad,inconsistent_winding_edges=winding,degenerate_triangles=degenerate,connected_components=components,signed_volume_mm3=round(volume,4),passed=bad==0 and winding==0 and degenerate==0 and components==1 and volume>0)

def main():
    root=Path(__file__).resolve().parents[1]
    results=[check(p) for p in sorted((root/'prints').glob('*.stl'))]
    assert len(results)==16, f'Expected 16 default prints; found {len(results)}'
    (root/'verification'/'RevB4_STL_Check.json').write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps(results,indent=2))
    assert all(r['passed'] for r in results), 'STL validation failed'
if __name__=='__main__':main()
