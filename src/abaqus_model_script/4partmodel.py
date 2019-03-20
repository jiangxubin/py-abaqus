# -*- coding: mbcs -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(0.0, 15.0))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(0.0, 20.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(48.5, 20.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(48.5, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(15.5, -3.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(15.0, -3.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(15.5, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(15.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 20.0), point2=(
    0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 10.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 10.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(
    15.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.5, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.5, 0.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 10.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.5, 0.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 10.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    7.5, 0.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(15.0, 0.0), point2=(
    15.0, -3.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.0, -1.5))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.0, -1.5), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.5, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.0, -1.5))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.5, 0.0), )
    , entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    15.0, -1.5), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(15.0, -3.0), point2=
    (15.5, -3.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.25, -3.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.25, 
    -3.0), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.0, -1.5))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.25, -3.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.0, -1.5), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    15.25, -3.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(15.5, -3.0), point2=
    (15.5, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.5, -1.5))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.5, -1.5), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.25, -3.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.5, -1.5))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.25, 
    -3.0), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.5, -1.5), 
    ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(15.5, 0.0), point2=(
    48.5, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((32.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((32.0, 0.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.5, -1.5))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((32.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.5, -1.5), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    32.0, 0.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(48.5, 0.0), point2=(
    48.5, 20.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((48.5, 10.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((48.5, 10.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((32.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((48.5, 10.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((32.0, 0.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    48.5, 10.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(48.5, 20.0), point2=
    (0.0, 20.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((24.25, 20.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((24.25, 
    20.0), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((48.5, 10.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((24.25, 20.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((48.5, 10.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    24.25, 20.0), ))
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='soil', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['soil'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=2.68, name='__profile__', 
    sheetSize=107.35, transform=
    mdb.models['Model-1'].parts['soil'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['soil'].faces.findAt((37.5, 
    6.666667, 0.0), (0.0, 0.0, 1.0)), sketchPlaneSide=SIDE1, 
    sketchOrientation=RIGHT, origin=(24.236104, 9.982244, 0.0)))
mdb.models['Model-1'].parts['soil'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-5.75, 10.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-5.75, 2.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-24.25, 2.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-24.25, 2.0), 
    point2=(-5.75, 2.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-15.0, 2.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-15.0, 2.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-5.75, 2.0), point2=
    (-5.75, 10.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-5.75, 6.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-5.75, 6.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-15.0, 2.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-5.75, 6.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-15.0, 2.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    -5.75, 6.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-9.236104, 
    -9.982244), point2=(-9.236104, 2.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.236104, 
    -3.991122))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.236104, 
    -3.991122), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-16.736104, 
    -9.982244))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.236104, 
    -3.991122))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-16.736104, 
    -9.982244), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.236104, 
    -3.991122), ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-9.236104, 2.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-15.0, 2.0))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-9.236104, 
    2.0), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-15.0, 2.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-8.736104, 
    -9.982244), point2=(-8.736104, 2.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-8.736104, 
    -3.991122))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-8.736104, 
    -3.991122), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-8.736104, 
    -11.482244))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-8.736104, 
    -3.991122))
mdb.models['Model-1'].sketches['__profile__'].ParallelConstraint(addUndoState=
    False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-8.736104, 
    -11.482244), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-8.736104, 
    -3.991122), ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-8.736104, 2.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-15.0, 2.0))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-8.736104, 
    2.0), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-15.0, 2.0), 
    ))
mdb.models['Model-1'].parts['soil'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['soil'].faces.findAt(((37.5, 6.666667, 0.0), ))
    , sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(17.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(17.0, 1.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(17.0, 1.0), point2=(
    17.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((17.0, 0.5))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((17.0, 0.5), 
    ))
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='crack', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['crack'].BaseWire(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].Material(name='soil')
mdb.models['Model-1'].materials['soil'].Density(table=((1616.0, ), ))
mdb.models['Model-1'].materials['soil'].Elastic(table=((6000000.0, 0.3), ))
mdb.models['Model-1'].materials['soil'].MaxpsDamageInitiation(table=((20000.0, 
    ), ))
mdb.models['Model-1'].materials['soil'].maxpsDamageInitiation.DamageEvolution(
    mixedModeBehavior=POWER_LAW, power=1.0, table=((10000.0, 10000.0, 10000.0), 
    ), type=ENERGY)
mdb.models['Model-1'].materials['soil'].maxpsDamageInitiation.DamageStabilizationCohesive(
    cohesiveCoeff=0.0001)
mdb.models['Model-1'].materials['soil'].GapFlow(table=((1e-06, ), ))
mdb.models['Model-1'].materials['soil'].FluidLeakoff(table=((5.879e-16, 
    5.879e-16), ))
mdb.models['Model-1'].materials['soil'].Permeability(inertialDragCoefficient=
    0.142887, specificWeight=10000.0, table=((2.418e-05, 0.0), ))
mdb.models['Model-1'].Material(name='pile')
mdb.models['Model-1'].materials['pile'].Density(table=((1616.0, ), ))
mdb.models['Model-1'].materials['pile'].Elastic(table=((90000000000.0, 0.1), ))
mdb.models['Model-1'].HomogeneousSolidSection(material='soil', name='soil', 
    thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='pile', name='pile', 
    thickness=None)
mdb.models['Model-1'].parts['soil'].Set(faces=
    mdb.models['Model-1'].parts['soil'].faces.findAt(((10.0, 7.988162, 0.0), ), 
    ((16.495368, 7.988162, 0.0), ), ), name='clay')
mdb.models['Model-1'].parts['soil'].Set(faces=
    mdb.models['Model-1'].parts['soil'].faces.findAt(((15.333333, 7.988162, 
    0.0), )), name='pile')
mdb.models['Model-1'].materials.changeKey(fromName='soil', toName='clay')
mdb.models['Model-1'].sections.changeKey(fromName='soil', toName='clay')
mdb.models['Model-1'].sections['clay'].setValues(material='clay', thickness=
    None)
mdb.models['Model-1'].parts['soil'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['soil'].sets['clay'], sectionName='clay', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['soil'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['soil'].sets['pile'], sectionName='pile', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='crack-1', part=
    mdb.models['Model-1'].parts['crack'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='soil-1', part=
    mdb.models['Model-1'].parts['soil'])
mdb.models['Model-1'].GeostaticStep(name='gravity', previous='Initial')
mdb.models['Model-1'].StaticStep(name='pile_bc', previous='gravity')
mdb.models['Model-1'].SoilsStep(cetol=None, creep=OFF, end=None, name=
    'excavation', previous='pile_bc', utol=1000000000.0)
mdb.models['Model-1'].SoilsStep(cetol=None, creep=OFF, end=None, initialInc=
    0.05, maxInc=100.0, minInc=1e-12, name='injection', previous='excavation', 
    timePeriod=100.0, utol=1000000000.0)
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
    'S', 'LE', 'U', 'RF', 'CF', 'CSTRESS', 'CDISP', 'PHILSM', 'PSILSM', 
    'VOIDR', 'SAT', 'POR'))
mdb.models['Model-1'].parts['soil'].Set(edges=
    mdb.models['Model-1'].parts['soil'].edges.findAt(((15.0, 2.995561, 0.0), ), 
    ((15.5, 2.995561, 0.0), ), ), name='pile_surf')
mdb.models['Model-1'].parts['soil'].Set(edges=
    mdb.models['Model-1'].parts['soil'].edges.findAt(((15.0, 2.995561, 0.0), ), 
    ((15.5, 2.995561, 0.0), ), ), name='clay_surf')
mdb.models['Model-1'].parts['soil'].Set(edges=
    mdb.models['Model-1'].parts['soil'].edges.findAt(((15.0, 2.995561, 0.0), ), 
    ((15.5, 2.995561, 0.0), ), ), name='clay_surf')
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].rootAssembly.deleteFeatures(('crack-1', 'soil-1'))
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='crack-1', part=
    mdb.models['Model-1'].parts['crack'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='soil-1', part=
    mdb.models['Model-1'].parts['soil'])
mdb.models['Model-1'].rootAssembly.deleteFeatures(('crack-1', 'soil-1'))
mdb.models['Model-1'].parts['soil'].Set(edges=
    mdb.models['Model-1'].parts['soil'].edges.findAt(((15.0, -0.75, 0.0), ), ((
    15.5, -2.25, 0.0), ), ), name='pile_no_int_lateral')
mdb.models['Model-1'].parts['soil'].Set(edges=
    mdb.models['Model-1'].parts['soil'].edges.findAt(((15.125, -3.0, 0.0), )), 
    name='pile_no_int_bottom')
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='crack-1', part=
    mdb.models['Model-1'].parts['crack'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='soil-1', part=
    mdb.models['Model-1'].parts['soil'])
mdb.models['Model-1'].parts['crack'].Set(edges=
    mdb.models['Model-1'].parts['crack'].edges.findAt(((17.0, 0.75, 0.0), )), 
    name='crack')
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].rootAssembly.deleteFeatures(('crack-1', 'soil-1'))
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='crack-1', part=
    mdb.models['Model-1'].parts['crack'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='soil-1', part=
    mdb.models['Model-1'].parts['soil'])
mdb.models['Model-1'].rootAssembly.engineeringFeatures.XFEMCrack(crackDomain=
    mdb.models['Model-1'].rootAssembly.instances['soil-1'].sets['clay'], 
    crackLocation=
    mdb.models['Model-1'].rootAssembly.instances['crack-1'].sets['crack'], 
    name='Crack-1')
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=2.68, name='__profile__', 
    sheetSize=107.35, transform=
    mdb.models['Model-1'].parts['soil'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['soil'].faces.findAt((16.495368, 
    7.988162, 0.0), (0.0, 0.0, 1.0)), sketchPlaneSide=SIDE1, 
    sketchOrientation=RIGHT, origin=(28.157377, 10.949345, 0.0)))
