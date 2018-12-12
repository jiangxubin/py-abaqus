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
mdb.Model(modelType=STANDARD_EXPLICIT, name='Model-1')
# Save by augustus on 2018_11_19-15.42.04; build 2016 2015_09_25-04.31.09 126547
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
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(30.0, 20.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(30.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-30.0, 20.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-30.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-30.0, 20.0), 
    point2=(30.0, 0.0))
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='soil', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['soil'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=3.16, name='__profile__', 
    sheetSize=126.49, transform=
    mdb.models['Model-1'].parts['soil'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['soil'].faces.findAt((10.0, 
    13.333333, 0.0), (0.0, 0.0, 1.0)), sketchPlaneSide=SIDE1, 
    sketchOrientation=RIGHT, origin=(0.0, 10.0, 0.0)))
mdb.models['Model-1'].parts['soil'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(8.0, 10.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-8.0, 10.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(8.0, 2.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-8.0, 2.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-8.0, 10.0), point2=
    (-8.0, 2.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-8.0, 6.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-8.0, 6.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-8.0, 2.0), point2=(
    8.0, 2.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 2.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 2.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-8.0, 6.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 2.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-8.0, 6.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    0.0, 2.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(8.0, 2.0), point2=(
    8.0, 10.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((8.0, 6.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((8.0, 6.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 2.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((8.0, 6.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 2.0), )
    , entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    8.0, 6.0), ))
mdb.models['Model-1'].parts['soil'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['soil'].faces.findAt(((10.0, 13.333333, 0.0), 
    )), sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(30.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(30.0, -5.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-30.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-30.0, -5.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-30.0, 0.0), point2=
    (-30.0, -5.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-30.0, -2.5))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-30.0, 
    -2.5), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-30.0, -5.0), 
    point2=(30.0, -5.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, -5.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, -5.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-30.0, -2.5))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, -5.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-30.0, 
    -2.5), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, -5.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(30.0, -5.0), point2=
    (30.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((30.0, -2.5))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((30.0, -2.5), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, -5.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((30.0, -2.5))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, -5.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    30.0, -2.5), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(30.0, 0.0), point2=(
    -30.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 0.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((30.0, -2.5))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((30.0, -2.5), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    0.0, 0.0), ))
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='rock', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['rock'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(7.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(7.0, 1.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(7.0, 1.0), point2=(
    7.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.0, 0.5))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.0, 0.5), 
    ))
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-7.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-7.0, 1.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-7.0, 1.0), point2=(
    -7.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-7.0, 0.5))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-7.0, 0.5), 
    ))
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='left-crack', 
    type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['left-crack'].BaseWire(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(7.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(7.0, 1.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(7.0, 1.0), point2=(
    7.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.0, 0.5))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.0, 0.5), 
    ))
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='right-crack', 
    type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['right-crack'].BaseWire(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].Material(name='soil')
mdb.models['Model-1'].materials['soil'].Density(table=((1616.0, ), ))
mdb.models['Model-1'].materials['soil'].Elastic(table=((5e-05, 0.17), ))
mdb.models['Model-1'].materials['soil'].MaxpsDamageInitiation(table=((1e-07, ), 
    ))
mdb.models['Model-1'].materials['soil'].maxpsDamageInitiation.DamageEvolution(
    mixedModeBehavior=POWER_LAW, power=1.0, table=((17000.0, 15000.0, 15000.0), 
    ), type=ENERGY)
mdb.models['Model-1'].materials['soil'].maxpsDamageInitiation.DamageStabilizationCohesive(
    cohesiveCoeff=0.0001)
mdb.models['Model-1'].materials['soil'].FluidLeakoff(table=((5.879e-16, 
    5.879e-16), ))
mdb.models['Model-1'].materials['soil'].GapFlow(table=((1e-06, ), ))
mdb.models['Model-1'].materials['soil'].Permeability(inertialDragCoefficient=
    0.142887, specificWeight=10000.0, table=((0.00014, 0.0), ))
mdb.models['Model-1'].Material(name='rock')
mdb.models['Model-1'].materials['rock'].Density(table=((3000.0, ), ))
mdb.models['Model-1'].materials['rock'].Elastic(table=((5e-08, 0.0), ))
mdb.models['Model-1'].HomogeneousSolidSection(material='soil', name='soil', 
    thickness=1.0)
mdb.models['Model-1'].HomogeneousSolidSection(material='rock', name='rock', 
    thickness=1.0)
