# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2016 replay file
# Internal Version: 2015_09_25-04.31.09 126547
# Run by augustus on Mon Nov 19 15:43:03 2018
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=193.507797241211, 
    height=106.066665649414)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('centrifuge.cae')
#: The model database "E:\workingspace\centrifuge\command-base\centrifuge.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.Spot(point=(30.0, 20.0))
s.Spot(point=(30.0, 0.0))
s.Spot(point=(-30.0, 20.0))
s.Spot(point=(-30.0, 0.0))
s.rectangle(point1=(-30.0, 20.0), point2=(30.0, 0.0))
p = mdb.models['Model-1'].Part(name='soil', dimensionality=TWO_D_PLANAR, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['soil']
p.BaseShell(sketch=s)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['soil']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
cliCommand("""session.journalOptions.setValues(replayGeometry=COORDINATE,recoverGeometry= COORDINATE)""")
p = mdb.models['Model-1'].parts['soil']
f, e, d1 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f.findAt(coordinates=(10.0, 13.333333, 
    0.0), normal=(0.0, 0.0, 1.0)), sketchPlaneSide=SIDE1, origin=(0.0, 10.0, 
    0.0))
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=126.49, gridSpacing=3.16, transform=t)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['soil']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
s1.Spot(point=(8.0, 10.0))
s1.Spot(point=(-8.0, 10.0))
s1.Spot(point=(8.0, 2.0))
s1.Spot(point=(-8.0, 2.0))
s1.Line(point1=(-8.0, 10.0), point2=(-8.0, 2.0))
s1.VerticalConstraint(entity=g.findAt((-8.0, 6.0)), addUndoState=False)
s1.Line(point1=(-8.0, 2.0), point2=(8.0, 2.0))
s1.HorizontalConstraint(entity=g.findAt((0.0, 2.0)), addUndoState=False)
s1.PerpendicularConstraint(entity1=g.findAt((-8.0, 6.0)), entity2=g.findAt((
    0.0, 2.0)), addUndoState=False)
s1.Line(point1=(8.0, 2.0), point2=(8.0, 10.0))
s1.VerticalConstraint(entity=g.findAt((8.0, 6.0)), addUndoState=False)
s1.PerpendicularConstraint(entity1=g.findAt((0.0, 2.0)), entity2=g.findAt((8.0, 
    6.0)), addUndoState=False)
p = mdb.models['Model-1'].parts['soil']
f = p.faces
pickedFaces = f.findAt(((10.0, 13.333333, 0.0), ))
e1, d2 = p.edges, p.datums
p.PartitionFaceBySketch(faces=pickedFaces, sketch=s1)
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.Spot(point=(30.0, 0.0))
s.Spot(point=(30.0, -5.0))
s.Spot(point=(-30.0, 0.0))
s.Spot(point=(-30.0, -5.0))
s.Line(point1=(-30.0, 0.0), point2=(-30.0, -5.0))
s.VerticalConstraint(entity=g.findAt((-30.0, -2.5)), addUndoState=False)
s.Line(point1=(-30.0, -5.0), point2=(30.0, -5.0))
s.HorizontalConstraint(entity=g.findAt((0.0, -5.0)), addUndoState=False)
s.PerpendicularConstraint(entity1=g.findAt((-30.0, -2.5)), entity2=g.findAt((
    0.0, -5.0)), addUndoState=False)
s.Line(point1=(30.0, -5.0), point2=(30.0, 0.0))
s.VerticalConstraint(entity=g.findAt((30.0, -2.5)), addUndoState=False)
s.PerpendicularConstraint(entity1=g.findAt((0.0, -5.0)), entity2=g.findAt((
    30.0, -2.5)), addUndoState=False)
s.Line(point1=(30.0, 0.0), point2=(-30.0, 0.0))
s.HorizontalConstraint(entity=g.findAt((0.0, 0.0)), addUndoState=False)
s.PerpendicularConstraint(entity1=g.findAt((30.0, -2.5)), entity2=g.findAt((
    0.0, 0.0)), addUndoState=False)
