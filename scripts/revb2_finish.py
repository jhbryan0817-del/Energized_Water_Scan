"""Follow-up corrections from the first exact collision/access audit."""
import adsk.core,adsk.fusion,json,math
def run(_context: str):
 a=adsk.core.Application.get();d=adsk.fusion.Design.cast(a.activeProduct);r=d.rootComponent;m=adsk.fusion.TemporaryBRepManager.get()
 P=lambda x,y,z:adsk.core.Point3D.create(x/10,y/10,z/10)
 V=adsk.core.Vector3D.create
 def comp(pre):return next(o.component for o in r.allOccurrences if o.name.startswith(pre))
 def box(x0,y0,z0,x1,y1,z1):return m.createBox(adsk.core.OrientedBoundingBox3D.create(P((x0+x1)/2,(y0+y1)/2,(z0+z1)/2),V(1,0,0),V(0,1,0),(x1-x0)/10,(y1-y0)/10,(z1-z0)/10))
 def persist(c,b,name):
  f=c.features.baseFeatures.add();f.name=name;f.startEdit();c.bRepBodies.add(b,f);f.finishEdit();return f.bodies.item(0)
 def cut(c,t,name):
  b=c.bRepBodies.item(0);t=persist(c,t,name+'_tool');oc=adsk.core.ObjectCollection.create();oc.add(t)
  i=c.features.combineFeatures.createInput(b,oc);i.operation=adsk.fusion.FeatureOperations.CutFeatureOperation;c.features.combineFeatures.add(i).name=name
 for pre,x,ys in [('PRINT_14',26,[-23,23]),('PRINT_11',60,[-27,27])]:
  for y in ys:cut(comp(pre),m.createCylinderOrCone(P(x,y,2.9),.42,P(x,y,9),.42),'RevB2_hull_boss_recess_D8_4')
 for pre in ['PRINT_03','PRINT_18']:cut(comp(pre),box(-29,50.4,19,-20,51.1,40),'RevB2_USB_corridor_clearance')
 for pre in ['PRINT_03','PRINT_20']:cut(comp(pre),box(59,58.8,19,68,61,40),'RevB2_power_route_clearance')
 # Fill the nominal 0.4 mm radial motor/cradle gap with a specified liner envelope.
 p=P(26.0222252113,0,37.7645713531);q=P(43.4088900845,0,33.1058285412)
 b=m.createCylinderOrCone(p,1.5,q,1.5);inner=m.createCylinderOrCone(p,1.46,q,1.46)
 assert m.booleanOperation(b,inner,adsk.fusion.BooleanTypes.DifferenceBooleanType)
 assert m.booleanOperation(b,box(20,-16,16,50,16,30),adsk.fusion.BooleanTypes.IntersectionBooleanType)
 # Preserve the central electrode relief beneath the liner as well.
 hole=m.createCylinderOrCone(P(40,0,0),.8,P(40,0,40),.8)
 assert m.booleanOperation(b,hole,adsk.fusion.BooleanTypes.DifferenceBooleanType)
 o=r.occurrences.addNewComponent(adsk.core.Matrix3D.create());o.component.name='PROCURE_Motor_cradle_liner_0_4mm_VERIFY';persist(o.component,b,'Conformal_nonconductive_liner')
 hull=comp('PRINT_01');face=next(f for f in hull.bRepBodies.item(0).faces if isinstance(f.geometry,adsk.core.Plane) and f.area>150 and f.boundingBox.maxPoint.y<-7)
 s=hull.sketches.add(face);s.name='RevB2_IoT_Beyond_Lab_side_branding'
 print(json.dumps({'sketch_origin':s.sketchToModelSpace(P(0,0,0)).asArray(),'x':s.sketchToModelSpace(P(10,0,0)).asArray(),'y':s.sketchToModelSpace(P(0,10,0)).asArray(),'normal':s.sketchToModelSpace(P(0,0,10)).asArray(),'corner0':s.modelToSketchSpace(P(-60,-75-40/6.5,40)).asArray(),'corner1':s.modelToSketchSpace(P(110,-75-57/6.5,57)).asArray(),'timeline':d.timeline.count}))
