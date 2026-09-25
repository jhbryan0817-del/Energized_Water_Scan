"""Run once on the 1012-item Rev-B.1 baseline in Fusion. All coordinates are mm.
Fixed-coordinate, named additive features; does not resize purchased components.
Review RevB2_Prototype_Readiness.md before manufacturing.
"""
import adsk.core, adsk.fusion, math, json

def run(_context: str):
 a=adsk.core.Application.get();d=adsk.fusion.Design.cast(a.activeProduct);r=d.rootComponent
 assert a.activeDocument.name=='Energized_Water_Scanner'
 assert d.timeline.count==1012, 'This migration is only for the untouched Rev-B.1 baseline'
 m=adsk.fusion.TemporaryBRepManager.get()
 P=lambda x,y,z:adsk.core.Point3D.create(x/10,y/10,z/10)
 V=adsk.core.Vector3D.create
 def box(x0,y0,z0,x1,y1,z1):
  return m.createBox(adsk.core.OrientedBoundingBox3D.create(P((x0+x1)/2,(y0+y1)/2,(z0+z1)/2),V(1,0,0),V(0,1,0),(x1-x0)/10,(y1-y0)/10,(z1-z0)/10))
 def cyl(x,y,z0,z1,diam):return m.createCylinderOrCone(P(x,y,z0),diam/20,P(x,y,z1),diam/20)
 def boolean(b,t,op):
  assert m.booleanOperation(b,t,op)
  return b
 def union(b,t):return boolean(b,t,adsk.fusion.BooleanTypes.UnionBooleanType)
 def cut(b,t):return boolean(b,t,adsk.fusion.BooleanTypes.DifferenceBooleanType)
 def comp(pre):return next(o.component for o in r.allOccurrences if o.name.startswith(pre))
 def persist(c,body,name):
  f=c.features.baseFeatures.add();f.name=name+'_geometry';assert f.startEdit()
  b=c.bRepBodies.add(body,f);b.name=name;assert f.finishEdit()
  return f.bodies.item(0)
 def modify(c,t,name,join=False,target=None):
  b=target or c.bRepBodies.item(0)
  tool=persist(c,t,name+'_tool');oc=adsk.core.ObjectCollection.create();oc.add(tool)
  inp=c.features.combineFeatures.createInput(b,oc)
  inp.operation=adsk.fusion.FeatureOperations.JoinFeatureOperation if join else adsk.fusion.FeatureOperations.CutFeatureOperation
  f=c.features.combineFeatures.add(inp);f.name=name
  assert c.bRepBodies.count>=1
  return b
 def new(name,body):
  o=r.occurrences.addNewComponent(adsk.core.Matrix3D.create());o.component.name=name
  persist(o.component,body,name);return o
 hull=comp('PRINT_01');tray=comp('PRINT_03');cradle=comp('PRINT_14');face=comp('PRINT_11')
 # Ring-lug/crimp envelopes replace the internal washer at the same stack level.
 for i,x,y,dx,dy in [(1,-100,0,1,0),(2,40,0,0,-1),(3,-30,-55,0,1),(4,-30,55,0,-1)]:
  c=comp('ELECTRODE_E'+str(i));b=c.bRepBodies.itemByName('Internal_washer')
  if dx: tongue=box(x+2,y-2,10,x+10,y+2,11)
  elif dy>0:tongue=box(x-2,y+2,10,x+2,y+10,11)
  else:tongue=box(x-2,y-10,10,x+2,y-2,11)
  barrel=m.createCylinderOrCone(P(x+dx*7,y+dy*7,12.2),.22,P(x+dx*15,y+dy*15,12.2),.22)
  union(tongue,barrel);modify(c,tongue,'RevB2_E%d_ring_lug_and_crimp'%i,True,b)
  b.name='M4_ring_lug_1mm_with_D4_4_crimp_ENVELOPE_VERIFY'
 # Open E2 sideways; retain the existing round bolt/nut relief and top bridge.
 modify(cradle,box(34,-24,9.8,46,-2,16),'RevB2_E2_side_wire_exit_12x6_2')
 # Common sensor-wire riser, separate from propulsion and the battery straps.
 modify(tray,box(-28,-27,15,-22,-19,20),'RevB2_sensor_riser_6x8')
 # Screw mount lugs: raised hull bosses, dry blind pilots, clearance in upper part.
 for c,pre,x,ys in [(cradle,'cradle',26,[-23,23]),(face,'face_mount',60,[-27,27])]:
  for y in ys:
   lo,hi=(y-4,-17) if y<0 else (17,y+4)
   lug=box(x-4,lo,9,x+4,hi,12)
   modify(c,lug,'RevB2_'+pre+'_lug_'+str(y),True)
   modify(hull,cyl(x,y,3,9,8),'RevB2_'+pre+'_hull_boss_'+str(y),True)
   modify(hull,cyl(x,y,3.8,9.1,2.5),'RevB2_'+pre+'_M3_blind_pilot_'+str(y))
   modify(c,cyl(x,y,8.9,50,3.4),'RevB2_'+pre+'_M3_clearance_'+str(y))
   modify(tray,box(x-5,y-5,15,x+5,y+5,20),'RevB2_'+pre+'_tray_access_'+str(y))
 # Four screw-secured capture bridges. Positive capture with 0.5 mm nominal top
 # clearance avoids using screw torque to press on unknown electronic components.
 cages=[('PRINT_18_ESP32_capture_bridge',-28,42,50.5,58.5,36.1,39.1,-20.5,34.8,[-24,38]),
        ('PRINT_19_Front_end_capture_bridge',-28,28,-49,-41,36.5,39.5,-20.5,20.5,[-24,24]),
        ('PRINT_20_Regulator_capture_bridge',53,74,52.5,60.5,28.316,31.316,56.5,70.2,[57,70]),
        ('PRINT_21_ESC_capture_bridge',84,134,38,46,36.5,39.5,91.5,126.5,[88,130])]
 # Regulator uses a transverse bridge outside the long board sides instead.
 cages.pop(2)
 for name,x0,x1,y0,y1,zunder,ztop,inner0,inner1,centers in cages:
  body=box(x0,y0,zunder,x1,y1,ztop)
  union(body,box(x0,y0,23,inner0,y1,zunder+.1))
  union(body,box(inner1,y0,23,x1,y1,zunder+.1))
  yc=(y0+y1)/2
  for x in centers:
   modify(tray,box(x-4,y0,19,x+4,y1,23),'RevB2_'+name+'_pedestal_'+str(x),True)
   modify(tray,cyl(x,yc,17,23.1,2.5),'RevB2_'+name+'_M3_pilot_'+str(x))
   cut(body,cyl(x,yc,22.9,ztop+.1,3.4))
  new(name,body)
 # Regulator capture: legs beyond Y ends; entire 12.7x17.78 proxy retained.
 body=box(59.5,26,28.316,67.5,59.78,31.316)
 union(body,box(59.5,26,23,67.5,33.5,28.416))
 union(body,box(59.5,52.28,23,67.5,59.78,28.416))
 for y in [30,55.78]:
  modify(tray,box(59.5,y-4,19,67.5,y+4,23),'RevB2_regulator_pedestal_'+str(y),True)
  modify(tray,cyl(63.5,y,17,23.1,2.5),'RevB2_regulator_M3_pilot_'+str(y))
  cut(body,cyl(63.5,y,22.9,31.5,3.4))
 new('PRINT_20_Regulator_capture_bridge',body)
 # ADC: change existing M2 clearance bores to printed M2 pilots, leaving PCB unchanged.
 for x in [37.54,57.86]:
  for y in [-37.76,-50.46]:
   modify(tray,cyl(x,y,16,24,2.22),'RevB2_ADC_fill_old_clearance',True)
   modify(tray,cyl(x,y,17,24.1,1.7),'RevB2_ADC_M2_blind_pilot')
 # Servo factory-size ears: two M2 pilot holes replacing open adjustment slots.
 for x in [127,156]:
  modify(tray,box(x-1.51,-42.01,19,x+1.51,-35.99,43),'RevB2_servo_slot_fill',True)
  modify(tray,cyl(x,-39,35,43.1,1.7),'RevB2_servo_M2_pilot')
  servo=comp('SERVO_');ear=servo.bRepBodies.itemByName('Mount_lugs_VERIFY')
  modify(servo,cyl(x,-39,42.9,45.6,2.2),'RevB2_servo_factory_hole_ENVELOPE_VERIFY',False,ear)
 # Rail-to-deck blind M3 fasteners, countersunk flush below the pod shoe.
 rail=comp('PRINT_06')
 for x in [-108,-98]:
  modify(hull,cyl(x,0,60,66,10),'RevB2_rail_internal_boss',True)
  modify(hull,cyl(x,0,60.8,68.1,2.5),'RevB2_rail_M3_blind_pilot')
  hole=cyl(x,0,67.9,72.1,3.4)
  union(hole,m.createCylinderOrCone(P(x,0,70.5),.17,P(x,0,72),.32))
  modify(rail,hole,'RevB2_rail_M3_flush_clearance')
 # Rudder bracket: four horizontal screws into dry internal backing pads.
 bracket=comp('PRINT_09')
 for y in [-9,9]:
  modify(hull,box(190,y-4,46,196.8,y+4,62),'RevB2_transom_internal_backing',True)
  for z in [50,58]:
   tool=m.createCylinderOrCone(P(190.8,y,z),.125,P(202,y,z),.125)
   modify(hull,tool,'RevB2_transom_M3_blind_pilot')
   tool=m.createCylinderOrCone(P(194,y,z),.17,P(210,y,z),.17)
   modify(bracket,tool,'RevB2_transom_M3_clearance')
 # Static locating stops constrain lengthwise sliding within the capture bridges.
 for bounds in [(-18,28,19,-12,29.5,26),(-18,58.44,19,-12,60.44,26),
                (-4,-60.5,19,4,-58.5,26),(-4,-27.5,19,4,-25.5,26),
                (55,40,19,56.5,46,25),(70.2,40,19,71.7,46,25),
                (100,27.5,19,106,29.5,25),(100,54.5,19,106,56.5,25)]:
  modify(tray,box(*bounds),'RevB2_device_edge_stop',True)
 assert d.computeAll()
 for c in [hull,tray,cradle,face,rail,bracket]:assert c.bRepBodies.count==1,(c.name,c.bRepBodies.count)
 print(json.dumps({'timeline':d.timeline.count,'status':'interfaces applied; run collision audit before exporting'}))