p = mdb.models['Model-1'].Part(name='rock', dimensionality=TWO_D_PLANAR, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['rock']
p.BaseShell(sketch=s)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['rock']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.Spot(point=(7.0, 0.0))
s1.Spot(point=(7.0, 1.0))
s1.Line(point1=(7.0, 1.0), point2=(7.0, 0.0))
s1.VerticalConstraint(entity=g.findAt((7.0, 0.5)), addUndoState=False)
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
p1 = mdb.models['Model-1'].parts['rock']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.Spot(point=(-7.0, 0.0))
s.Spot(point=(-7.0, 1.0))
s.Line(point1=(-7.0, 1.0), point2=(-7.0, 0.0))
s.VerticalConstraint(entity=g.findAt((-7.0, 0.5)), addUndoState=False)
p = mdb.models['Model-1'].Part(name='left-crack', dimensionality=TWO_D_PLANAR, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['left-crack']
p.BaseWire(sketch=s)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['left-crack']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.Spot(point=(7.0, 0.0))
s1.Spot(point=(7.0, 1.0))
s1.Line(point1=(7.0, 1.0), point2=(7.0, 0.0))
s1.VerticalConstraint(entity=g.findAt((7.0, 0.5)), addUndoState=False)
p = mdb.models['Model-1'].Part(name='right-crack', dimensionality=TWO_D_PLANAR, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['right-crack']
p.BaseWire(sketch=s1)
s1.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['right-crack']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['Model-1'].Material(name='soil')
mdb.models['Model-1'].materials['soil'].Density(table=((1616.0, ), ))
mdb.models['Model-1'].materials['soil'].Elastic(table=((5e-05, 0.17), ))
mdb.models['Model-1'].materials['soil'].MaxpsDamageInitiation(table=((1e-07, ), 
    ))
mdb.models['Model-1'].materials['soil'].maxpsDamageInitiation.DamageEvolution(
    type=ENERGY, mixedModeBehavior=POWER_LAW, power=1.0, table=((17000.0, 
    15000.0, 15000.0), ))
mdb.models['Model-1'].materials['soil'].maxpsDamageInitiation.DamageStabilizationCohesive(
    cohesiveCoeff=0.0001)
mdb.models['Model-1'].materials['soil'].FluidLeakoff(table=((5.879e-16, 
    5.879e-16), ))
mdb.models['Model-1'].materials['soil'].GapFlow(table=((1e-06, ), ))
mdb.models['Model-1'].materials['soil'].Permeability(specificWeight=10000.0, 
    inertialDragCoefficient=0.142887, table=((0.00014, 0.0), ))
mdb.models['Model-1'].Material(name='rock')
mdb.models['Model-1'].materials['rock'].Density(table=((3000.0, ), ))
mdb.models['Model-1'].materials['rock'].Elastic(table=((5e-08, 0.0), ))
mdb.models['Model-1'].HomogeneousSolidSection(name='soil', material='soil', 
    thickness=1.0)
mdb.models['Model-1'].HomogeneousSolidSection(name='rock', material='rock', 
    thickness=1.0)
p = mdb.models['Model-1'].parts['soil']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.07976, 
    farPlane=5.92024, width=4.50021, height=2.49334, viewOffsetX=0.355749, 
    viewOffsetY=-0.0335339)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['soil']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.83943, 
    farPlane=6.16057, width=5.65338, height=3.13225, viewOffsetX=0.563987, 
    viewOffsetY=0.116509)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.27065, 
    farPlane=6.72935, width=7.44693, height=4.12597, viewOffsetX=0.970731, 
    viewOffsetY=0.452596)
p = mdb.models['Model-1'].parts['soil']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['soil']
f = p.faces
faces = f.findAt(((-2.666667, 14.666667, 0.0), ), ((-15.333333, 17.333333, 
    0.0), ))
