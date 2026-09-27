"""Refresh native inspection views after final motion fixes; no geometry edits."""
import adsk.core,adsk.fusion,os
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def run(_context: str):
    a=adsk.core.Application.get();d=adsk.fusion.Design.cast(a.activeProduct);r=d.rootComponent
    # Mid-graphite is readable under the viewport's fixed underside lighting.
    ap=d.appearances.itemByName('RevD_Graphite');assert ap
    for p in ap.appearanceProperties:
        if p.id in ('opaque_albedo','generic_diffuse','surface_albedo'):p.value=adsk.core.Color.create(100,114,132,255)
    def physical(o):return not o.name.startswith(('DATUM','REFERENCE','OPTION','CLEARANCES','INTERFACE_HOLD'))
    def pose(aa):
        for i,v in enumerate(aa,1):d.userParameters.itemByName('probe_E'+str(i)+'_angle').expression=str(v)+' deg'
        assert d.computeAll();adsk.doEvents()
    def view(name,eye,target,ext):
        p=lambda q:adsk.core.Point3D.create(*[v/10 for v in q]);c=a.activeViewport.camera;c.isSmoothTransition=False;c.cameraType=adsk.core.CameraTypes.OrthographicCameraType;c.eye=p(eye);c.target=p(target);c.upVector=adsk.core.Vector3D.create(0,0,1);c.viewExtents=ext;a.activeViewport.camera=c;a.activeViewport.refresh();adsk.doEvents()
        assert a.activeViewport.saveAsImageFile(os.path.join(BASE,'previews',name+'.png'),1600,1100)
    for o in r.allOccurrences:o.isLightBulbOn=physical(o)
    pose([0]*4);view('RevD_closed',(430,-510,330),(55,0,15),34)
    view('RevD_stowed_bottom',(360,-460,-380),(45,0,10),34)
    for o in r.allOccurrences:
        if o.name.startswith('PRINT_02'):o.isLightBulbOn=False
    view('RevD_open',(390,-510,440),(40,0,20),33)
    keep=('PRINT_01','PRINT_22','PRINT_23','PRINT_24','PRINT_25')
    for o in r.allOccurrences:o.isLightBulbOn=o.name.startswith(keep)
    view('RevD_four_wells',(320,-460,460),(20,0,20),31)
    for o in r.allOccurrences:o.isLightBulbOn=physical(o)
    pose([90]*4);view('RevD_deployed',(430,-510,290),(45,0,-35),39)
    pose([60,20,20,45]);view('RevD_measurement',(430,-510,290),(45,0,-30),39)
    pose([0]*4)
    for o in r.allOccurrences:
        if o.name.startswith('PRINT_02'):o.isLightBulbOn=False
    view('RevD_open',(390,-510,440),(40,0,20),33)
    print('Six final native inspection views refreshed')