mdb.models['Model-1'].parts['soil'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-9.671273, 9.032899)
    , point2=(-9.671273, 1.032899))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.671273, 
    1.432899))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.671273, 
    1.432899), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.671273, 
    8.632899))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.671273, 
    1.432899))
mdb.models['Model-1'].sketches['__profile__'].ParallelConstraint(addUndoState=
    False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.671273, 
    8.632899), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.671273, 
    1.432899), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-9.671273, 1.032899)
    , point2=(-28.157377, 1.032899))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-27.233072, 
    1.032899))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-27.233072, 
    1.032899), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.671273, 
    1.432899))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-27.233072, 
    1.032899))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.671273, 
    1.432899), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-27.233072, 
    1.032899), ))
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(48.5, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(0.0, 20.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(15.5, -3.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(15.0, -3.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(48.5, 20.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 20.0), point2=(
    0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 10.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 10.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(15.5, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(15.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(
    15.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.5, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.5, 0.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(15.0, 0.0), point2=(
    15.0, -3.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.0, -1.5))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.0, -1.5), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.5, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.0, -1.5))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.5, 0.0), )
    , entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    15.0, -1.5), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(15.0, -3.0), point2=
    (15.5, -3.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.25, -3.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.25, 
    -3.0), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.0, -1.5))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.25, -3.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.0, -1.5), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    15.25, -3.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(15.5, -3.0), point2=
    (15.5, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.5, -1.5))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.5, -1.5), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.25, -3.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.5, -1.5))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.25, 
    -3.0), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.5, -1.5), 
    ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(15.5, 0.0), point2=(
    48.5, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((32.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((32.0, 0.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.5, -1.5))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((32.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.5, -1.5), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    32.0, 0.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(48.5, 0.0), point2=(
    48.5, 20.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((48.5, 10.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((48.5, 10.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((32.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((48.5, 10.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((32.0, 0.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    48.5, 10.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(48.5, 20.0), point2=
    (0.0, 20.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((24.25, 20.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((24.25, 
    20.0), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((48.5, 10.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((24.25, 20.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((48.5, 10.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    24.25, 20.0), ))
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='soil', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['soil'].BaseWire(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
del mdb.models['Model-1'].parts['soil']
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(0.0, 20.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(15.5, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(15.5, -3.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(15.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(15.0, -3.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(48.5, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(48.5, 20.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 20.0), point2=(
    0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 10.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 10.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(
    15.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.5, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.5, 0.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 10.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.5, 0.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 10.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    7.5, 0.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(15.0, 0.0), point2=(
    15.0, -3.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.0, -1.5))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.0, -1.5), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.5, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.0, -1.5))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.5, 0.0), )
    , entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    15.0, -1.5), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(15.0, -3.0), point2=
    (15.5, -3.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.25, -3.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.25, 
    -3.0), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.0, -1.5))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.25, -3.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.0, -1.5), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    15.25, -3.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(15.5, -3.0), point2=
    (15.5, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.5, -1.5))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.5, -1.5), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.25, -3.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.5, -1.5))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.25, 
    -3.0), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.5, -1.5), 
    ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(15.5, 0.0), point2=(
    48.5, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((32.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((32.0, 0.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.5, -1.5))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((32.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.5, -1.5), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    32.0, 0.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(48.5, 0.0), point2=(
    48.5, 20.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((48.5, 10.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((48.5, 10.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((32.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((48.5, 10.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((32.0, 0.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    48.5, 10.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(48.5, 20.0), point2=
    (0.0, 20.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((24.25, 20.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((24.25, 
    20.0), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((48.5, 10.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((24.25, 20.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((48.5, 10.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    24.25, 20.0), ))
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='soil', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['soil'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=2.68, name='__profile__', 
    sheetSize=107.35, transform=
    mdb.models['Model-1'].parts['soil'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['soil'].faces.findAt((37.5, 
    6.666667, 0.0), (0.0, 0.0, 1.0)), sketchPlaneSide=SIDE1, 
    sketchOrientation=RIGHT, origin=(24.236104, 9.982244, 0.0)))
mdb.models['Model-1'].parts['soil'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-5.75, 10.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-5.75, 2.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-5.75, 10.0), 
    point2=(-5.75, 2.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-5.75, 6.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-5.75, 6.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-5.75, 2.0), point2=
    (-24.2361039999471, 2.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-14.993052, 
    2.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-14.993052, 
    2.0), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-5.75, 6.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-14.993052, 
    2.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-5.75, 6.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    -14.993052, 2.0), ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-24.236104, 
    2.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-24.236104, 
    0.017756))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
    -24.2361039999471, 2.0), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-24.236104, 
    0.017756), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-8.736104, 
    -9.982244), point2=(-8.736104, 2.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-8.736104, 
    -3.991122))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-8.736104, 
    -3.991122), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-8.736104, 
    -11.482244))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-8.736104, 
    -3.991122))
mdb.models['Model-1'].sketches['__profile__'].ParallelConstraint(addUndoState=
    False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-8.736104, 
    -11.482244), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-8.736104, 
    -3.991122), ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-8.736104, 2.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-14.993052, 
    2.0))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-8.736104, 
    2.0), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-14.993052, 
    2.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-9.236104, 
    -9.982244), point2=(-9.236104, 2.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.236104, 
    -3.991122))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.236104, 
    -3.991122), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-16.736104, 
    -9.982244))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.236104, 
    -3.991122))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-16.736104, 
    -9.982244), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.236104, 
    -3.991122), ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-9.236104, 2.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-14.993052, 
    2.0))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-9.236104, 
    2.0), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-14.993052, 
    2.0), ))
mdb.models['Model-1'].parts['soil'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['soil'].faces.findAt(((37.5, 6.666667, 0.0), ))
    , sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
del mdb.models['Model-1'].parts['soil'].features['Partition face-1']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=2.68, name='__profile__', 
    sheetSize=107.35, transform=
    mdb.models['Model-1'].parts['soil'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['soil'].faces.findAt((37.5, 
    6.666667, 0.0), (0.0, 0.0, 1.0)), sketchPlaneSide=SIDE1, 
    sketchOrientation=RIGHT, origin=(24.236104, 9.982244, 0.0)))
mdb.models['Model-1'].parts['soil'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-5.75, 10.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-5.75, 2.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-24.25, 10.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-24.25, 2.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-24.25, 2.0), 
    point2=(-5.75, 2.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-15.0, 2.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-15.0, 2.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-5.75, 2.0), point2=
    (-5.75, 10.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-5.75, 6.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-5.75, 6.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-15.0, 2.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-5.75, 6.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-15.0, 2.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    -5.75, 6.0), ))
mdb.models['Model-1'].parts['soil'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['soil'].faces.findAt(((37.5, 6.666667, 0.0), ))
    , sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=2.68, name='__profile__', 
    sheetSize=107.35, transform=
    mdb.models['Model-1'].parts['soil'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['soil'].faces.findAt((37.5, 
    6.666667, 0.0), (0.0, 0.0, 1.0)), sketchPlaneSide=SIDE1, 
    sketchOrientation=RIGHT, origin=(24.236104, 9.982244, 0.0)))
mdb.models['Model-1'].parts['soil'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-8.736104, 
    -9.982244), point2=(-8.736104, 2.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-8.736104, 
    -3.991122))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-8.736104, 
    -3.991122), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-8.736104, 
    -11.482244))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-8.736104, 
    -3.991122))