p.Set(faces=faces, name='soil')
#: The set 'soil' has been created (2 faces).
p = mdb.models['Model-1'].parts['rock']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['rock']
f = p.faces
faces = f.findAt(((10.0, -1.666667, 0.0), ))
p.Set(faces=faces, name='rock')
#: The set 'rock' has been created (1 face).
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['rock']
region = p.sets['rock']
p = mdb.models['Model-1'].parts['rock']
p.SectionAssignment(region=region, sectionName='rock', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['soil']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['soil']
region = p.sets['soil']
p = mdb.models['Model-1'].parts['soil']
p.SectionAssignment(region=region, sectionName='soil', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['left-crack']
a.Instance(name='left-crack-1', part=p, dependent=OFF)
p = mdb.models['Model-1'].parts['right-crack']
a.Instance(name='right-crack-1', part=p, dependent=OFF)
p = mdb.models['Model-1'].parts['rock']
a.Instance(name='rock-1', part=p, dependent=OFF)
p = mdb.models['Model-1'].parts['soil']
a.Instance(name='soil-1', part=p, dependent=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].GeostaticStep(name='gravity', previous='Initial', 
    matrixSolver=DIRECT, matrixStorage=UNSYMMETRIC, nlgeom=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='gravity')
mdb.models['Model-1'].SoilsStep(name='execavation', previous='gravity', 
    timePeriod=1.0, initialInc=1.0, minInc=1e-05, maxInc=1.0, utol=1e-08, 
    cetol=None, matrixSolver=DIRECT, matrixStorage=UNSYMMETRIC)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='execavation')
mdb.models['Model-1'].SoilsStep(name='injection', previous='execavation', 
    timePeriod=100.0, initialInc=0.05, minInc=1e-12, maxInc=5.0, utol=1e-08, 
    cetol=None, matrixSolver=DIRECT, matrixStorage=UNSYMMETRIC)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='injection')
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
    'S', 'LE', 'U', 'RF', 'CF', 'CSTRESS', 'CDISP', 'PHILSM', 'PSILSM', 
    'VOIDR', 'SAT', 'POR'))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    adaptiveMeshConstraints=OFF)
mdb.models['Model-1'].ContactProperty('IntProp-1')
#: The interaction property "IntProp-1" has been created.
mdb.models['Model-1'].ContactProperty('IntProp-2')
mdb.models['Model-1'].interactionProperties['IntProp-2'].TangentialBehavior(
    formulation=FRICTIONLESS)
mdb.models['Model-1'].interactionProperties['IntProp-2'].NormalBehavior(
    pressureOverclosure=HARD, allowSeparation=ON, 
    constraintEnforcementMethod=DEFAULT)
#: The interaction property "IntProp-2" has been created.
a = mdb.models['Model-1'].rootAssembly
crackDomain = a.instances['soil-1'].sets['soil']
a = mdb.models['Model-1'].rootAssembly
a.engineeringFeatures.XFEMCrack(name='Crack-1', crackDomain=crackDomain, 
    interactionProperty='IntProp-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['rock-1'].faces
faces1 = f1.findAt(((10.0, -1.666667, 0.0), ))
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['rock-1'].edges
side1Edges1 = s1.findAt(((15.0, 0.0, 0.0), ))
a.Surface(side1Edges=side1Edges1, name='rock-master')
#: The surface 'rock-master' has been created (1 edge).
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['soil-1'].faces
faces1 = f1.findAt(((-15.333333, 17.333333, 0.0), ))
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['soil-1'].edges
side1Edges1 = s1.findAt(((-15.0, 0.0, 0.0), ))
a.Surface(side1Edges=side1Edges1, name='soil-slave')
#: The surface 'soil-slave' has been created (1 edge).
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
region1=a.surfaces['rock-master']
a = mdb.models['Model-1'].rootAssembly
region2=a.surfaces['soil-slave']
mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='Int-1', 
    createStepName='Initial', master=region1, slave=region2, sliding=FINITE, 
    thickness=ON, interactionProperty='IntProp-2', adjustMethod=NONE, 
    initialClearance=OMIT, datumAxis=None, clearanceRegion=None)
#: The interaction "Int-1" has been created.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='gravity')
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['soil-1'].faces
faces1 = f1.findAt(((-2.666667, 14.666667, 0.0), ), ((-15.333333, 17.333333, 
    0.0), ))
