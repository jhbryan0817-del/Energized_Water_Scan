"""Robot palette and reproducible native Fusion inspection views."""
import adsk.core,adsk.fusion,os,json
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def run(_context: str):
    a=adsk.core.Application.get();d=adsk.fusion.Design.cast(a.activeProduct);r=d.rootComponent
    def physical(o):return not o.name.startswith(('DATUM','REFERENCE','OPTION','CLEARANCES','INTERFACE_HOLD'))
    # Copy a known solid-color appearance; never edit a shared library asset.
    source=None
    for lib in a.materialLibraries:
        for ap in lib.appearances:
            if ap.name in ['Paint - Enamel Glossy (White)','Plastic - Matte (White)','ABS (White)']:
                source=ap;break
        if source:break
    if not source:
        source=next(ap for ap in d.appearances if any(p.objectType==adsk.core.ColorProperty.classType() for p in ap.appearanceProperties))
    palette={}
    for name,rgb in [('Graphite',(40,49,61)),('Ceramic',(200,213,220)),('Signal',(0,195,213)),('Orange',(250,145,35)),('Dark',(23,27,34))]:
        ap=d.appearances.itemByName('RevD_'+name) or d.appearances.addByCopy(source,'RevD_'+name)
        colors=[p for p in ap.appearanceProperties if p.objectType==adsk.core.ColorProperty.classType()]
        assert colors,ap.name
        for p in colors:
            if p.id in ['opaque_albedo','generic_diffuse','surface_albedo']:p.value=adsk.core.Color.create(*rgb,255)
        palette[name]=ap
    for o in r.allOccurrences:
        n=o.name
        if n.startswith('PRINT_01'):o.appearance=palette['Graphite']
        elif n.startswith('PRINT_02'):o.appearance=palette['Ceramic']
        elif n.startswith(('PRINT_22','PRINT_23','PRINT_24','PRINT_25')):o.appearance=palette['Signal']
        elif n.startswith(('PRINT_03','PRINT_04','PRINT_30','PRINT_31')):o.appearance=palette['Ceramic']
        elif n.startswith('PRINT_'):o.appearance=palette['Orange']
        if n.startswith('PROBE_'):
            f=o.component.features.baseFeatures.item(0);assert f.startEdit()
            for b in f.bodies:
                if b.name.startswith('PRINT_'):
                    b.appearance=palette['Signal']
                    for face in b.faces:face.appearance=palette['Signal']
            assert f.finishEdit()
        for b in o.component.bRepBodies:
            if n.startswith('PRINT_01'):b.appearance=palette['Graphite']
            elif n.startswith('PRINT_02'):b.appearance=palette['Ceramic']
            elif n.startswith(('PRINT_22','PRINT_23','PRINT_24','PRINT_25')):b.appearance=palette['Signal']
            elif n.startswith(('PRINT_03','PRINT_04','PRINT_30','PRINT_31')):b.appearance=palette['Ceramic']
            elif b.name.startswith(('PRINT_26','PRINT_27','PRINT_28','PRINT_29')):b.appearance=palette['Signal']
            elif 'ALLOCATION' in n:b.appearance=palette['Dark']
            elif n.startswith('PRINT_'):b.appearance=palette['Orange']
            if n.startswith('PRINT_') or b.name.startswith('PRINT_'):
                for face in b.faces: face.appearance=b.appearance
    def pose(aa):
        for i,v in enumerate(aa,1):d.userParameters.itemByName('probe_E'+str(i)+'_angle').expression=str(v)+' deg'
        assert d.computeAll()
    def view(name,eye,target,up,ext):
        p=lambda q:adsk.core.Point3D.create(*[v/10 for v in q]);c=a.activeViewport.camera;c.isSmoothTransition=False;c.cameraType=adsk.core.CameraTypes.OrthographicCameraType;c.eye=p(eye);c.target=p(target);c.upVector=adsk.core.Vector3D.create(*up);c.viewExtents=ext;a.activeViewport.camera=c;a.activeViewport.refresh();adsk.doEvents()
        assert a.activeViewport.saveAsImageFile(os.path.join(BASE,'previews',name+'.png'),1600,1100)
    for o in r.allOccurrences:o.isLightBulbOn=physical(o)
    pose([0]*4);view('RevD_closed',(430,-510,330),(55,0,15),(0,0,1),34)
    view('RevD_stowed_bottom',(360,-460,-380),(45,0,10),(0,0,1),34)
    for o in r.allOccurrences:
        if o.name.startswith('PRINT_02'):o.isLightBulbOn=False
    view('RevD_open',(390,-510,440),(40,0,20),(0,0,1),33)
    keep=('PRINT_01','PRINT_22','PRINT_23','PRINT_24','PRINT_25')
    for o in r.allOccurrences:o.isLightBulbOn=o.name.startswith(keep)
    view('RevD_four_wells',(320,-460,460),(20,0,20),(0,0,1),31)
    for o in r.allOccurrences:o.isLightBulbOn=physical(o)
    pose([90]*4);view('RevD_deployed',(430,-510,290),(45,0,-35),(0,0,1),39)
    pose([60,20,20,45]);view('RevD_measurement',(430,-510,290),(45,0,-30),(0,0,1),39)
    pose([0]*4)
    for o in r.allOccurrences:
        if o.name.startswith('PRINT_02'):o.isLightBulbOn=False
    view('RevD_open',(390,-510,440),(40,0,20),(0,0,1),33)
    print('RevD palette and six inspection views saved')