mdb.models['Model-1'].parts['soil'].Set(faces=
    mdb.models['Model-1'].parts['soil'].faces.findAt(((-2.666667, 14.666667, 
    0.0), ), ((-15.333333, 17.333333, 0.0), ), ), name='soil')
mdb.models['Model-1'].parts['rock'].Set(faces=
    mdb.models['Model-1'].parts['rock'].faces.findAt(((10.0, -1.666667, 0.0), 
    )), name='rock')
mdb.models['Model-1'].parts['rock'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['rock'].sets['rock'], sectionName='rock', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['soil'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['soil'].sets['soil'], sectionName='soil', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=OFF, name='left-crack-1', 
    part=mdb.models['Model-1'].parts['left-crack'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=OFF, name='right-crack-1'
    , part=mdb.models['Model-1'].parts['right-crack'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=OFF, name='rock-1', part=
    mdb.models['Model-1'].parts['rock'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=OFF, name='soil-1', part=
    mdb.models['Model-1'].parts['soil'])
mdb.models['Model-1'].GeostaticStep(matrixSolver=DIRECT, matrixStorage=
    UNSYMMETRIC, name='gravity', nlgeom=ON, previous='Initial')
mdb.models['Model-1'].SoilsStep(cetol=None, initialInc=1.0, matrixSolver=DIRECT
    , matrixStorage=UNSYMMETRIC, maxInc=1.0, minInc=1e-05, name='execavation', 
    previous='gravity', timePeriod=1.0, utol=1e-08)
mdb.models['Model-1'].SoilsStep(cetol=None, initialInc=0.05, matrixSolver=
    DIRECT, matrixStorage=UNSYMMETRIC, maxInc=5.0, minInc=1e-12, name=
    'injection', previous='execavation', timePeriod=100.0, utol=1e-08)
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
    'S', 'LE', 'U', 'RF', 'CF', 'CSTRESS', 'CDISP', 'PHILSM', 'PSILSM', 
    'VOIDR', 'SAT', 'POR'))
mdb.models['Model-1'].ContactProperty('IntProp-1')
mdb.models['Model-1'].ContactProperty('IntProp-2')
mdb.models['Model-1'].interactionProperties['IntProp-2'].TangentialBehavior(
    formulation=FRICTIONLESS)
mdb.models['Model-1'].interactionProperties['IntProp-2'].NormalBehavior(
    allowSeparation=ON, constraintEnforcementMethod=DEFAULT, 
    pressureOverclosure=HARD)
mdb.models['Model-1'].rootAssembly.engineeringFeatures.XFEMCrack(crackDomain=
    mdb.models['Model-1'].rootAssembly.instances['soil-1'].sets['soil'], 
    interactionProperty='IntProp-1', name='Crack-1')
mdb.models['Model-1'].rootAssembly.Surface(name='rock-master', side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['rock-1'].edges.findAt(((15.0, 
    0.0, 0.0), )))
mdb.models['Model-1'].rootAssembly.Surface(name='soil-slave', side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['soil-1'].edges.findAt(((
    -15.0, 0.0, 0.0), )))
mdb.models['Model-1'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='Initial', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='IntProp-2', master=
    mdb.models['Model-1'].rootAssembly.surfaces['rock-master'], name='Int-1', 
    slave=mdb.models['Model-1'].rootAssembly.surfaces['soil-slave'], sliding=
    FINITE, thickness=ON)
mdb.models['Model-1'].rootAssembly.Set(faces=
    mdb.models['Model-1'].rootAssembly.instances['soil-1'].faces.findAt(((
    -2.666667, 14.666667, 0.0), (0.0, 0.0, 1.0)), ((-15.333333, 17.333333, 
    0.0), (0.0, 0.0, 1.0)), )+\
    mdb.models['Model-1'].rootAssembly.instances['rock-1'].faces.findAt(((10.0, 
    -1.666667, 0.0), (0.0, 0.0, 1.0)), ), name='gravity')
mdb.models['Model-1'].Gravity(comp2=-10.0, createStepName='gravity', 
    distributionType=UNIFORM, field='', name='gravity', region=
    mdb.models['Model-1'].rootAssembly.sets['gravity'])
mdb.models['Model-1'].rootAssembly.Surface(name='pore-surface', side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['soil-1'].edges.findAt(((
    -15.0, 0.0, 0.0), )))
mdb.models['Model-1'].Pressure(amplitude=UNSET, createStepName='injection', 
    distributionType=UNIFORM, field='', magnitude=10000.0, name='pore', region=
    mdb.models['Model-1'].rootAssembly.surfaces['pore-surface'])
mdb.models['Model-1'].rootAssembly.Surface(name='left-bc-edge', side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['soil-1'].edges.findAt(((
    -30.0, 15.0, 0.0), ), )+\
    mdb.models['Model-1'].rootAssembly.instances['rock-1'].edges.findAt(((
    -30.0, -1.25, 0.0), ), ))
mdb.models['Model-1'].rootAssembly.Surface(name='right-bc-edge', side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['soil-1'].edges.findAt(((30.0, 
    5.0, 0.0), ), )+\
    mdb.models['Model-1'].rootAssembly.instances['rock-1'].edges.findAt(((30.0, 
    -3.75, 0.0), ), ))
mdb.models['Model-1'].rootAssembly.Surface(name='rock-bottom-bc-edge', 
    side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['rock-1'].edges.findAt(((
    -15.0, -5.0, 0.0), )))
mdb.models['Model-1'].rootAssembly.Surface(name='rock-up-bc-edge', side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['rock-1'].edges.findAt(((15.0, 
    0.0, 0.0), )))
mdb.models['Model-1'].rootAssembly.Surface(name='soil-pore-left-bc-edge', 
    side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['soil-1'].edges.findAt(((
    -30.0, 15.0, 0.0), )))
mdb.models['Model-1'].rootAssembly.Surface(name='soil-right-pore-bc-edge', 
    side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['soil-1'].edges.findAt(((30.0, 
    5.0, 0.0), )))
mdb.models['Model-1'].rootAssembly.Surface(name='soil-up-before-pore-bc-edge', 
    side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['soil-1'].edges.findAt(((4.0, 
    20.0, 0.0), ), ((-13.5, 20.0, 0.0), ), ((24.5, 20.0, 0.0), ), ))
mdb.models['Model-1'].rootAssembly.Surface(name=
    'soil-bottom-before-pore-bc-edge', side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['soil-1'].edges.findAt(((
    -15.0, 0.0, 0.0), )))
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['soil-1'].edges.findAt(((-8.0, 
    18.0, 0.0), ), ((-4.0, 12.0, 0.0), ), ((8.0, 14.0, 0.0), ), ((-13.5, 20.0, 
    0.0), ), ((24.5, 20.0, 0.0), ), ), name='soil-up-after-pore-bc-edge')
del mdb.models['Model-1'].rootAssembly.surfaces['left-bc-edge']
del mdb.models['Model-1'].rootAssembly.surfaces['pore-surface']
del mdb.models['Model-1'].rootAssembly.surfaces['right-bc-edge']
del mdb.models['Model-1'].rootAssembly.surfaces['rock-bottom-bc-edge']
del mdb.models['Model-1'].rootAssembly.surfaces['soil-bottom-before-pore-bc-edge']
del mdb.models['Model-1'].rootAssembly.surfaces['soil-pore-left-bc-edge']
del mdb.models['Model-1'].rootAssembly.surfaces['soil-right-pore-bc-edge']
del mdb.models['Model-1'].rootAssembly.surfaces['soil-up-before-pore-bc-edge']
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['soil-1'].edges.findAt(((4.0, 
    20.0, 0.0), ), ((-13.5, 20.0, 0.0), ), ((24.5, 20.0, 0.0), ), ), name=
    'soil-up-before-pore-bc-edge')
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['soil-1'].edges.findAt(((
    -30.0, 15.0, 0.0), ), )+\
    mdb.models['Model-1'].rootAssembly.instances['rock-1'].edges.findAt(((
    -30.0, -1.25, 0.0), ), ), name='left-bc')
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['soil-1'].edges.findAt(((30.0, 
    5.0, 0.0), ), )+\
    mdb.models['Model-1'].rootAssembly.instances['rock-1'].edges.findAt(((30.0, 
    -3.75, 0.0), ), ), name='right-bc')
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['rock-1'].edges.findAt(((
    -15.0, -5.0, 0.0), )), name='rock-bottom-bc')
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['rock-1'].edges.findAt(((15.0, 
    0.0, 0.0), )), name='rock-up-bc')
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['soil-1'].edges.findAt(((
    -30.0, 15.0, 0.0), )), name='soil-left-pore-bc-edge')
