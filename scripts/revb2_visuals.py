import adsk.core,adsk.fusion,os,json
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def run(_context: str):
 a=adsk.core.Application.get();d=adsk.fusion.Design.cast(a.activeProduct);r=d.rootComponent
 occ=list(r.allOccurrences);saved=[(o,o.isLightBulbOn) for o in occ]
 P=lambda x,y,z:adsk.core.Point3D.create(x/10,y/10,z/10)
 def view(name,eye,target,extent):
  c=a.activeViewport.camera;c.isSmoothTransition=False;c.cameraType=adsk.core.CameraTypes.OrthographicCameraType;c.eye=P(*eye);c.target=P(*target);c.upVector=adsk.core.Vector3D.create(0,0,1);c.viewExtents=extent;a.activeViewport.camera=c;a.activeViewport.refresh();adsk.doEvents()
  assert a.activeViewport.saveAsImageFile(os.path.join(BASE,'previews',name+'.png'),1800,1100)
 for o in occ:
  if o.name.startswith(('DATUM','REFERENCE','OPTION','CLEARANCES')):o.isLightBulbOn=False
  elif o.name.startswith(('PRINT_02','SEAL_Main')):o.isLightBulbOn=False
  else:o.isLightBulbOn=True
 view('RevB2_open_assembly',(360,-480,400),(55,0,25),31)
 for o in occ:
  if o.name.startswith(('PRINT_02','SEAL_Main')):o.isLightBulbOn=True
 view('RevB2_branding',(40,-500,150),(35,0,35),29)
 for o in occ:o.isLightBulbOn=o.name.startswith(('PRINT_11','PRINT_14','ELECTRODE_E2','PROCURE_Motor_cradle'))
 view('RevB2_E2_side_exit',(70,-120,62),(38,-4,14),5)
 for o,v in saved:o.isLightBulbOn=v
 # Leave the modified open assembly visible, with branding toward the viewer.
 view('RevB2_assembly',(360,-480,400),(55,0,25),31)
 print('Four revision previews saved')
