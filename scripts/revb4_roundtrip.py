import adsk.core,adsk.fusion,json,os
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def run(_context: str):
 a=adsk.core.Application.get();original=a.activeDocument
 def inventory(d):
  return {o.fullPathName+'/'+b.name:round(b.volume*1000,5) for o in d.rootComponent.allOccurrences if not o.name.startswith(('DATUM','REFERENCE','OPTION','CLEARANCES')) for b in o.bRepBodies if b.isSolid}
 d=adsk.fusion.Design.cast(a.activeProduct);expected=inventory(d);timeline=d.timeline.count;params=d.userParameters.count
 options=a.importManager.createFusionArchiveImportOptions(os.path.join(BASE,'cad','Energized_Water_Scanner_RevB4.f3d'))
 doc=a.importManager.importToNewDocument(options);assert doc
 reopened=adsk.fusion.Design.cast(a.activeProduct)
 actual=inventory(reopened)
 issues=[{'index':i,'name':reopened.timeline.item(i).name,'message':reopened.timeline.item(i).errorOrWarningMessage} for i in range(reopened.timeline.count) if reopened.timeline.item(i).healthState in (adsk.fusion.FeatureHealthStates.WarningFeatureHealthState,adsk.fusion.FeatureHealthStates.ErrorFeatureHealthState)]
 result={'revision':'Rev-B.4','timeline_items':reopened.timeline.count,'parameters':reopened.userParameters.count,'body_count':len(actual),'feature_errors_and_warnings':issues,'all_body_volumes_match':actual==expected,'passed':actual==expected and reopened.timeline.count==timeline and reopened.userParameters.count==params and not issues}
 with open(os.path.join(BASE,'verification','RevB4_Native_Roundtrip.json'),'w') as f:json.dump(result,f,indent=2)
 assert result['passed'],result
 doc.close(False);original.activate()
 assert original.save('Rev-B.4: supplier interface audit; regulator pin-row access and M4 nut corner envelopes; remaining hardware gates documented')
 print(json.dumps(result));print('Original cloud design saved')
