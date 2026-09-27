"""Revision-matched physical STEP, native archive, stowed-pose STL and previews."""
import adsk.core,adsk.fusion,os,json,zipfile,math
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def run(_context: str):
    app=adsk.core.Application.get();doc=app.activeDocument;d=adsk.fusion.Design.cast(app.activeProduct);root=d.rootComponent
    assert doc.name=='Energized_Water_Scanner'
    def physical(o):return not o.name.startswith(('DATUM','REFERENCE','OPTION','CLEARANCES','INTERFACE_HOLD'))
    def pose(aa):
        for i,v in enumerate(aa,1):d.userParameters.itemByName('probe_E'+str(i)+'_angle').expression=str(v)+' deg'
        assert d.computeAll()
    def prints():
        return [(o,b) for o in root.allOccurrences for b in o.bRepBodies if (o.name.startswith('PRINT_') or b.name.startswith('PRINT_'))]
    def view(name,eye,target,ext):
        p=lambda a:adsk.core.Point3D.create(*[v/10 for v in a])
        c=app.activeViewport.camera;c.isSmoothTransition=False;c.cameraType=adsk.core.CameraTypes.OrthographicCameraType;c.eye=p(eye);c.target=p(target);c.upVector=adsk.core.Vector3D.create(0,0,1);c.viewExtents=ext
        app.activeViewport.camera=c;app.activeViewport.refresh();adsk.doEvents()
        assert app.activeViewport.saveAsImageFile(os.path.join(BASE,'previews',name+'.png'),1600,1100)
    for o in root.allOccurrences:o.isLightBulbOn=physical(o)
    pose([0]*4);view('RevD_stowed',(450,-530,310),(65,0,0),34)
    ps=prints();assert len(ps)==23,len(ps)
    manifest=[]
    for o,b in ps:
        assert b.isSolid and b.lumps.count==1,(o.name,b.name,b.lumps.count)
        name=(b.name if b.name.startswith('PRINT_') else o.component.name).replace(' (1)','')
        opt=d.exportManager.createSTLExportOptions(b,os.path.join(BASE,'prints',name+'.stl'));opt.meshRefinement=adsk.fusion.MeshRefinementSettings.MeshRefinementHigh;opt.unitType=adsk.fusion.DistanceUnits.MillimeterDistanceUnits;opt.isBinaryFormat=True
        assert d.exportManager.execute(opt)
        q=b.boundingBox;manifest.append({'file':name+'.stl','volume_mm3':b.volume*1000,'extent_mm':[(v-w)*10 for v,w in zip(q.maxPoint.asArray(),q.minPoint.asArray())]})
    # Remove only explicitly retired current-print paths, retaining historical CAD and git history.
    for name in ['PRINT_22_E1_dry_servo_pod.stl','PRINT_23_E2_dry_servo_pod.stl','PRINT_24_E3_dry_servo_pod.stl','PRINT_25_E4_dry_servo_pod.stl','PRINT_04_Battery_slide_tray.stl']:
        path=os.path.join(BASE,'prints',name)
        if os.path.isfile(path):os.remove(path)
    with zipfile.ZipFile(os.path.join(BASE,'prints','Print_STLs.zip'),'w',zipfile.ZIP_DEFLATED) as z:
        for p in manifest:z.write(os.path.join(BASE,'prints',p['file']),p['file'])
    pose([0]*4)
    for o in root.allOccurrences:
        if o.name.startswith('PRINT_02'):o.isLightBulbOn=False
    view('RevD_open',(390,-510,440),(40,0,20),33)
    assert d.exportManager.execute(d.exportManager.createFusionArchiveExportOptions(os.path.join(BASE,'cad','Energized_Water_Scanner_RevD.f3d')))
    mgr=adsk.fusion.TemporaryBRepManager.get()
    copies=[(o.component.name,[(b.name,mgr.copy(b)) for b in o.bRepBodies if b.isSolid]) for o in root.allOccurrences if physical(o) and o.bRepBodies.count]
    tmp=app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType);td=adsk.fusion.Design.cast(app.activeProduct);td.designType=adsk.fusion.DesignTypes.DirectDesignType
    for name,bs in copies:
        o=td.rootComponent.occurrences.addNewComponent(adsk.core.Matrix3D.create());o.component.name=name
        for bn,b in bs:o.component.bRepBodies.add(b).name=bn
    assert td.exportManager.execute(td.exportManager.createSTEPExportOptions(os.path.join(BASE,'cad','Energized_Water_Scanner_RevD.step')))
    tmp.close(False);doc.activate()
    result={'revision':'Rev-D','stl_pose':'stowed','assembly_pose':[0,0,0,0],'prints':manifest,'step_solids':sum(len(bs) for _,bs in copies),'timeline':d.timeline.count,'assembly_release_passed':False}
    with open(os.path.join(BASE,'verification','RevD_Export_Manifest.json'),'w') as f:json.dump(result,f,indent=2)
    print(json.dumps({'prints':len(manifest),'step_solids':result['step_solids'],'timeline':d.timeline.count}))
