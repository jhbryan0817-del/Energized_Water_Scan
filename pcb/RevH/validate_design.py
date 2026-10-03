"""Run with KiCad 10 Python from this directory; DRC/ERC require kicad-cli."""
from pathlib import Path
import json,pcbnew as p
root=Path(__file__).resolve().parent
b=p.LoadBoard(str(root/'EWS_RevH.kicad_pcb'))
parts=json.loads((root/'component_manifest.json').read_text())
fps={f.GetReference():f for f in b.GetFootprints()}
assert b.GetCopperLayerCount()==6
assert abs(p.ToMM(b.GetDesignSettings().GetBoardThickness())-2)<1e-6
count=0
for z in parts:
 for pin,net in z['pins'].items():
  if net.startswith('FLASH') or net=='ESC_BEC_NC':continue
  pads=[a for a in fps[z['ref']].Pads() if a.GetNumber()==pin]
  assert pads,(z['ref'],pin)
  assert all(a.GetNetname()==net for a in pads),(z['ref'],pin,net)
  count+=len(pads)
for r,x,y in [('H1',33,158.5),('H2',117,158.5),('H3',33,41.5),('H4',117,41.5)]:
 a=next(iter(fps[r].Pads()))
 assert abs(p.ToMM(a.GetPosition().x)-x)<1e-6 and abs(p.ToMM(a.GetPosition().y)-y)<1e-6
 assert abs(p.ToMM(a.GetDrillSize().x)-3.4)<1e-6
print(f'{count} electrical pins match manifest; six layers, 2mm thickness and mounting datums verified')