mdb.models['Model-1'].sketches['__profile__'].ParallelConstraint(addUndoState=
    False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-8.736104, 
    -11.482244), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-8.736104, 
    -3.991122), ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-8.736104, 2.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-6.674305, 2.0))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-8.736104, 
    2.0), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-6.674305, 
    2.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-9.236104, 
    -9.982244), point2=(-9.236104, 2.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.236104, 
    -3.991122))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.236104, 
    -3.991122), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-16.736104, 
    -9.982244))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.236104, 
    -3.991122))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-16.736104, 
    -9.982244), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.236104, 
    -3.991122), ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-9.236104, 2.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-6.674305, 2.0))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-9.236104, 
    2.0), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-6.674305, 
    2.0), ))
mdb.models['Model-1'].parts['soil'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['soil'].faces.findAt(((37.5, 6.666667, 0.0), ))
    , sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=2.68, name='__profile__', 
    sheetSize=107.35, transform=
    mdb.models['Model-1'].parts['soil'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['soil'].faces.findAt((16.495368, 
    7.988162, 0.0), (0.0, 0.0, 1.0)), sketchPlaneSide=SIDE1, 
    sketchOrientation=RIGHT, origin=(28.157377, 10.949345, 0.0)))
mdb.models['Model-1'].parts['soil'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-9.671273, 1.032899)
    , point2=(-9.671273, -10.9493450000441))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.671273, 
    -4.958223))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.671273, 
    -4.958223), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.820578, 
    1.032899))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.671273, 
    -4.958223))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.820578, 
    1.032899), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.671273, 
    -4.958223), ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-9.671273, 
    -10.949345))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((3.842623, 
    -10.949345))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-9.671273, 
    -10.9493450000441), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((3.842623, 
    -10.949345), ))
mdb.models['Model-1'].parts['soil'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['soil'].faces.findAt(((16.495368, 7.988162, 
    0.0), )), sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=2.62, name='__profile__', 
    sheetSize=104.92, transform=
    mdb.models['Model-1'].parts['soil'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['soil'].faces.findAt((28.490735, 
    3.994081, 0.0), (0.0, 0.0, 1.0)), sketchPlaneSide=SIDE1, 
    sketchOrientation=RIGHT, origin=(28.691064, 11.186363, 0.0)))
mdb.models['Model-1'].parts['soil'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-13.191064, 
    0.795881), point2=(-13.191064, 8.81363700002147))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-13.191064, 
    4.804759))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-13.191064, 
    4.804759), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-13.041759, 
    0.795881))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-13.191064, 
    4.804759))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-13.041759, 
    0.795881), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-13.191064, 
    4.804759), ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-13.191064, 
    8.813637))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-4.441064, 
    8.813637))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-13.191064, 
    8.81363700002147), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-4.441064, 
    8.813637), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-13.691064, 
    0.795881), point2=(-13.691064, 8.81363700002147))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-13.691064, 
    4.804759))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-13.691064, 
    4.804759), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-13.691064, 
    0.196769))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-13.691064, 
    4.804759))
mdb.models['Model-1'].sketches['__profile__'].ParallelConstraint(addUndoState=
    False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-13.691064, 
    0.196769), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-13.691064, 
    4.804759), ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-13.691064, 
    8.813637))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-4.441064, 
    8.813637))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-13.691064, 
    8.81363700002147), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-4.441064, 
    8.813637), ))
mdb.models['Model-1'].parts['soil'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['soil'].faces.findAt(((28.490735, 3.994081, 
    0.0), )), sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
del mdb.models['Model-1'].parts['soil'].features['Partition face-4']
del mdb.models['Model-1'].parts['soil'].features['Partition face-3']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=2.68, name='__profile__', 
    sheetSize=107.35, transform=
    mdb.models['Model-1'].parts['soil'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['soil'].faces.findAt((16.495368, 
    7.988162, 0.0), (0.0, 0.0, 1.0)), sketchPlaneSide=SIDE1, 
    sketchOrientation=RIGHT, origin=(28.157377, 10.949345, 0.0)))
mdb.models['Model-1'].parts['soil'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-9.671273, 1.032899)
    , point2=(20.3426230000166, 1.032899))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((5.335675, 
    1.032899))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((5.335675, 
    1.032899), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.820578, 
    1.032899))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((5.335675, 
    1.032899))
mdb.models['Model-1'].sketches['__profile__'].ParallelConstraint(addUndoState=
    False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.820578, 
    1.032899), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((5.335675, 
    1.032899), ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((20.342623, 
    1.032899))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.342623, 
    -0.949345))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
    20.3426230000166, 1.032899), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.342623, 
    -0.949345), ))
mdb.models['Model-1'].parts['soil'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['soil'].faces.findAt(((16.495368, 7.988162, 
    0.0), )), sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=2.62, name='__profile__', 
    sheetSize=104.92, transform=
    mdb.models['Model-1'].parts['soil'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['soil'].faces.findAt((28.490735, 
    14.648911, 0.0), (0.0, 0.0, 1.0)), sketchPlaneSide=SIDE1, 
    sketchOrientation=RIGHT, origin=(24.25, 15.991122, 0.0)))
mdb.models['Model-1'].parts['soil'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-5.763896, 
    3.911122))
mdb.models['Model-1'].sketches['__profile__'].copyMove(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-5.763896, 
    3.911122), ), ), vector=(0.5, 0.0))
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=2.62, name='__profile__', 
    sheetSize=104.92, transform=
    mdb.models['Model-1'].parts['soil'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['soil'].faces.findAt((16.495368, 
    7.988162, 0.0), (0.0, 0.0, 1.0)), sketchPlaneSide=SIDE1, 
    sketchOrientation=RIGHT, origin=(28.157377, 10.949345, 0.0)))
mdb.models['Model-1'].parts['soil'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-5.25, 10.0))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-5.25, 11.5))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-5.25, 11.5))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.671273, 
    8.952899))
mdb.models['Model-1'].sketches['__profile__'].copyMove(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.671273, 
    8.952899), ), ), vector=(0.5, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.171273, 
    5.032899))
mdb.models['Model-1'].sketches['__profile__'].move(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.171273, 
    5.032899), ), ), vector=(0.001273, -5.617899))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-9.671273, 1.032899)
    , point2=(-9.67127299999996, -4.58499999998137))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.671273, 
    -1.77605))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.671273, 
    -1.77605), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.820578, 
    1.032899))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.671273, 
    -1.77605))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.820578, 
    1.032899), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.671273, 
    -1.77605), ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-9.671273, 
    1.032899))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-9.671273, 
    -4.585))
mdb.models['Model-1'].sketches['__profile__'].ObliqueDimension(textPoint=(
    -7.68725561633301, -3.17979181549072), value=7.0, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-9.671273, 
    1.032899), ), vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
    -9.67127299999996, -4.58499999998137), ))
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].dimensions[0], ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-9.67127299999996, 
    -5.967101), point2=(-7.86, -5.96710099999998))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-8.765636, 
    -5.967101))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-8.765636, 
    -5.967101), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.671273, 
    -2.467101))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-8.765636, 
    -5.967101))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.671273, 
    -2.467101), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-8.765636, 
    -5.967101), ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-9.671273, 
    -5.967101))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-7.86, 
    -5.967101))
mdb.models['Model-1'].sketches['__profile__'].ObliqueDimension(textPoint=(
    -8.62890028491211, -4.74688184997559), value=0.5, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
    -9.67127299999996, -5.967101), ), vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-7.86, 
    -5.96710099999998), ))
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].dimensions[1], ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-9.17127299999996, 
    -5.96710099999998), point2=(-9.17127299999996, 9.05065499995589))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.171273, 
    1.541777))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.171273, 
    1.541777), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.421273, 
    -5.967101))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.171273, 
    1.541777))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.421273, 
    -5.967101), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.171273, 
    1.541777), ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-9.171273, 
    9.050655))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-3.907377, 
    9.050655))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
    -9.17127299999996, 9.05065499995589), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-3.907377, 
    9.050655), ))