f2 = a.instances['rock-1'].faces
faces2 = f2.findAt(((10.0, -1.666667, 0.0), ))
a.Set(faces=faces1+faces2, name='gravity')
#: The set 'gravity' has been created (3 faces).
a = mdb.models['Model-1'].rootAssembly
region = a.sets['gravity']
mdb.models['Model-1'].Gravity(name='gravity', createStepName='gravity', 
    comp2=-10.0, distributionType=UNIFORM, field='', region=region)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='injection')
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['soil-1'].faces
faces1 = f1.findAt(((-15.333333, 17.333333, 0.0), ))
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['soil-1'].edges
side1Edges1 = s1.findAt(((-15.0, 0.0, 0.0), ))
a.Surface(side1Edges=side1Edges1, name='pore-surface')
#: The surface 'pore-surface' has been created (1 edge).
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
region = a.surfaces['pore-surface']
mdb.models['Model-1'].Pressure(name='pore', createStepName='injection', 
    region=region, distributionType=UNIFORM, field='', magnitude=10000.0, 
    amplitude=UNSET)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['soil-1'].edges
side1Edges1 = s1.findAt(((-30.0, 15.0, 0.0), ))
s2 = a.instances['rock-1'].edges
side1Edges2 = s2.findAt(((-30.0, -1.25, 0.0), ))
a.Surface(side1Edges=side1Edges1+side1Edges2, name='left-bc-edge')
#: The surface 'left-bc-edge' has been created (2 edges).
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['soil-1'].edges
side1Edges1 = s1.findAt(((30.0, 5.0, 0.0), ))
s2 = a.instances['rock-1'].edges
side1Edges2 = s2.findAt(((30.0, -3.75, 0.0), ))
a.Surface(side1Edges=side1Edges1+side1Edges2, name='right-bc-edge')
#: The surface 'right-bc-edge' has been created (2 edges).
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['rock-1'].edges
side1Edges1 = s1.findAt(((-15.0, -5.0, 0.0), ))
a.Surface(side1Edges=side1Edges1, name='rock-bottom-bc-edge')
#: The surface 'rock-bottom-bc-edge' has been created (1 edge).
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['rock-1'].faces
faces1 = f1.findAt(((10.0, -1.666667, 0.0), ))
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['rock-1'].edges
side1Edges1 = s1.findAt(((15.0, 0.0, 0.0), ))
a.Surface(side1Edges=side1Edges1, name='rock-up-bc-edge')
#: The surface 'rock-up-bc-edge' has been created (1 edge).
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['soil-1'].edges
side1Edges1 = s1.findAt(((-30.0, 15.0, 0.0), ))
a.Surface(side1Edges=side1Edges1, name='soil-pore-left-bc-edge')
#: The surface 'soil-pore-left-bc-edge' has been created (1 edge).
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['soil-1'].edges
side1Edges1 = s1.findAt(((30.0, 5.0, 0.0), ))
a.Surface(side1Edges=side1Edges1, name='soil-right-pore-bc-edge')
#: The surface 'soil-right-pore-bc-edge' has been created (1 edge).
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['soil-1'].edges
side1Edges1 = s1.findAt(((4.0, 20.0, 0.0), ), ((-13.5, 20.0, 0.0), ), ((24.5, 
    20.0, 0.0), ))
a.Surface(side1Edges=side1Edges1, name='soil-up-before-pore-bc-edge')
#: The surface 'soil-up-before-pore-bc-edge' has been created (3 edges).
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['soil-1'].faces
faces1 = f1.findAt(((-15.333333, 17.333333, 0.0), ))
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['soil-1'].edges
side1Edges1 = s1.findAt(((-15.0, 0.0, 0.0), ))
a.Surface(side1Edges=side1Edges1, name='soil-bottom-before-pore-bc-edge')
#: The surface 'soil-bottom-before-pore-bc-edge' has been created (1 edge).
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['soil-1'].faces
faces1 = f1.findAt(((-15.333333, 17.333333, 0.0), ))
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['soil-1'].edges
edges1 = e1.findAt(((-8.0, 18.0, 0.0), ), ((-4.0, 12.0, 0.0), ), ((8.0, 14.0, 
    0.0), ), ((-13.5, 20.0, 0.0), ), ((24.5, 20.0, 0.0), ))
