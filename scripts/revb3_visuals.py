import adsk.core,adsk.fusion,os
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def run(_context: str):
 a=adsk.core.Application.get();d=adsk.fusion.Design.cast(a.activeProduct);occ=list(d.rootComponent.allOccurrences)
 saved=[(o,o.isLightBulbOn) for o in occ];camera=a.activeViewport.camera
 P=lambda x,y,z:adsk.core.Point3D.create(x/10,y/10,z/10)
 def view(name,eye,target,extent):
  c=a.activeViewport.camera;c.isSmoothTransition=False;c.cameraType=adsk.core.CameraTypes.OrthographicCameraType;c.eye=P(*eye);c.target=P(*target);c.upVector=adsk.core.Vector3D.create(0,0,1);c.viewExtents=extent;a.activeViewport.camera=c;a.activeViewport.refresh();adsk.doEvents()
  assert a.activeViewport.saveAsImageFile(os.path.join(BASE,'previews',name+'.png'),1600,1000)
 for o in occ:o.isLightBulbOn=not o.name.startswith(('DATUM','REFERENCE','OPTION','CLEARANCES','PRINT_02','SEAL_Main'))
 view('RevB3_open_assembly',(360,-480,400),(55,0,25),31)
 for o in occ:o.isLightBulbOn=o.name.startswith(('PRINT_03','PRINT_18','ESP32'))
 view('RevB3_ESP_header_window',(-65,140,140),(3,46,30),7)
 for o in occ:o.isLightBulbOn=o.name.startswith('PRINT_04')
 view('RevB3_battery_screw_reliefs',(-130,-155,150),(-52.5,0,22),12)
 for o,v in saved:o.isLightBulbOn=v
 a.activeViewport.camera=camera;a.activeViewport.refresh()
 print('Three Rev-B.3 previews saved; original visibility/camera restored')
