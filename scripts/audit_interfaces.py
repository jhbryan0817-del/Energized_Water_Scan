"""Measure drivetrain clearance/coaxiality and document the wet/dry boundary."""
import adsk.core,adsk.fusion,json,os,math
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def run(_context: str):
    a=adsk.core.Application.get();d=adsk.fusion.Design.cast(a.activeProduct);r=d.rootComponent
    def occ(pre):return next(o for o in r.allOccurrences if o.name.startswith(pre))
    mm=lambda p:[v*10 for v in p.asArray()]
    drive=list(occ('DRIVELINE').bRepBodies);battery=occ('BATTERY').bRepBodies.item(0)
    distances=[]
    for b in drive:
        result=a.measureManager.measureMinimumDistance(battery,b)
        distances.append({'body':b.name,'battery_clearance_mm':result.value*10})
    shaft=next(b for b in drive if b.name=='Motor_output_shaft')
    def axis(b):
        cylinders=[f.geometry for f in b.faces if isinstance(f.geometry,adsk.core.Cylinder)]
        c=max(cylinders,key=lambda c:c.radius);return c.origin,c.axis
    p,v=axis(shaft);v.normalize();axes=[]
    for b in drive:
        if 'Propeller' in b.name:continue
        p2,v2=axis(b);v2.normalize();q=p.vectorTo(p2)
        axes.append({'body':b.name,'radial_axis_offset_mm':q.crossProduct(v).length*10,'axis_angle_degrees':math.degrees(math.acos(min(1,abs(v.dotProduct(v2)))) )})
    seals=[]
    for i in range(1,5):
        label='E'+str(i);o=occ('PROCURE_'+label+'_bonded_wire_feedthrough')
        seals.append({'probe':label,'radial_seal':'SKF 6x16x7 HMSA10 RG candidate','cartridge':'Machined POM-C, face gasket retained','wire_entry_bodies':[{'name':b.name,'volume_mm3':b.volume*1000,'min_mm':mm(b.boundingBox.minPoint),'max_mm':mm(b.boundingBox.maxPoint)} for b in o.bRepBodies],'dry_servo':'HS-65HB above sealed output shaft, timing transmission','cover':'Service/dust cover only; not a watertight compartment','qualification':'Supplier water-duty/counterface, gasket compression and potted jacket adhesion/cycle/immersion tests required'})
    hull=occ('PRINT_01');out={'revision':'Rev-E','timeline':d.timeline.count,'hull_transform_cm':hull.transform2.asArray(),'hull_grounded':hull.isGrounded,'motor_axis_unit_vector':v.asArray(),'motor_slope_degrees':math.degrees(math.asin(abs(v.z))),'drivetrain_axes':axes,'battery_clearances':distances,'shaft_coaxiality_passed':max(x['radial_axis_offset_mm'] for x in axes)<1e-5 and max(x['axis_angle_degrees'] for x in axes)<1e-4,'wet_dry_boundary':seals,'waterproof_qualification_passed':False,'assembly_release_passed':False}
    open(os.path.join(BASE,'verification','RevE_Interfaces.json'),'w').write(json.dumps(out,indent=2))