mdb.models['Model-1'].parts['soil'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['soil'].faces.findAt(((16.495368, 7.988162, 
    0.0), )), sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=2.62, name='__profile__', 
    sheetSize=104.92, transform=
    mdb.models['Model-1'].parts['soil'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['soil'].faces.findAt((17.490735, 
    9.64891, 0.0), (0.0, 0.0, 1.0)), sketchPlaneSide=SIDE1, 
    sketchOrientation=RIGHT, origin=(32.73008, 9.742034, 0.0)))
mdb.models['Model-1'].parts['soil'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-13.743976, 
    -4.75979), point2=(-13.743976, -9.74203400005587))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-13.743976, 
    -7.250912))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-13.743976, 
    -7.250912), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-13.768976, 
    -4.75979))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-13.743976, 
    -7.250912))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-13.768976, 
    -4.75979), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-13.743976, 
    -7.250912), ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-13.743976, 
    -9.742034))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-0.73008, 
    -9.742034))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-13.743976, 
    -9.74203400005587), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-0.73008, 
    -9.742034), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-14.243976, 
    -4.75979), point2=(-14.243976, -9.74203400005587))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-14.243976, 
    -7.250912))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-14.243976, 
    -7.250912), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-14.243976, 
    -4.40979))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-14.243976, 
    -7.250912))
mdb.models['Model-1'].sketches['__profile__'].ParallelConstraint(addUndoState=
    False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-14.243976, 
    -4.40979), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-14.243976, 
    -7.250912), ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-14.243976, 
    -9.742034))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-0.73008, 
    -9.742034))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-14.243976, 
    -9.74203400005587), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-0.73008, 
    -9.742034), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-13.743976, 
    -4.75979), point2=(15.769920000054, -4.75979))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((1.012972, 
    -4.75979))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((1.012972, 
    -4.75979), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-13.768976, 
    -4.75979))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((1.012972, 
    -4.75979))
mdb.models['Model-1'].sketches['__profile__'].ParallelConstraint(addUndoState=
    False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-13.768976, 
    -4.75979), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((1.012972, 
    -4.75979), ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((15.76992, 
    -4.75979))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.76992, 
    0.257966))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
    15.769920000054, -4.75979), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.76992, 
    0.257966), ))
mdb.models['Model-1'].parts['soil'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['soil'].faces.findAt(((17.490735, 9.64891, 
    0.0), )), sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=2.62, name='__profile__', 
    sheetSize=104.92, transform=
    mdb.models['Model-1'].parts['soil'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['soil'].faces.findAt((18.65277, 
    7.315577, 0.0), (0.0, 0.0, 1.0)), sketchPlaneSide=SIDE1, 
    sketchOrientation=RIGHT, origin=(9.700793, 15.822357, 0.0)))