mdb.models['Model-1'].rootAssembly.sets.changeKey(fromName='rock-bottom-bc', 
    toName='rock-bottom-bc-edge')
mdb.models['Model-1'].rootAssembly.sets.changeKey(fromName='rock-up-bc', 
    toName='rock-up-bc-edge')
mdb.models['Model-1'].rootAssembly.sets.changeKey(fromName='left-bc', toName=
    'left-bc-edge')
mdb.models['Model-1'].rootAssembly.sets.changeKey(fromName='right-bc', toName=
    'right-bc-edge')
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['soil-1'].edges.findAt(((30.0, 
    5.0, 0.0), )), name='soil-right-pore-bc-edge')
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['soil-1'].edges.findAt(((
    -15.0, 0.0, 0.0), )), name='soil-bottom-pore-bc-edge')
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='left-bc', 
    region=mdb.models['Model-1'].rootAssembly.sets['left-bc-edge'], u1=SET, u2=
    SET, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='right-bc', 
    region=mdb.models['Model-1'].rootAssembly.sets['right-bc-edge'], u1=SET, 
    u2=SET, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='rock-bc', 
    region=mdb.models['Model-1'].rootAssembly.sets['rock-bottom-bc-edge'], u1=
    SET, u2=SET, ur3=UNSET)