a.Set(edges=edges1, name='soil-up-after-pore-bc-edge')
#: The set 'soil-up-after-pore-bc-edge' has been created (5 edges).
del mdb.models['Model-1'].rootAssembly.surfaces['left-bc-edge']
del mdb.models['Model-1'].rootAssembly.surfaces['pore-surface']
del mdb.models['Model-1'].rootAssembly.surfaces['right-bc-edge']
del mdb.models['Model-1'].rootAssembly.surfaces['rock-bottom-bc-edge']
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
del mdb.models['Model-1'].rootAssembly.surfaces['soil-bottom-before-pore-bc-edge']
del mdb.models['Model-1'].rootAssembly.surfaces['soil-pore-left-bc-edge']
del mdb.models['Model-1'].rootAssembly.surfaces['soil-right-pore-bc-edge']
del mdb.models['Model-1'].rootAssembly.surfaces['soil-up-before-pore-bc-edge']
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['soil-1'].edges
edges1 = e1.findAt(((4.0, 20.0, 0.0), ), ((-13.5, 20.0, 0.0), ), ((24.5, 20.0, 
    0.0), ))
a.Set(edges=edges1, name='soil-up-before-pore-bc-edge')
#: The set 'soil-up-before-pore-bc-edge' has been created (3 edges).
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['soil-1'].edges
edges1 = e1.findAt(((-30.0, 15.0, 0.0), ))
e2 = a.instances['rock-1'].edges
edges2 = e2.findAt(((-30.0, -1.25, 0.0), ))
a.Set(edges=edges1+edges2, name='left-bc')
#: The set 'left-bc' has been created (2 edges).
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['soil-1'].edges
edges1 = e1.findAt(((30.0, 5.0, 0.0), ))
e2 = a.instances['rock-1'].edges
edges2 = e2.findAt(((30.0, -3.75, 0.0), ))
a.Set(edges=edges1+edges2, name='right-bc')
#: The set 'right-bc' has been created (2 edges).
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['rock-1'].edges
edges1 = e1.findAt(((-15.0, -5.0, 0.0), ))
a.Set(edges=edges1, name='rock-bottom-bc')
#: The set 'rock-bottom-bc' has been created (1 edge).
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['rock-1'].faces
faces1 = f1.findAt(((10.0, -1.666667, 0.0), ))
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['rock-1'].edges
edges1 = e1.findAt(((15.0, 0.0, 0.0), ))
a.Set(edges=edges1, name='rock-up-bc')
#: The set 'rock-up-bc' has been created (1 edge).
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['soil-1'].edges
edges1 = e1.findAt(((-30.0, 15.0, 0.0), ))
a.Set(edges=edges1, name='soil-left-pore-bc-edge')
#: The set 'soil-left-pore-bc-edge' has been created (1 edge).
mdb.models['Model-1'].rootAssembly.sets.changeKey(fromName='rock-bottom-bc', 
    toName='rock-bottom-bc-edge')
mdb.models['Model-1'].rootAssembly.sets.changeKey(fromName='rock-up-bc', 
    toName='rock-up-bc-edge')
mdb.models['Model-1'].rootAssembly.sets.changeKey(fromName='left-bc', 
    toName='left-bc-edge')
mdb.models['Model-1'].rootAssembly.sets.changeKey(fromName='right-bc', 
    toName='right-bc-edge')
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['soil-1'].edges
edges1 = e1.findAt(((30.0, 5.0, 0.0), ))
a.Set(edges=edges1, name='soil-right-pore-bc-edge')
#: The set 'soil-right-pore-bc-edge' has been created (1 edge).
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['soil-1'].faces
faces1 = f1.findAt(((-15.333333, 17.333333, 0.0), ))
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['soil-1'].edges
edges1 = e1.findAt(((-15.0, 0.0, 0.0), ))
a.Set(edges=edges1, name='soil-bottom-pore-bc-edge')
#: The set 'soil-bottom-pore-bc-edge' has been created (1 edge).
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
region = a.sets['left-bc-edge']
mdb.models['Model-1'].DisplacementBC(name='left-bc', createStepName='Initial', 
    region=region, u1=SET, u2=SET, ur3=UNSET, amplitude=UNSET, 
    distributionType=UNIFORM, fieldName='', localCsys=None)
