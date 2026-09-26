"""Connect each recessed conductor groove to its terminal potting pocket."""
import adsk.core, adsk.fusion, os, json
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run(_context: str):
    app = adsk.core.Application.get()
    d = adsk.fusion.Design.cast(app.activeProduct)
    root = d.rootComponent
    assert d.timeline.count == 1515
    manager = adsk.fusion.TemporaryBRepManager.get()
    for label, x, sign in [('E4', 90, 1), ('E3', -75, 1), ('E2', 90, -1), ('E1', -75, -1)]:
        rotation = next(d.timeline.item(i) for i in range(d.timeline.count) if d.timeline.item(i).name == 'RevC_' + label + '_angle_driven_rotation')
        assert rotation.rollTo(True)
        comp = next(o.component for o in root.occurrences if o.name.startswith('PROBE_' + label + '_MOVING'))
        target = next(b for b in comp.bRepBodies if b.name.startswith('PRINT_'))
        center = adsk.core.Point3D.create((x + 129.5) / 10, sign * 74.2 / 10, -18 / 10)
        bounds = adsk.core.OrientedBoundingBox3D.create(center, adsk.core.Vector3D.create(1, 0, 0), adsk.core.Vector3D.create(0, 1, 0), .54, .26, .30)
        tool = manager.createBox(bounds)
        base = comp.features.baseFeatures.add()
        base.name = 'RevC_' + label + '_groove_connection_tool'
        assert base.startEdit()
        comp.bRepBodies.add(tool, base)
        assert base.finishEdit()
        collection = adsk.core.ObjectCollection.create()
        collection.add(base.bodies.item(0))
        inputs = comp.features.combineFeatures.createInput(target, collection)
        inputs.operation = adsk.fusion.FeatureOperations.CutFeatureOperation
        comp.features.combineFeatures.add(inputs).name = 'RevC_' + label + '_groove_to_terminal_pocket'
        assert d.timeline.moveToEnd()
    assert d.computeAll()
    result = {'revision': 'Rev-C.1', 'timeline': d.timeline.count, 'fixes': ['Connect the four wire grooves to the terminal potting pockets before their parametric rotations'], 'assembly_release_passed': False}
    with open(os.path.join(BASE, 'verification', 'RevC_Arm_Finish.json'), 'w') as f:
        json.dump(result, f, indent=2)
    print(json.dumps(result))