mdb.models['Model-1'].parts['soil'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(8.785311, -3.840113)
    , point2=(9.28531099997801, -3.840113))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((9.035311, 
    -3.840113))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((9.035311, 
    -3.840113), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((8.785311, 
    -4.190113))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((9.035311, 
    -3.840113))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((8.785311, 
    -4.190113), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((9.035311, 
    -3.840113), ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((9.285311, 
    -3.840113))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((9.285311, 
    -10.089225))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
    9.28531099997801, -3.840113), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((9.285311, 
    -10.089225), ))

mdb.models['Model-1'].parts['soil'].deleteFeatures(('Partition face-3', 
    'Partition face-5'))
del mdb.models['Model-1'].parts['soil']
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(48.5, 20.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(48.5, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(0.0, 20.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(15.0, 12.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(15.5, 12.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(18.5, 20.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(19.0, 20.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(18.5, 5.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(19.0, 5.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(15.0, -3.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(15.5, -3.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(18.5, 20.0), point2=
    (18.5, 5.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((18.5, 12.5))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((18.5, 12.5), 
    ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(18.5, 5.0), point2=(
    19.0, 5.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((18.75, 5.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((18.75, 5.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((18.5, 12.5))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((18.75, 5.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((18.5, 12.5), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    18.75, 5.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(19.0, 5.0), point2=(
    19.0, 20.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((19.0, 12.5))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((19.0, 12.5), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((18.75, 5.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((19.0, 12.5))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((18.75, 5.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    19.0, 12.5), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(19.0, 20.0), point2=
    (18.5, 20.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((18.75, 20.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((18.75, 
    20.0), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((19.0, 12.5))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((18.75, 20.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((19.0, 12.5), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    18.75, 20.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(19.0, 20.0), point2=
    (48.5, 20.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((33.75, 20.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((33.75, 
    20.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(48.5, 20.0), point2=
    (48.5, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((48.5, 10.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((48.5, 10.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((33.75, 20.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((48.5, 10.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((33.75, 
    20.0), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((48.5, 10.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(15.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(15.5, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(48.5, 0.0), point2=(
    15.5, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((32.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((32.0, 0.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(15.5, 0.0), point2=(
    15.5, 12.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.5, 6.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.5, 6.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((32.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.5, 6.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((32.0, 0.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    15.5, 6.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(15.5, 12.0), point2=
    (18.5, 12.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((17.0, 12.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((17.0, 12.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.5, 6.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((17.0, 12.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.5, 6.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    17.0, 12.0), ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((18.5, 12.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((18.5, 12.5))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((18.5, 12.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    18.5, 12.5), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(15.5, 0.0), point2=(
    15.5, -3.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.5, -1.5))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.5, -1.5), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.5, -1.5))
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.5, -1.5), 
    ), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(15.5, 12.0), point2=
    (15.0, 12.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.25, 12.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.25, 
    12.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(15.0, 12.0), point2=
    (15.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.0, 6.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.0, 6.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.25, 12.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.0, 6.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.25, 
    12.0), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.0, 6.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(15.0, 0.0), point2=(
    0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.5, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.5, 0.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.0, 6.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.5, 0.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.0, 6.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    7.5, 0.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(
    0.0, 20.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 10.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 10.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.5, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 10.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.5, 0.0), )
    , entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    0.0, 10.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 20.0), point2=(
    18.5, 20.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((9.25, 20.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((9.25, 20.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 10.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((9.25, 20.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 10.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    9.25, 20.0), ))
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].constraints[82], ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((18.75, 20.0))
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((18.75, 
    20.0), ), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((17.0, 12.0))
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((17.0, 12.0), 
    ), ))
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='clay', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['clay'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(18.5, 20.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(19.0, 20.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(18.5, 5.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(19.0, 5.0))
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(18.5, 20.0), 
    point2=(19.0, 5.0))
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='wall', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['wall'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(15.0, 12.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(15.5, 12.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(15.0, -3.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(15.5, -3.0))
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(15.0, 12.0), 
    point2=(15.5, -3.0))
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='pile', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['pile'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['clay'].Set(faces=
    mdb.models['Model-1'].parts['clay'].faces.findAt(((11.166667, 17.333333, 
    0.0), )), name='clay')
mdb.models['Model-1'].parts['pile'].Set(faces=
    mdb.models['Model-1'].parts['pile'].faces.findAt(((15.333333, 7.0, 0.0), ))
    , name='pile')
mdb.models['Model-1'].parts['wall'].Set(faces=
    mdb.models['Model-1'].parts['wall'].faces.findAt(((18.833333, 15.0, 0.0), 
    )), name='wall')
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=2.62, name='__profile__', 
    sheetSize=104.92, transform=
    mdb.models['Model-1'].parts['clay'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['clay'].faces.findAt((11.166667, 
    17.333333, 0.0), (0.0, 0.0, 1.0)), sketchPlaneSide=SIDE1, 
    sketchOrientation=RIGHT, origin=(24.349582, 10.005489, 0.0)))
mdb.models['Model-1'].parts['clay'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-8.849582, 1.994511)
    , point2=(-5.84958199996854, 1.994511))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-7.349582, 
    1.994511))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-7.349582, 
    1.994511), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.099582, 
    1.994511))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-7.349582, 
    1.994511))
mdb.models['Model-1'].sketches['__profile__'].ParallelConstraint(addUndoState=
    False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.099582, 
    1.994511), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-7.349582, 
    1.994511), ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-5.849582, 
    1.994511))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-5.849582, 
    2.494511))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
    -5.84958199996854, 1.994511), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-5.849582, 
    2.494511), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-9.349582, 1.994511)
    , point2=(-24.3495819999685, 1.994511))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-16.849582, 
    1.994511))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-16.849582, 
    1.994511), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.349582, 
    -4.005489))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-16.849582, 
    1.994511))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.349582, 
    -4.005489), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-16.849582, 
    1.994511), ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-24.349582, 
    1.994511))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-24.349582, 
    -0.005489))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
    -24.3495819999685, 1.994511), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-24.349582, 
    -0.005489), ))
mdb.models['Model-1'].parts['clay'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['clay'].faces.findAt(((11.166667, 17.333333, 
    0.0), )), sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['clay'].Set(faces=
    mdb.models['Model-1'].parts['clay'].faces.findAt(((17.5, 14.666667, 0.0), 
    )), name='excavation')
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=1.37, name='__profile__', 
    sheetSize=55.17, transform=
    mdb.models['Model-1'].parts['wall'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['wall'].faces.findAt((18.833333, 
    15.0, 0.0), (0.0, 0.0, 1.0)), sketchPlaneSide=SIDE1, 
    sketchOrientation=RIGHT, origin=(18.75, 12.5, 0.0)))
mdb.models['Model-1'].parts['wall'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-0.25, -0.5))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(0.25, -0.5))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-0.25, -0.5), 
    point2=(0.25, -0.5))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, -0.5))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, -0.5), 
    ))
mdb.models['Model-1'].parts['wall'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['wall'].faces.findAt(((18.833333, 15.0, 0.0), 
    )), sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['wall'].Set(edges=
    mdb.models['Model-1'].parts['wall'].edges.findAt(((18.5, 18.0, 0.0), )), 
    name='wall_excavation')
mdb.models['Model-1'].parts['wall'].Set(edges=
    mdb.models['Model-1'].parts['wall'].edges.findAt(((18.5, 10.25, 0.0), ), ((
    18.625, 5.0, 0.0), ), ((19.0, 6.75, 0.0), ), ((19.0, 14.0, 0.0), ), ), 
    name='wall_no_excavation')
mdb.models['Model-1'].parts['clay'].Set(edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt(((18.5, 18.0, 0.0), )), 
    name='clay_excavation')
mdb.models['Model-1'].parts['clay'].Set(edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt(((19.0, 8.75, 0.0), ), ((
    18.625, 5.0, 0.0), ), ((18.5, 10.25, 0.0), ), ), name='clay_no_excavation')
mdb.models['Model-1'].parts['clay'].Set(edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt(((15.0, 9.0, 0.0), ), ((
    15.5, 3.0, 0.0), ), ), name='clay_pile_int')
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=1.07, name='__profile__', 
    sheetSize=43.13, transform=
    mdb.models['Model-1'].parts['pile'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['pile'].faces.findAt((15.333333, 
    7.0, 0.0), (0.0, 0.0, 1.0)), sketchPlaneSide=SIDE1, 
    sketchOrientation=RIGHT, origin=(15.25, 4.5, 0.0)))
mdb.models['Model-1'].parts['pile'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-0.25, -6.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(0.25, -6.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-0.25, -6.0), 
    point2=(0.25, -6.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, -6.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, -6.0), 
    ))
mdb.models['Model-1'].parts['pile'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['pile'].faces.findAt(((15.333333, 7.0, 0.0), ))
    , sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['pile'].Set(edges=
    mdb.models['Model-1'].parts['pile'].edges.findAt(((15.5, 1.875, 0.0), ), ((
    15.0, 8.625, 0.0), ), ), name='pile_clay_int')
mdb.models['Model-1'].parts['pile'].Set(edges=
    mdb.models['Model-1'].parts['pile'].edges.findAt(((15.0, -1.875, 0.0), ), (
    (15.5, -2.625, 0.0), ), ), name='pile_clya_no_int_lateral')
mdb.models['Model-1'].parts['pile'].Set(edges=
    mdb.models['Model-1'].parts['pile'].edges.findAt(((15.125, -3.0, 0.0), )), 
    name='pile_clay_no_int_bottom')
mdb.models['Model-1'].parts['wall'].Set(edges=
    mdb.models['Model-1'].parts['wall'].edges.findAt(((18.5, 10.25, 0.0), ), ((
    19.0, 6.75, 0.0), ), ((19.0, 14.0, 0.0), ), ((18.5, 18.0, 0.0), ), ), name=
    'wall_lateral')
mdb.models['Model-1'].parts['wall'].Set(edges=
    mdb.models['Model-1'].parts['wall'].edges.findAt(((18.625, 5.0, 0.0), )), 
    name='wall_bottom')
mdb.models['Model-1'].parts['clay'].Set(edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt(((18.625, 5.0, 0.0), )), 
    name='clay_bottom')
mdb.models['Model-1'].parts['clay'].Set(edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt(((19.0, 8.75, 0.0), ), ((
    18.5, 10.25, 0.0), ), ((18.5, 18.0, 0.0), ), ), name='clay_lateral')
mdb.models['Model-1'].parts['pile'].Set(edges=
    mdb.models['Model-1'].parts['pile'].edges.findAt(((15.0, -1.875, 0.0), ), (
    (15.5, -2.625, 0.0), ), ((15.5, 1.875, 0.0), ), ((15.0, 8.625, 0.0), ), ), 
    name='pile_lateral')
mdb.models['Model-1'].parts['pile'].sets.changeKey(fromName=
    'pile_clay_no_int_bottom', toName='pile_bottom')
mdb.models['Model-1'].parts['pile'].Set(edges=
    mdb.models['Model-1'].parts['pile'].edges.findAt(((15.0, -1.875, 0.0), ), (
    (15.5, -2.625, 0.0), ), ((15.5, 1.875, 0.0), ), ((15.0, 8.625, 0.0), ), ), 
    name='pile_lateral')
mdb.models['Model-1'].materials.changeKey(fromName='pile', toName='pile_wall')
mdb.models['Model-1'].sections.changeKey(fromName='pile', toName='pile_wall')
mdb.models['Model-1'].parts['clay'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['clay'].sets['clay'], sectionName='clay', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['pile'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['pile'].sets['pile'], sectionName='pile_wall', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['wall'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['wall'].sets['wall'], sectionName='pile_wall', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].rootAssembly.suppressFeatures(featureNames=('soil-1', ))
del mdb.models['Model-1'].parts['pile'].features['Partition face-1']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=1.07, name='__profile__', 
    sheetSize=43.13, transform=
    mdb.models['Model-1'].parts['pile'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['pile'].faces.findAt((15.333333, 
    7.0, 0.0), (0.0, 0.0, 1.0)), sketchPlaneSide=SIDE1, 
    sketchOrientation=RIGHT, origin=(15.25, 4.5, 0.0)))
mdb.models['Model-1'].parts['pile'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-0.25, -4.5))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(0.25, -4.5))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.25, -4.5), point2=
    (-0.25, -4.5))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, -4.5))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, -4.5), 
    ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-0.25, -4.5), 
    point2=(0.25, -4.5))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.225, -4.5))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.225, 
    -4.5), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-0.225, -4.5))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.225, -4.5))
mdb.models['Model-1'].sketches['__profile__'].ParallelConstraint(addUndoState=
    False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-0.225, 
    -4.5), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.225, 
    -4.5), ))
mdb.models['Model-1'].parts['pile'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['pile'].faces.findAt(((15.333333, 7.0, 0.0), ))
    , sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['pile'].Set(edges=
    mdb.models['Model-1'].parts['pile'].edges.findAt(((15.5, 3.0, 0.0), ), ((
    15.0, 9.0, 0.0), ), ), name='pile_clay_int')
mdb.models['Model-1'].parts['pile'].Set(edges=
    mdb.models['Model-1'].parts['pile'].edges.findAt(((15.0, -0.75, 0.0), ), ((
    15.5, -2.25, 0.0), ), ), name='pile_clya_no_int_lateral')
mdb.models['Model-1'].parts['pile'].Set(edges=
    mdb.models['Model-1'].parts['pile'].edges.findAt(((15.5, 3.0, 0.0), ), ((
    15.0, 9.0, 0.0), ), ((15.0, -0.75, 0.0), ), ((15.5, -2.25, 0.0), ), ), 
    name='pile_lateral')
mdb.models['Model-1'].parts['pile'].Set(edges=
    mdb.models['Model-1'].parts['pile'].edges.findAt(((15.125, -3.0, 0.0), )), 
    name='pile_bottom')
mdb.models['Model-1'].rootAssembly.deleteFeatures(('crack-1', 'soil-1'))
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='clay-1', part=
    mdb.models['Model-1'].parts['clay'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='crack-1', part=
    mdb.models['Model-1'].parts['crack'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='pile-1', part=
    mdb.models['Model-1'].parts['pile'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='wall-1', part=
    mdb.models['Model-1'].parts['wall'])
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=2.62, name='__profile__', 
    sheetSize=104.92, transform=
    mdb.models['Model-1'].parts['clay'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['clay'].faces.findAt((17.5, 
    9.666667, 0.0), (0.0, 0.0, 1.0)), sketchPlaneSide=SIDE1, 
    sketchOrientation=RIGHT, origin=(32.730907, 9.74105, 0.0)))
mdb.models['Model-1'].parts['clay'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-13.730907, 
    -4.74105), point2=(-13.730907, -9.74105000003483))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-13.730907, 
    -7.24105))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-13.730907, 
    -7.24105), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-13.730907, 
    2.75895))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-13.730907, 
    -7.24105))
mdb.models['Model-1'].sketches['__profile__'].ParallelConstraint(addUndoState=
    False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-13.730907, 
    2.75895), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-13.730907, 
    -7.24105), ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-13.730907, 
    -9.74105))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-0.730907, 
    -9.74105))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-13.730907, 
    -9.74105000003483), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-0.730907, 
    -9.74105), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-14.230907, 
    -4.74105), point2=(-14.230907, -9.74105000003483))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-14.230907, 
    -7.24105))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-14.230907, 
    -7.24105), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-13.980907, 
    -4.74105))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-14.230907, 
    -7.24105))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-13.980907, 
    -4.74105), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-14.230907, 
    -7.24105), ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-14.230907, 
    -9.74105))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-0.730907, 
    -9.74105))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-14.230907, 
    -9.74105000003483), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-0.730907, 
    -9.74105), ))