a = mdb.models['Model-1'].rootAssembly
region = a.sets['right-bc-edge']
mdb.models['Model-1'].DisplacementBC(name='right-bc', createStepName='Initial', 
    region=region, u1=SET, u2=SET, ur3=UNSET, amplitude=UNSET, 
    distributionType=UNIFORM, fieldName='', localCsys=None)
a = mdb.models['Model-1'].rootAssembly
region = a.sets['rock-bottom-bc-edge']
mdb.models['Model-1'].DisplacementBC(name='rock-bc', createStepName='Initial', 
    region=region, u1=SET, u2=SET, ur3=UNSET, amplitude=UNSET, 
    distributionType=UNIFORM, fieldName='', localCsys=None)
mdb.models['Model-1'].boundaryConditions.changeKey(fromName='rock-bc', 
    toName='rock-bottom-bc')
a = mdb.models['Model-1'].rootAssembly
region = a.sets['rock-up-bc-edge']
mdb.models['Model-1'].DisplacementBC(name='rock-up-bc', 
    createStepName='Initial', region=region, u1=SET, u2=SET, ur3=UNSET, 
    amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='execavation')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='gravity')
mdb.models['Model-1'].ExpressionField(name='AnalyticalField-1', localCsys=None, 
    description='', expression='20 -  Y ')
a = mdb.models['Model-1'].rootAssembly
region = a.sets['soil-left-pore-bc-edge']
mdb.models['Model-1'].PorePressureBC(name='left-pore-bc', 
    createStepName='gravity', region=region, fixed=OFF, distributionType=FIELD, 
    fieldName='AnalyticalField-1', magnitude=10000.0, amplitude=UNSET)
mdb.models['Model-1'].boundaryConditions['left-pore-bc'].move('gravity', 
    'Initial')
#* ValueError: Non-zero boundary condition in initial step.
a = mdb.models['Model-1'].rootAssembly
region = a.sets['soil-right-pore-bc-edge']
mdb.models['Model-1'].PorePressureBC(name='right-pore-bc', 
    createStepName='gravity', region=region, fixed=OFF, distributionType=FIELD, 
    fieldName='AnalyticalField-1', magnitude=10000.0, amplitude=UNSET)
a = mdb.models['Model-1'].rootAssembly
region = a.sets['soil-bottom-pore-bc-edge']
mdb.models['Model-1'].PorePressureBC(name='bottom-pore-bc', 
    createStepName='gravity', region=region, fixed=OFF, 
    distributionType=UNIFORM, fieldName='', magnitude=200000.0, 
    amplitude=UNSET)
a = mdb.models['Model-1'].rootAssembly
region = a.sets['soil-up-before-pore-bc-edge']
mdb.models['Model-1'].PorePressureBC(name='up-pore-bc', 
    createStepName='gravity', region=region, fixed=OFF, 
    distributionType=UNIFORM, fieldName='', magnitude=0.0, amplitude=UNSET)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='execavation')
a = mdb.models['Model-1'].rootAssembly
region = a.sets['soil-up-after-pore-bc-edge']
mdb.models['Model-1'].PorePressureBC(name='after-exe-up-pore-bc', 
    createStepName='execavation', region=region, fixed=OFF, 
    distributionType=UNIFORM, fieldName='', magnitude=0.0, amplitude=UNSET)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
a = mdb.models['Model-1'].rootAssembly
region = a.instances['soil-1'].sets['soil']
mdb.models['Model-1'].GeostaticStress(name='geo-soil', region=region, 
    stressMag1=0.0, vCoord1=20.0, stressMag2=323200.0, vCoord2=0.0, 
    lateralCoeff1=0.5, lateralCoeff2=None)
a = mdb.models['Model-1'].rootAssembly
region = a.instances['rock-1'].sets['rock']
mdb.models['Model-1'].GeostaticStress(name='geo-rock', region=region, 
    stressMag1=-323200.0, vCoord1=0.0, stressMag2=-473200.0, vCoord2=-5.0, 
    lateralCoeff1=0.5, lateralCoeff2=None)