mdb.models['Model-1'].boundaryConditions.changeKey(fromName='rock-bc', toName=
    'rock-bottom-bc')
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='rock-up-bc', 
    region=mdb.models['Model-1'].rootAssembly.sets['rock-up-bc-edge'], u1=SET, 
    u2=SET, ur3=UNSET)
mdb.models['Model-1'].ExpressionField(description='', expression='20 -  Y ', 
    localCsys=None, name='AnalyticalField-1')
mdb.models['Model-1'].PorePressureBC(amplitude=UNSET, createStepName='gravity', 
    distributionType=FIELD, fieldName='AnalyticalField-1', fixed=OFF, 
    magnitude=10000.0, name='left-pore-bc', region=
    mdb.models['Model-1'].rootAssembly.sets['soil-left-pore-bc-edge'])
mdb.models['Model-1'].boundaryConditions['left-pore-bc'].move('gravity', 
    'Initial')
#* ValueError: Non-zero boundary condition in initial step.
mdb.models['Model-1'].PorePressureBC(amplitude=UNSET, createStepName='gravity', 
    distributionType=FIELD, fieldName='AnalyticalField-1', fixed=OFF, 
    magnitude=10000.0, name='right-pore-bc', region=
    mdb.models['Model-1'].rootAssembly.sets['soil-right-pore-bc-edge'])
mdb.models['Model-1'].PorePressureBC(amplitude=UNSET, createStepName='gravity', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, magnitude=200000.0, 
    name='bottom-pore-bc', region=
    mdb.models['Model-1'].rootAssembly.sets['soil-bottom-pore-bc-edge'])
mdb.models['Model-1'].PorePressureBC(amplitude=UNSET, createStepName='gravity', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, magnitude=0.0, name=
    'up-pore-bc', region=
    mdb.models['Model-1'].rootAssembly.sets['soil-up-before-pore-bc-edge'])
mdb.models['Model-1'].PorePressureBC(amplitude=UNSET, createStepName=
    'execavation', distributionType=UNIFORM, fieldName='', fixed=OFF, 
    magnitude=0.0, name='after-exe-up-pore-bc', region=
    mdb.models['Model-1'].rootAssembly.sets['soil-up-after-pore-bc-edge'])
mdb.models['Model-1'].GeostaticStress(lateralCoeff1=0.5, lateralCoeff2=None, 
    name='geo-soil', region=
    mdb.models['Model-1'].rootAssembly.instances['soil-1'].sets['soil'], 
    stressMag1=0.0, stressMag2=323200.0, vCoord1=20.0, vCoord2=0.0)
mdb.models['Model-1'].GeostaticStress(lateralCoeff1=0.5, lateralCoeff2=None, 
    name='geo-rock', region=
    mdb.models['Model-1'].rootAssembly.instances['rock-1'].sets['rock'], 
    stressMag1=-323200.0, stressMag2=-473200.0, vCoord1=0.0, vCoord2=-5.0)
mdb.models['Model-1'].predefinedFields['geo-soil'].setValues(stressMag2=
    -323200.0)
mdb.models['Model-1'].VoidsRatio(distributionType=UNIFORM, name='void', region=
    mdb.models['Model-1'].rootAssembly.instances['soil-1'].sets['soil'], 
    variation=CONSTANT_RATIO, voidsRatio1=0.64)
mdb.models['Model-1'].PorePressure(distributionType=FIELD, field=
    'AnalyticalField-1', name='pore', porePressure1=10000.0, region=
    mdb.models['Model-1'].rootAssembly.instances['soil-1'].sets['soil'], 
    variation=CONSTANT_RATIO)
