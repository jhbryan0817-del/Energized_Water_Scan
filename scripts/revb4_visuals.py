import adsk.core,adsk.fusion,os
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def run(_context: str):
 a=adsk.core.Application.get();d=adsk.fusion.Design.cast(a.activeProduct);occ=list(d.rootComponent.allOccurrences)
 saved=[(o,o.isLightBulbOn) for o in occ];camera=a.activeViewport.camera
 P=lambda x,y,z:adsk.core.Point3D.create(x/10,y/10,z/10)
 for o in occ:o.isLightBulbOn=o.name.startswith(('PRINT_20','D24'))
 c=a.activeViewport.camera;c.isSmoothTransition=False;c.cameraType=adsk.core.CameraTypes.OrthographicCameraType;c.eye=P(100,-50,110);c.target=P(64,42,26);c.upVector=adsk.core.Vector3D.create(0,0,1);c.viewExtents=4.5
 a.activeViewport.camera=c;a.activeViewport.refresh();adsk.doEvents()
 assert a.activeViewport.saveAsImageFile(os.path.join(BASE,'previews','RevB4_regulator_connection_access.png'),1400,1000)
 for o,v in saved:o.isLightBulbOn=v
 a.activeViewport.camera=camera;a.activeViewport.refresh()
 print('Regulator preview saved; visibility/camera restored')
