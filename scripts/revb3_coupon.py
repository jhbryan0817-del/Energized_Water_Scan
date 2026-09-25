"""Export an actual hull subsection for E2 and motor-support fit trials.
Open section: not a watertight hull and not a surrogate for E1 access.
"""
import adsk.core,adsk.fusion,os,json
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def run(_context: str):
 a=adsk.core.Application.get();original=a.activeDocument;d=adsk.fusion.Design.cast(a.activeProduct)
 assert original.name=='Energized_Water_Scanner' and d.timeline.count==1236
 m=adsk.fusion.TemporaryBRepManager.get();P=lambda x,y,z:adsk.core.Point3D.create(x/10,y/10,z/10)
 V=adsk.core.Vector3D.create
 hull=next(o for o in d.rootComponent.allOccurrences if o.name.startswith('PRINT_01')).bRepBodies.item(0)
 clip=m.createBox(adsk.core.OrientedBoundingBox3D.create(P(40,0,8),V(1,0,0),V(0,1,0),5.2,6.8,1.6))
 body=m.copy(hull);assert m.booleanOperation(body,clip,adsk.fusion.BooleanTypes.IntersectionBooleanType)
 assert body.lumps.count==1
 # Confirm the nominal 2 mm floor beneath every revised pilot using solid intersection.
 floors=[]
 for x,ys in [(26,[-23,23]),(60,[-27,27])]:
  for y in ys:
   tool=m.createCylinderOrCone(P(x,y,0),.125,P(x,y,2),.125);expected=tool.volume
   assert m.booleanOperation(tool,m.copy(hull),adsk.fusion.BooleanTypes.IntersectionBooleanType)
   fraction=tool.volume/expected;assert abs(fraction-1)<1e-6
   floors.append({'center_mm':[x,y],'floor_z_mm':[0,2],'solid_fraction':fraction})
 tmp=a.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType);td=adsk.fusion.Design.cast(a.activeProduct);td.designType=adsk.fusion.DesignTypes.DirectDesignType
 b=td.rootComponent.bRepBodies.add(body);b.name='RevB3_E2_motor_mount_hull_section'
 os.makedirs(os.path.join(BASE,'coupons'),exist_ok=True)
 opt=td.exportManager.createSTLExportOptions(b,os.path.join(BASE,'coupons','COUPON_01_E2_motor_mount_hull_section.stl'))
 opt.meshRefinement=adsk.fusion.MeshRefinementSettings.MeshRefinementHigh;opt.unitType=adsk.fusion.DistanceUnits.MillimeterDistanceUnits;opt.isBinaryFormat=True
 assert td.exportManager.execute(opt);tmp.close(False);original.activate()
 result={'revision':'Rev-B.3','clip_min_mm':[14,-34,0],'clip_max_mm':[66,34,16],'motor_pilot_floor_checks':floors,'limits':'Actual hull subsection for fit trials only; open cut faces invalidate whole-hull stiffness and leak-test claims. No E1 tool access represented.'}
 with open(os.path.join(BASE,'verification','RevB3_Coupon_Check.json'),'w') as f:json.dump(result,f,indent=2)
 print(json.dumps(result))

