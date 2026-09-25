import adsk.core,adsk.fusion,math,json
def run(_context: str):
 a=adsk.core.Application.get();d=adsk.fusion.Design.cast(a.activeProduct)
 c=next(o.component for o in d.rootComponent.allOccurrences if o.name.startswith('PRINT_01'))
 s=c.sketches.itemByName('RevB2_IoT_Beyond_Lab_side_branding');assert s.sketchTexts.count==0
 inp=s.sketchTexts.createInput3("'IoT Beyond Lab'",adsk.core.ValueInput.createByString('12 mm'))
 inp.fontName='Arial';inp.textStyle=adsk.fusion.TextStyles.TextStyleBold
 assert inp.setAsMultiLine(adsk.core.Point3D.create(-13.9,1.8,0),adsk.core.Point3D.create(2.1,3.2,0),adsk.core.HorizontalAlignments.CenterHorizontalAlignment,adsk.core.VerticalAlignments.MiddleVerticalAlignment,0)
 t=s.sketchTexts.add(inp);assert t.definition.rotate(math.pi/2)
 f=c.features.extrudeFeatures.addSimple(t,adsk.core.ValueInput.createByString('0.6 mm'),adsk.fusion.FeatureOperations.JoinFeatureOperation)
 f.name='RevB2_IoT_Beyond_Lab_raised_0_6mm';s.isVisible=False
 assert c.bRepBodies.count==1
 a.activeViewport.fit();a.activeViewport.saveAsImageFile(r'C:/Users/jhbryan/Documents/Codex/2026-09-25/https-github-com-jhbryan0817-del-energized/work/after_brand.png',1600,1000)
 print('Branding joined to hull; timeline',d.timeline.count)