mdb.models['Model-1'].parts['clay'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['clay'].faces.findAt(((17.5, 9.666667, 0.0), ))
    , sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=1.92, name='__profile__', 
    sheetSize=77.17, transform=
    mdb.models['Model-1'].parts['clay'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['clay'].faces.findAt((28.833333, 
    1.666667, 0.0), (0.0, 0.0, 1.0)), sketchPlaneSide=SIDE1, 
    sketchOrientation=RIGHT, origin=(33.75, 10.0, 0.0)))
mdb.models['Model-1'].parts['clay'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-14.75, -5.0), 
    point2=(14.75, -5.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, -5.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, -5.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-14.75, -5.25))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, -5.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-14.75, 
    -5.25), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, -5.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((14.75, -5.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((14.75, 0.0))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((14.75, 
    -5.0), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((14.75, 0.0), 
    ))
mdb.models['Model-1'].parts['clay'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['clay'].faces.findAt(((28.833333, 1.666667, 
    0.0), )), sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].rootAssembly.deleteFeatures(('clay-1', 'crack-1', 
    'pile-1', 'wall-1'))
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='clay-1', part=
    mdb.models['Model-1'].parts['clay'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='crack-1', part=
    mdb.models['Model-1'].parts['crack'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='pile-1', part=
    mdb.models['Model-1'].parts['pile'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='wall-1', part=
    mdb.models['Model-1'].parts['wall'])
mdb.models['Model-1'].StaticStep(name='release_lateral', previous='gravity')
mdb.models['Model-1'].StaticStep(name='release_bottom', previous=
    'release_lateral')
mdb.models['Model-1'].StaticStep(name='release_pile', previous=
    'release_bottom')
del mdb.models['Model-1'].steps['pile_bc']
mdb.models['Model-1'].steps.changeKey(fromName='release_pile', toName=
    'release_pile_lateral')
mdb.models['Model-1'].steps.changeKey(fromName='release_lateral', toName=
    'release_wall_lateral')
mdb.models['Model-1'].steps.changeKey(fromName='release_bottom', toName=
    'release_wall_bottom')
del mdb.models['Model-1'].steps['release_wall_bottom']
mdb.models['Model-1'].StaticStep(name='release_wall_bottom', previous=
    'gravity')
mdb.models['Model-1'].rootAssembly.engineeringFeatures.cracks['Crack-1'].setValues(
    crackDomain=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].sets['clay'])
mdb.models['Model-1'].ContactProperty('soil_pile_wall')
mdb.models['Model-1'].interactionProperties['soil_pile_wall'].TangentialBehavior(
    dependencies=0, directionality=ISOTROPIC, elasticSlipStiffness=None, 
    formulation=PENALTY, fraction=0.005, maximumElasticSlip=FRACTION, 
    pressureDependency=OFF, shearStressLimit=None, slipRateDependency=OFF, 
    table=((0.15, ), ), temperatureDependency=OFF)
mdb.models['Model-1'].interactionProperties['soil_pile_wall'].NormalBehavior(
    allowSeparation=ON, constraintEnforcementMethod=DEFAULT, 
    pressureOverclosure=HARD)
mdb.models['Model-1'].rootAssembly.Surface(name='clay_excavtion', side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].edges.findAt(((18.5, 
    18.0, 0.0), )))
mdb.models['Model-1'].rootAssembly.Surface(name='clay_no_excavation', 
    side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].edges.findAt(((18.5, 
    10.25, 0.0), ), ((18.625, 5.0, 0.0), ), ((19.0, 8.75, 0.0), ), ))
mdb.models['Model-1'].rootAssembly.surfaces.changeKey(fromName='clay_excavtion'
    , toName='clay_wall_excavtion')
mdb.models['Model-1'].rootAssembly.surfaces.changeKey(fromName=
    'clay_no_excavation', toName='clay_wall_no_excavation')
mdb.models['Model-1'].rootAssembly.Surface(name='clay_pile_int', side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].edges.findAt(((15.5, 
    3.0, 0.0), ), ((15.0, 9.0, 0.0), ), ))
mdb.models['Model-1'].rootAssembly.Surface(name='pile_clay_excavation', 
    side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['wall-1'].edges.findAt(((18.5, 
    18.0, 0.0), )))
mdb.models['Model-1'].rootAssembly.Surface(name='pile_clay_no_excavation', 
    side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['wall-1'].edges.findAt(((18.5, 
    10.25, 0.0), ), ((18.625, 5.0, 0.0), ), ((19.0, 6.75, 0.0), ), ((19.0, 
    14.0, 0.0), ), ))
mdb.models['Model-1'].rootAssembly.surfaces.changeKey(fromName=
    'pile_clay_excavation', toName='wall_clay_excavation')
mdb.models['Model-1'].rootAssembly.surfaces.changeKey(fromName=
    'pile_clay_no_excavation', toName='wall_clay_no_excavation')
mdb.models['Model-1'].rootAssembly.Surface(name='pile_clay_int', side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['pile-1'].edges.findAt(((15.5, 
    3.0, 0.0), ), ((15.375, 12.0, 0.0), ), ((15.0, 9.0, 0.0), ), ))
mdb.models['Model-1'].rootAssembly.Surface(name='clay_pile_int', side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].edges.findAt(((15.5, 
    3.0, 0.0), ), ((15.0, 9.0, 0.0), ), ((15.375, 12.0, 0.0), ), ))
mdb.models['Model-1'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='gravity', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='soil_pile_wall', master=
    mdb.models['Model-1'].rootAssembly.surfaces['wall_clay_excavation'], name=
    'wall_clay_int', slave=
    mdb.models['Model-1'].rootAssembly.surfaces['clay_wall_excavtion'], 
    sliding=FINITE, thickness=ON)
mdb.models['Model-1'].interactions.changeKey(fromName='wall_clay_int', toName=
    'wall_clay_excavation_int')
mdb.models['Model-1'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='gravity', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='soil_pile_wall', master=
    mdb.models['Model-1'].rootAssembly.surfaces['wall_clay_no_excavation'], 
    name='wall_clay_no_excavation_int', slave=
    mdb.models['Model-1'].rootAssembly.surfaces['clay_wall_no_excavation'], 
    sliding=FINITE, thickness=ON)
mdb.models['Model-1'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='gravity', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='soil_pile_wall', master=
    mdb.models['Model-1'].rootAssembly.surfaces['pile_clay_int'], name=
    'pile_clay_int', slave=
    mdb.models['Model-1'].rootAssembly.surfaces['clay_pile_int'], sliding=
    FINITE, thickness=ON)
mdb.models['Model-1'].ModelChange(activeInStep=False, createStepName=
    'excavation', includeStrain=False, name='excavation', region=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].sets['excavation'])
mdb.models['Model-1'].Gravity(comp2=-10.0, createStepName='gravity', 
    distributionType=UNIFORM, field='', name='gravity')
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].edges.findAt(((0.0, 
    3.0, 0.0), ), ((0.0, 14.0, 0.0), ), ), name='clay_left_bc')