mdb.models['Model-1'].predefinedFields['geo-soil'].setValues(
    stressMag2=-323200.0)
a = mdb.models['Model-1'].rootAssembly
region = a.instances['soil-1'].sets['soil']
mdb.models['Model-1'].VoidsRatio(name='void', region=region, voidsRatio1=0.64, 
    distributionType=UNIFORM, variation=CONSTANT_RATIO)
a = mdb.models['Model-1'].rootAssembly
region = a.instances['soil-1'].sets['soil']
mdb.models['Model-1'].PorePressure(name='pore', region=region, 
    porePressure1=10000.0, distributionType=FIELD, field='AnalyticalField-1', 
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
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='execavation')
a = mdb.models['Model-1'].rootAssembly
region = a.sets['soil-left-pore-bc-edge']
mdb.models['Model-1'].PorePressureBC(name='exe-left-pore-bc', 
    createStepName='execavation', region=region, fixed=OFF, 
    distributionType=UNIFORM, fieldName='', magnitude=10000.0, amplitude=UNSET)
a = mdb.models['Model-1'].rootAssembly
region = a.sets['soil-right-pore-bc-edge']
mdb.models['Model-1'].PorePressureBC(name='exe-right-pore-bc', 
    createStepName='execavation', region=region, fixed=OFF, 
    distributionType=FIELD, fieldName='AnalyticalField-1', magnitude=10000.0, 
    amplitude=UNSET)
mdb.models['Model-1'].boundaryConditions['exe-left-pore-bc'].setValues(
    distributionType=FIELD, fieldName='AnalyticalField-1')
a = mdb.models['Model-1'].rootAssembly
region = a.sets['soil-bottom-pore-bc-edge']
mdb.models['Model-1'].PorePressureBC(name='exe-bottom-pore-bc', 
    createStepName='execavation', region=region, fixed=OFF, 
    distributionType=UNIFORM, fieldName='', magnitude=200000.0, 
    amplitude=UNSET)
a = mdb.models['Model-1'].rootAssembly
region = a.sets['soil-up-before-pore-bc-edge']
mdb.models['Model-1'].PorePressureBC(name='exe-up-pore-bc', 
    createStepName='execavation', region=region, fixed=OFF, 
    distributionType=UNIFORM, fieldName='', magnitude=0.0, amplitude=UNSET)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='injection')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='gravity')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='injection')
mdb.models['Model-1'].loads['pore'].suppress()
mdb.models['Model-1'].loads['pore'].resume()
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['soil-1'], )
a.seedPartInstance(regions=partInstances, size=1.0, deviationFactor=0.1, 
    minSizeFactor=0.1)
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['rock-1'], )
a.seedPartInstance(regions=partInstances, size=1.0, deviationFactor=0.1, 
    minSizeFactor=0.1)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['soil-1'].faces
pickedRegions = f1.findAt(((-2.666667, 14.666667, 0.0), ), ((-15.333333, 
    17.333333, 0.0), ))
a.setMeshControls(regions=pickedRegions, elemShape=QUAD, algorithm=MEDIAL_AXIS)
elemType1 = mesh.ElemType(elemCode=CPE4P, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=UNKNOWN_TRI, elemLibrary=STANDARD)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['soil-1'].faces
faces1 = f1.findAt(((-2.666667, 14.666667, 0.0), ), ((-15.333333, 17.333333, 
    0.0), ))
pickedRegions =(faces1, )
a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['soil-1'], )
a.generateMesh(regions=partInstances)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['rock-1'].faces
pickedRegions = f1.findAt(((10.0, -1.666667, 0.0), ))
a.setMeshControls(regions=pickedRegions, elemShape=QUAD, algorithm=MEDIAL_AXIS)
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['rock-1'], )
a.generateMesh(regions=partInstances)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
mdb.models['Model-1'].loads['pore'].suppress()
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['Job-centrifuge'].writeInput(consistencyChecking=OFF)
#: The job input file has been written to "Job-centrifuge.inp".
mdb.save()
#: The model database has been saved to "E:\workingspace\centrifuge\command-base\centrifuge.cae".
