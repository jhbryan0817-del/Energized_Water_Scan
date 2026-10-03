from pathlib import Path
import json,uuid,math
OUT=Path(__file__).resolve().parent
parts=json.loads((OUT/'component_manifest.json').read_text())
def uid(s):return str(uuid.uuid5(uuid.NAMESPACE_DNS,'EWS.RevH.'+s))
def q(s):return json.dumps(str(s))
def fx(size=1):return f'(effects (font (size {size} {size})))'
rootid=uid('root')
pages={
 'Control': [z for z in parts if z['ref'] in ['U1','J1','J2','J3','JP1']],
 'Power': [z for z in parts if z['ref'] in ['U5','U6','J5','J6','J7','J8','J9','J10','J11','R50','R51','R52','R53','Q1','F1','D5','D6','R60','C40','C41','C42']],
 'Input_protection':[z for z in parts if z['ref'] in ['J12','J13','D1','D2','D3','D4'] or (z['ref'].startswith('R') and int(z['ref'][1:])>=100)],
 'Isolation':[z for z in parts if z['ref'] in ['U2','U3'] or (z['group'] in ['HI','LO'] and not z['ref'].startswith('D')) or z['ref'] in ['R3','R13','C5','C6','C7','C15','C16','C17']],
}
pages['Health']=[z for z in parts if z['ref'] in ['J14','R61','R62','R63','C43','R64','R65','C44']]
used={z['ref'] for pp in pages.values() for z in pp}
pages['ADC']=[z for z in parts if z['ref'] not in used and not z['ref'].startswith('H')]
pages['Control'].append(dict(ref='#FLG01',value='PWR_FLAG_JP1_FITTED',footprint='',pins={'1':'ESP_5V'},uuid=uid('power_flag'),note='Power is present only with JP1 fitted. Remove JP1 before USB.'))
assert len([z['ref'] for pp in pages.values() for z in pp])==len(set(z['ref'] for pp in pages.values() for z in pp))
pin_names={
'U1':dict(enumerate(['3V3','EN','GPIO36_IN','GPIO39_IN','GPIO34_IN','GPIO35_IN','GPIO32','GPIO33','GPIO25','GPIO26','GPIO27','GPIO14','GPIO12_STRAP','GND','GPIO13','FLASH9_RESERVED','FLASH10_RESERVED','FLASH11_RESERVED','5V','GND','GPIO23','GPIO22','TX0','RX0','GPIO21','GND','GPIO19','GPIO18','GPIO5_STRAP','GPIO17_WROOM','GPIO16_WROOM','GPIO4','GPIO0_BOOT','GPIO2_STRAP','GPIO15_STRAP','FLASH8_RESERVED','FLASH7_RESERVED','FLASH6_RESERVED'],1)),
'U2':dict(enumerate(['DCDC_OUT','DCDC_HGND','HLDO_IN','NC','HLDO_OUT','INP','INN','HGND','GND','OUTN','OUTP','VDD','LDO_OUT','DIAG_N','DCDC_GND','DCDC_IN'],1)),
'U4':dict(enumerate(['ADDR','ALERT_RDY','GND','AIN0','AIN1','AIN2','AIN3','VDD','SDA','SCL'],1)),
'U5':dict(enumerate(['PG','SHDN_VIN_REF','VIN','GND','VOUT_5V'],1)),
'U6':dict(enumerate(['EN_VIN_REF','VIN','GND','GND','VOUT_5V'],1))}
pin_names['U3']=pin_names['U2']
pin_names['U7']=pin_names['U4']
pin_names['Q1']={1:'GATE',2:'DRAIN',3:'SOURCE'}
pin_names['D5']={1:'K',2:'A'}
pin_names['D6']={1:'K',2:'A'}
def pintype(z,num):
    ref=z['ref'];n=int(num)
    if ref.startswith('#'):return 'power_out'
    if ref in ('U2','U3'):
        return {1:'power_out',2:'passive',3:'power_in',4:'passive',5:'power_out',6:'input',7:'input',8:'passive',9:'passive',10:'output',11:'output',12:'power_in',13:'power_out',14:'open_collector',15:'passive',16:'power_in'}[n]
    if ref=='U1':return 'power_out' if n==1 else ('power_in' if n==19 else ('input' if n in [2,3,4,5,6] else 'bidirectional'))
    if ref in ('U4','U7'):return {1:'input',2:'open_collector',3:'passive',4:'input',5:'input',6:'input',7:'input',8:'power_in',9:'bidirectional',10:'input'}[n]
    if ref=='U5':return {1:'open_collector',2:'input',3:'passive',4:'passive',5:'power_out'}[n]
    if ref=='U6':return {1:'input',2:'passive',3:'passive',4:'passive',5:'power_out'}[n]
    return 'passive'