mdb.models['Model-1'].rootAssembly.sets.changeKey(fromName='clay_left_bc', 
    toName='clay_lateral_bc')
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].edges.findAt(((48.5, 
    3.75, 0.0), ), ((0.0, 3.0, 0.0), ), ((48.5, 16.25, 0.0), ), ((0.0, 14.0, 
    0.0), ), ), name='clay_lateral_bc')
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].edges.findAt(((
    41.125, 0.0, 0.0), ), ((17.75, 0.0, 0.0), ), ((18.875, 0.0, 0.0), ), ((
    11.25, 0.0, 0.0), ), ), name='clay_bottom_bc')
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='gravity', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'clay_left_bc', region=
    mdb.models['Model-1'].rootAssembly.sets['clay_lateral_bc'], u1=0.0, u2=0.0, 
    ur3=UNSET)
mdb.models['Model-1'].boundaryConditions.changeKey(fromName='clay_left_bc', 
    toName='clay_lateral_bc')
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='gravity', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'clay_bottom_bc', region=
    mdb.models['Model-1'].rootAssembly.sets['clay_bottom_bc'], u1=0.0, u2=0.0, 
    ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='gravity', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'clay_pile_int_bottom', region=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].sets['clay_bottom'], 
    u1=UNSET, u2=0.0, ur3=UNSET)
mdb.models['Model-1'].boundaryConditions['clay_pile_int_bottom'].deactivate(
    'release_wall_bottom')
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='gravity', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'clay_pile_int_lateral', region=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].sets['clay_lateral']
    , u1=0.0, u2=UNSET, ur3=UNSET)
mdb.models['Model-1'].boundaryConditions['clay_pile_int_lateral'].deactivate(
    'release_wall_lateral')
mdb.models['Model-1'].boundaryConditions.changeKey(fromName=
    'clay_pile_int_bottom', toName='clay_wall_int_bottom_bc')
mdb.models['Model-1'].boundaryConditions.changeKey(fromName=
    'clay_pile_int_lateral', toName='clay_wall_int_lateral_bc')
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='gravity', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'wall_clay_int_bottom_bc', region=
    mdb.models['Model-1'].rootAssembly.instances['wall-1'].sets['wall_bottom'], 
    u1=UNSET, u2=0.0, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='gravity', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'wall_clay_int_lateral_bc', region=
    mdb.models['Model-1'].rootAssembly.instances['wall-1'].sets['wall_lateral']
    , u1=0.0, u2=UNSET, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='gravity', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'clay_pile_int_lateral_bc', region=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].sets['clay_pile_int']
    , u1=0.0, u2=UNSET, ur3=UNSET)
mdb.models['Model-1'].boundaryConditions.changeKey(fromName=
    'clay_pile_int_lateral_bc', toName='clay_pile_int_bc')
mdb.models['Model-1'].boundaryConditions['clay_pile_int_bc'].setValues(u2=0.0)
mdb.models['Model-1'].steps.changeKey(fromName='release_pile_lateral', toName=
    'release_pile')
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='gravity', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'pile_bottom_bc', region=
    mdb.models['Model-1'].rootAssembly.instances['pile-1'].sets['pile_bottom'], 
    u1=UNSET, u2=0.0, ur3=UNSET)
mdb.models['Model-1'].boundaryConditions['wall_clay_int_bottom_bc'].deactivate(
    'release_wall_bottom')
mdb.models['Model-1'].boundaryConditions['wall_clay_int_lateral_bc'].deactivate(
    'release_wall_lateral')
mdb.models['Model-1'].boundaryConditions['clay_pile_int_bc'].deactivate(
    'release_pile')
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['crack-1'].edges.findAt(((
    17.0, 0.75, 0.0), )), faces=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].faces.findAt(((
    38.666667, 3.333333, 0.0), (0.0, 0.0, 1.0)), ((17.5, 1.666667, 0.0), (0.0, 
    0.0, 1.0)), ((18.833333, 3.333333, 0.0), (0.0, 0.0, 1.0)), ((10.0, 8.0, 
    0.0), (0.0, 0.0, 1.0)), ((28.833333, 10.0, 0.0), (0.0, 0.0, 1.0)), ((17.5, 
    14.666667, 0.0), (0.0, 0.0, 1.0)), )+\
    mdb.models['Model-1'].rootAssembly.instances['pile-1'].faces.findAt(((
    15.166667, 4.0, 0.0), (0.0, 0.0, 1.0)), ((15.333333, -1.0, 0.0), (0.0, 0.0, 
    1.0)), )+\
    mdb.models['Model-1'].rootAssembly.instances['wall-1'].faces.findAt(((
    18.833333, 9.666667, 0.0), (0.0, 0.0, 1.0)), ((18.666667, 14.666667, 0.0), 
    (0.0, 0.0, 1.0)), ), name='whole_model')
mdb.models['Model-1'].GeostaticStress(lateralCoeff1=0.7, lateralCoeff2=None, 
    name='geo', region=mdb.models['Model-1'].rootAssembly.sets['whole_model'], 
    stressMag1=0.0, stressMag2=-451200.0, vCoord1=20.0, vCoord2=0.0)
mdb.models['Model-1'].ExpressionField(description='', expression='20 -  Y ', 
    localCsys=None, name='AnalyticalField-1')
mdb.models['Model-1'].PorePressure(distributionType=FIELD, field=
    'AnalyticalField-1', name='pore', porePressure1=10000.0, region=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].sets['clay'], 
    variation=CONSTANT_RATIO)
mdb.models['Model-1'].VoidsRatio(distributionType=UNIFORM, name=
    'Predefined Field-3', region=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].sets['clay'], 
    variation=CONSTANT_RATIO, voidsRatio1=0.64)
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=2.62, name='__profile__', 
    sheetSize=104.92, transform=
    mdb.models['Model-1'].parts['clay'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['clay'].faces.findAt((17.5, 
    14.666667, 0.0), (0.0, 0.0, 1.0)), sketchPlaneSide=SIDE1, 
    sketchOrientation=RIGHT, origin=(9.25, 16.0, 0.0)))