mdb.models['Model-1'].boundaryConditions['bottom-pore-bc'].move('gravity', 
    'Initial')
#* ValueError: Non-zero boundary condition in initial step.
mdb.models['Model-1'].boundaryConditions['after-exe-up-pore-bc'].move(
    'execavation', 'injection')
mdb.models['Model-1'].boundaryConditions['bottom-pore-bc'].deactivate(
    'execavation')
mdb.models['Model-1'].boundaryConditions['left-pore-bc'].deactivate(
    'execavation')
mdb.models['Model-1'].boundaryConditions['right-pore-bc'].deactivate(
    'execavation')
mdb.models['Model-1'].boundaryConditions['up-pore-bc'].deactivate(
    'execavation')
mdb.models['Model-1'].PorePressureBC(amplitude=UNSET, createStepName=
    'execavation', distributionType=UNIFORM, fieldName='', fixed=OFF, 
    magnitude=10000.0, name='exe-left-pore-bc', region=
    mdb.models['Model-1'].rootAssembly.sets['soil-left-pore-bc-edge'])
mdb.models['Model-1'].PorePressureBC(amplitude=UNSET, createStepName=
    'execavation', distributionType=FIELD, fieldName='AnalyticalField-1', 
    fixed=OFF, magnitude=10000.0, name='exe-right-pore-bc', region=
    mdb.models['Model-1'].rootAssembly.sets['soil-right-pore-bc-edge'])
mdb.models['Model-1'].boundaryConditions['exe-left-pore-bc'].setValues(
    distributionType=FIELD, fieldName='AnalyticalField-1')
mdb.models['Model-1'].PorePressureBC(amplitude=UNSET, createStepName=
    'execavation', distributionType=UNIFORM, fieldName='', fixed=OFF, 
    magnitude=200000.0, name='exe-bottom-pore-bc', region=
    mdb.models['Model-1'].rootAssembly.sets['soil-bottom-pore-bc-edge'])
mdb.models['Model-1'].PorePressureBC(amplitude=UNSET, createStepName=
    'execavation', distributionType=UNIFORM, fieldName='', fixed=OFF, 
    magnitude=0.0, name='exe-up-pore-bc', region=
    mdb.models['Model-1'].rootAssembly.sets['soil-up-before-pore-bc-edge'])
mdb.models['Model-1'].loads['pore'].suppress()
mdb.models['Model-1'].loads['pore'].resume()
mdb.models['Model-1'].rootAssembly.seedPartInstance(deviationFactor=0.1, 
    minSizeFactor=0.1, regions=(
    mdb.models['Model-1'].rootAssembly.instances['soil-1'], ), size=1.0)
mdb.models['Model-1'].rootAssembly.seedPartInstance(deviationFactor=0.1, 
    minSizeFactor=0.1, regions=(
    mdb.models['Model-1'].rootAssembly.instances['rock-1'], ), size=1.0)
mdb.models['Model-1'].rootAssembly.setMeshControls(algorithm=MEDIAL_AXIS, 
    elemShape=QUAD, regions=
    mdb.models['Model-1'].rootAssembly.instances['soil-1'].faces.findAt(((
    -2.666667, 14.666667, 0.0), ), ((-15.333333, 17.333333, 0.0), ), ))
mdb.models['Model-1'].rootAssembly.setElementType(elemTypes=(ElemType(
    elemCode=CPE4P, elemLibrary=STANDARD), ElemType(elemCode=UNKNOWN_TRI, 
    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].rootAssembly.instances['soil-1'].faces.findAt(((
    -2.666667, 14.666667, 0.0), ), ((-15.333333, 17.333333, 0.0), ), ), ))
mdb.models['Model-1'].rootAssembly.generateMesh(regions=(
    mdb.models['Model-1'].rootAssembly.instances['soil-1'], ))
mdb.models['Model-1'].rootAssembly.setMeshControls(algorithm=MEDIAL_AXIS, 
    elemShape=QUAD, regions=
    mdb.models['Model-1'].rootAssembly.instances['rock-1'].faces.findAt(((10.0, 
    -1.666667, 0.0), )))
mdb.models['Model-1'].rootAssembly.generateMesh(regions=(
    mdb.models['Model-1'].rootAssembly.instances['rock-1'], ))
mdb.models['Model-1'].loads['pore'].suppress()
# Save by augustus on 2018_11_20-14.33.33; build 2016 2015_09_25-04.31.09 126547