def symbol(z):
    ref=z['ref'];nn=len(z['pins']);nr=math.ceil(nn/2);h=max(5.08,(nr+1)*2.54);w=17.78 if nn>10 else 11.43
    geom=[]; coords={}
    for i,(num,net) in enumerate(z['pins'].items()):
        left=i<nr; row=i if left else i-nr;yy=h/2-2.54*(row+1);xx=(-w-5.08) if left else(w+5.08);angle=0 if left else 180
        pname=pin_names.get(ref,{}).get(int(num),str(num))
        if ref in ('D1','D2','D3','D4'):pname={1:'A1',2:'K2',3:'K1_A2'}[int(num)]
        geom.append(f'(pin {pintype(z,num)} line (at {xx} {yy} {angle}) (length 5.08) (name {q(pname)} {fx(.8)}) (number {q(num)} {fx(.8)}))')
        coords[num]=(xx,yy,left)
    lib=f'''(symbol "EWS:{ref}" (pin_names (offset 0.5)) (in_bom yes) (on_board yes)
    (property "Reference" {q(ref)} (at 0 {h/2+3} 0) {fx()})
    (property "Value" {q(z['value'])} (at 0 {-h/2-3} 0) {fx(.8)})
    (property "Footprint" {q(z['footprint'])} (at 0 0 0) (effects (font (size 1 1)) hide))
    (symbol "{ref}_0_1" (rectangle (start {-w} {h/2}) (end {w} {-h/2}) (stroke (width .254) (type default)) (fill (type background))))
    (symbol "{ref}_1_1" {''.join(geom)}))'''
    return lib,coords,h
def base(pageid,title,paper='A3'):
    return f'''(kicad_sch (version 20250114) (generator "eeschema") (uuid {pageid}) (paper "{paper}")
    (title_block (title {q(title)}) (rev "H prototype") (company "IoT Beyond Lab") (comment 1 "Engineering prototype - qualification required"))'''