mdb.models['Model-1'].parts['clay'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(5.75, -4.0), point2=
    (5.75, 4.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((5.75, 0.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((5.75, 0.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-8.5, -4.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((5.75, 0.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-8.5, -4.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    5.75, 0.0), ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((5.75, 4.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 4.0))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((5.75, 4.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    0.0, 4.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(6.25, -4.0), point2=
    (6.25, 4.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((6.25, 0.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((6.25, 0.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((6.4, -4.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((6.25, 0.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((6.4, -4.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    6.25, 0.0), ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((6.25, 4.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 4.0))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((6.25, 4.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    0.0, 4.0), ))
mdb.models['Model-1'].parts['clay'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['clay'].faces.findAt(((17.5, 14.666667, 0.0), 
    )), sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['clay'].seedEdgeBySize(constraint=FINER, 
    deviationFactor=0.1, edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt(((15.5, 14.0, 0.0), ), ((
    16.25, 12.0, 0.0), ), ((18.5, 18.0, 0.0), ), ((16.25, 20.0, 0.0), ), ((
    15.0, 14.0, 0.0), ), ((26.375, 5.0, 0.0), ), ((19.0, 3.75, 0.0), ), ((
    41.125, 0.0, 0.0), ), ((48.5, 3.75, 0.0), ), ((18.5, 3.75, 0.0), ), ((18.5, 
    10.25, 0.0), ), ((15.5, 3.0, 0.0), ), ((17.75, 0.0, 0.0), ), ((11.25, 12.0, 
    0.0), ), ((0.0, 3.0, 0.0), ), ((11.25, 0.0, 0.0), ), ((15.0, 9.0, 0.0), ), 
    ((48.5, 16.25, 0.0), ), ((26.375, 20.0, 0.0), ), ((19.0, 8.75, 0.0), ), ((
    3.75, 20.0, 0.0), ), ((0.0, 14.0, 0.0), ), ), size=1.0)
mdb.models['Model-1'].parts['clay'].setMeshControls(algorithm=MEDIAL_AXIS, 
    elemShape=QUAD, regions=mdb.models['Model-1'].parts['clay'].faces.findAt(((
    16.5, 14.666667, 0.0), ), ((15.166667, 14.666667, 0.0), ), ((38.666667, 
    3.333333, 0.0), ), ((17.5, 1.666667, 0.0), ), ((18.833333, 3.333333, 0.0), 
    ), ((10.0, 8.0, 0.0), ), ((28.833333, 10.0, 0.0), ), ((10.0, 17.333333, 
    0.0), ), ))
mdb.models['Model-1'].parts['clay'].setElementType(elemTypes=(ElemType(
    elemCode=CPE4P, elemLibrary=STANDARD), ElemType(elemCode=UNKNOWN_TRI, 
    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['clay'].faces.findAt(((16.5, 14.666667, 0.0), 
    ), ((15.166667, 14.666667, 0.0), ), ((38.666667, 3.333333, 0.0), ), ((17.5, 
    1.666667, 0.0), ), ((18.833333, 3.333333, 0.0), ), ((10.0, 8.0, 0.0), ), ((
    28.833333, 10.0, 0.0), ), ((10.0, 17.333333, 0.0), ), ), ))
mdb.models['Model-1'].parts['clay'].generateMesh()
mdb.models['Model-1'].parts['pile'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=1.0)
mdb.models['Model-1'].parts['pile'].setMeshControls(algorithm=MEDIAL_AXIS, 
    elemShape=QUAD, regions=mdb.models['Model-1'].parts['pile'].faces.findAt(((
    15.166667, 4.0, 0.0), ), ((15.333333, -1.0, 0.0), ), ))
mdb.models['Model-1'].parts['pile'].setElementType(elemTypes=(ElemType(
    elemCode=CPE4, elemLibrary=STANDARD), ElemType(elemCode=CPE3, 
    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['pile'].faces.findAt(((15.166667, 4.0, 0.0), ), 
    ((15.333333, -1.0, 0.0), ), ), ))
mdb.models['Model-1'].parts['pile'].generateMesh()
mdb.models['Model-1'].parts['wall'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=1.0)
mdb.models['Model-1'].parts['wall'].setElementType(elemTypes=(ElemType(
    elemCode=CPE4, elemLibrary=STANDARD), ElemType(elemCode=CPE3, 
    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['wall'].faces.findAt(((18.833333, 9.666667, 
    0.0), ), ((18.666667, 14.666667, 0.0), ), ), ))
mdb.models['Model-1'].parts['wall'].generateMesh()
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name='Job-pile_wall_test', 
    nodalOutputPrecision=SINGLE, numCpus=1, numGPUs=0, queue=None, 
    resultsFormat=ODB, scratch='', type=ANALYSIS, userSubroutine='', waitHours=
    0, waitMinutes=0)
mdb.models['Model-1'].sections.changeKey(fromName='pile_wall', toName='pile')
mdb.models['Model-1'].HomogeneousSolidSection(material='pile_wall', name='wall'
    , thickness=None)
mdb.models['Model-1'].sections['pile'].setValues(material='pile_wall', 
    thickness=None)
del mdb.models['Model-1'].parts['wall'].sectionAssignments[0]
mdb.models['Model-1'].parts['wall'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['wall'].sets['wall'], sectionName='wall', 
    thicknessAssignment=FROM_SECTION)
del mdb.models['Model-1'].parts['pile'].sectionAssignments[0]
mdb.models['Model-1'].parts['pile'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['pile'].sets['pile'], sectionName='pile', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].rootAssembly.regenerate()
# mdb.jobs['Job-pile_wall_test'].submit(consistencyChecking=OFF, datacheckJob=True)

mdb.models['Model-1'].steps['injection'].setValues(matrixSolver=DIRECT, 
    matrixStorage=UNSYMMETRIC)
del mdb.models['Model-1'].steps['excavation']
mdb.models['Model-1'].StaticStep(matrixSolver=DIRECT, matrixStorage=UNSYMMETRIC
    , name='excavation', previous='release_pile')
mdb.models['Model-1'].ModelChange(activeInStep=False, createStepName=
    'excavation', includeStrain=False, name='excavation', region=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].sets['excavation'])
# mdb.jobs['Job-pile_wall_test'].submit(consistencyChecking=OFF)
mdb.models['Model-1'].loads['gravity'].setValues(distributionType=UNIFORM, 
    field='', region=Region(
    faces=mdb.models['Model-1'].rootAssembly.instances['clay-1'].faces.findAt((
    (16.5, 14.666667, 0.0), (0.0, 0.0, 1.0)), ((15.166667, 14.666667, 0.0), (
    0.0, 0.0, 1.0)), ((38.666667, 3.333333, 0.0), (0.0, 0.0, 1.0)), ((17.5, 
    1.666667, 0.0), (0.0, 0.0, 1.0)), ((18.833333, 3.333333, 0.0), (0.0, 0.0, 
    1.0)), ((10.0, 8.0, 0.0), (0.0, 0.0, 1.0)), ((28.833333, 10.0, 0.0), (0.0, 
    0.0, 1.0)), ((10.0, 17.333333, 0.0), (0.0, 0.0, 1.0)), )+\
    mdb.models['Model-1'].rootAssembly.instances['pile-1'].faces.findAt(((
    15.166667, 4.0, 0.0), (0.0, 0.0, 1.0)), ((15.333333, -1.0, 0.0), (0.0, 0.0, 
    1.0)), )+\
    mdb.models['Model-1'].rootAssembly.instances['wall-1'].faces.findAt(((
    18.833333, 9.666667, 0.0), (0.0, 0.0, 1.0)), ((18.666667, 14.666667, 0.0), 
    (0.0, 0.0, 1.0)), ), 
    edges=mdb.models['Model-1'].rootAssembly.instances['crack-1'].edges.findAt(
    ((17.0, 0.75, 0.0), ), )))
# mdb.jobs['Job-pile_wall_test'].submit(consistencyChecking=OFF)
mdb.models['Model-1'].predefinedFields['geo'].setValues(region=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].sets['clay'])
mdb.models['Model-1'].loads['gravity'].setValues(distributionType=UNIFORM, 
    field='', region=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].sets['clay'])
# mdb.jobs['Job-pile_wall_test'].submit(consistencyChecking=OFF)

# Save by augustus on 2019_01_08-18.20.59; build 2016 2015_09_25-04.31.09 126547
mdb.models['Model-1'].predefinedFields['geo'].suppress()
mdb.models['Model-1'].materials['clay'].elastic.setValues(table=((12000000.0, 
    0.3), ))
# mdb.jobs['Job-pile_wall_test'].submit(consistencyChecking=OFF)
mdb.models['Model-1'].steps['gravity'].setValues(matrixSolver=DIRECT, 
    matrixStorage=UNSYMMETRIC, maxInc=1.0, minInc=1e-05, 
    timeIncrementationMethod=AUTOMATIC, utol=1e-05)
# mdb.jobs['Job-pile_wall_test'].submit(consistencyChecking=OFF)
mdb.models['Model-1'].materials['clay'].density.setValues(table=((900.0, ), ))
mdb.models['Model-1'].materials['clay'].elastic.setValues(table=((12000000.0, 
    0.49), ))
mdb.models['Model-1'].boundaryConditions['clay_lateral_bc'].setValues(u2=UNSET)
mdb.models['Model-1'].materials['clay'].density.setValues(table=((1616.0, ), ))
mdb.models['Model-1'].materials['clay'].elastic.setValues(table=((12000000.0, 
    0.3), ))
# mdb.jobs['Job-pile_wall_test'].submit(consistencyChecking=OFF)
mdb.models['Model-1'].steps['release_wall_lateral'].suppress()
mdb.models['Model-1'].boundaryConditions['clay_wall_int_lateral_bc'].deactivate(
    'release_wall_bottom')
mdb.models['Model-1'].loads['gravity'].setValues(distributionType=UNIFORM, 
    field='', region=Region(
    faces=mdb.models['Model-1'].rootAssembly.instances['clay-1'].faces.getSequenceFromMask(
    mask=('[#ff ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['pile-1'].faces.getSequenceFromMask(
    mask=('[#3 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['wall-1'].faces.getSequenceFromMask(
    mask=('[#3 ]', ), ), 
    edges=mdb.models['Model-1'].rootAssembly.instances['crack-1'].edges.getSequenceFromMask(
    mask=('[#1 ]', ), )))
# mdb.jobs['Job-pile_wall_test'].submit(consistencyChecking=OFF)
mdb.models['Model-1'].boundaryConditions['pile_bottom_bc'].setValues(u1=0.0)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='gravity', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'pile_lateral_bc', region=
    mdb.models['Model-1'].rootAssembly.instances['pile-1'].sets['pile_clya_no_int_lateral']
    , u1=0.0, u2=UNSET, ur3=UNSET)
# Save by augustus on 2019_01_08-22.50.25; build 2016 2015_09_25-04.31.09 126547