all_libs=[]
for pagenu,(name,pp) in enumerate(pages.items(),2):
    pageid=uid(name);symbols=[];instances=[];labels=[]
    cols=3 if name=='Control' else 4
    cellw=125 if name=='Control' else 96
    cellh=85 if name=='Control' else 38
    for idx,z in enumerate(pp):
        lib,coords,h=symbol(z);symbols.append(lib);all_libs.append(lib.replace('"EWS:'+z['ref']+'"','"'+z['ref']+'"',1))
        xx=round((cellw*(idx%cols)+cellw/2+10)/1.27)*1.27; yy=round((48+cellh*(idx//cols))/1.27)*1.27
        labels.append(f'(text {q(z["note"][:85])} (at {xx} {yy+h/2+9} 0) {fx(.7)})' if z['note'] else '')
        instances.append(f'''(symbol (lib_id "EWS:{z['ref']}") (at {xx} {yy} 0) (unit 1) (in_bom yes) (on_board yes) (dnp no) (uuid {z['uuid']})
        (property "Reference" {q(z['ref'])} (at {xx} {yy-h/2-3} 0) {fx()})
        (property "Value" {q(z['value'])} (at {xx} {yy+h/2+3} 0) {fx(.8)})
        (property "Footprint" {q(z['footprint'])} (at {xx} {yy} 0) (effects (font (size 1 1)) hide))
        (instances (project "EWS_RevH" (path "/{rootid}/{pageid}" (reference {q(z['ref'])}) (unit 1)))))''')
        for num,(dx,dy,left) in coords.items():
            net=z['pins'][num]; px=xx+dx;py=yy-dy; ex=px+(-5.08 if left else 5.08)
            if net.startswith('FLASH') or net=='ESC_BEC_NC':
                labels.append(f'(no_connect (at {px} {py}) (uuid {uid(z["ref"]+num+"nc")}))');continue
            labels.append(f'(wire (pts (xy {px} {py}) (xy {ex} {py})) (stroke (width 0) (type default)) (uuid {uid(z["ref"]+num+"w")}))')
            labels.append(f'(global_label {q(net)} (shape bidirectional) (at {ex} {py} {0 if left else 180}) (effects (font (size .8 .8)) (justify {"left" if left else "right"})) (uuid {uid(z["ref"]+num+"l")}))')
    content=base(pageid,'EWS Rev H / '+name)+'\n(lib_symbols '+''.join(symbols)+')\n'+''.join(instances)+''.join(labels)+')'
    if name=='Control':
        content=content.replace('(symbol "EWS:#FLG01" (pin_names (offset 0.5)) (in_bom yes) (on_board yes)', '(symbol "EWS:#FLG01" (pin_names (offset 0.5)) (in_bom no) (on_board no)')
        content=content.replace('(unit 1) (in_bom yes) (on_board yes) (dnp no) (uuid '+uid('power_flag')+')','(unit 1) (in_bom no) (on_board no) (dnp no) (uuid '+uid('power_flag')+')')
    (OUT/(name+'.kicad_sch')).write_text(content)
root=base(rootid,'EWS Rev H / System overview')+'\n(lib_symbols)\n'
notes=['Two electrodes E2/E4 -> four-resistor-per-leg input networks -> dual AMC3330 isolated paths -> independent ADS1115 converters -> ESP32.',
       'HI: 997:1 divider; 600 VAC RMS design target. LO: 10.96:1 divider; use conservative +/-2 V working range before characterization.',
       'Both ADCs sample continuously at 860 SPS nominal; separate unsynchronized clocks. DIAG and READY are wired to ESP32.',
       '2S harness -> F1 -> Q1 -> protected VBAT. Motor/ESC power stays external. Never parallel ESC BEC.',
       'Remove JP1 before USB. U1 requires WROOM pin availability. Expansion signals are 3.3 V only.',
       'No CAT rating, surge qualification, water-safety threshold or guaranteed detection floor is claimed.']
for i,t in enumerate(notes):root+=f'(text {q(t)} (at 20 {20+i*7} 0) (effects (font (size 1.1 1.1)) (justify left)))\n'
for i,name in enumerate(pages):
    xx=30+(i%3)*115;yy=90+(i//3)*65;pageid=uid(name)
    root+=f'''(sheet (at {xx} {yy}) (size 90 40) (stroke (width .254) (type default)) (fill (color 0 0 0 0)) (uuid {pageid})
    (property "Sheetname" {q(name)} (at {xx} {yy-2} 0) (effects (font (size 1.3 1.3)) (justify left)))
    (property "Sheetfile" {q(name+'.kicad_sch')} (at {xx} {yy+42} 0) (effects (font (size 1 1)) (justify left)))
    (instances (project "EWS_RevH" (path "/{rootid}" (page "{i+2}")))))'''
root+='(sheet_instances (path "/" (page "1"))))'
(OUT/'EWS_RevH.kicad_sch').write_text(root)
(OUT/'EWS.kicad_sym').write_text('(kicad_symbol_lib (version 20250114) (generator "kicad_symbol_editor") '+''.join(all_libs)+')')
(OUT/'sym-lib-table').write_text('(sym_lib_table (version 7) (lib (name "EWS")(type "KiCad")(uri "${KIPRJMOD}/EWS.kicad_sym")(options "")(descr "Project-local reviewed pin definitions")))')
print({name:len(pp) for name,pp in pages.items()})
(OUT/'schematic_paths.json').write_text(json.dumps({z['ref']:'/'+rootid+'/'+uid(name)+'/'+z['uuid'] for name,pp in pages.items() for z in pp if not z['ref'].startswith('#')},indent=2))
