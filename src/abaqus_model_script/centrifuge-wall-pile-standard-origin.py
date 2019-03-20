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
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(0.0, 20.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(50.0, 20.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(50.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(18.5, 20.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(19.0, 20.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(18.5, 5.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(19.0, 5.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(15.5, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(15.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(15.0, 12.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(15.5, 12.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(
    0.0, 20.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 10.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 10.0), 
    ))
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
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(18.5, 20.0), point2=
    (18.5, 5.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((18.5, 12.5))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((18.5, 12.5), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((9.25, 20.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((18.5, 12.5))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((9.25, 20.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    18.5, 12.5), ))
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
    (50.0, 20.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((34.5, 20.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((34.5, 20.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((19.0, 12.5))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((34.5, 20.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((19.0, 12.5), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    34.5, 20.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(50.0, 20.0), point2=
    (50.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((50.0, 10.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((50.0, 10.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((34.5, 20.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((50.0, 10.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((34.5, 20.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    50.0, 10.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(50.0, 0.0), point2=(
    15.5, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((32.75, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((32.75, 0.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((50.0, 10.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((32.75, 0.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((50.0, 10.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    32.75, 0.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(15.5, 0.0), point2=(
    15.5, 12.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.5, 6.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.5, 6.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((32.75, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.5, 6.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((32.75, 0.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    15.5, 6.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(15.5, 12.0), point2=
    (15.0, 12.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.25, 12.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.25, 
    12.0), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.5, 6.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.25, 12.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((15.5, 6.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    15.25, 12.0), ))
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
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='clay', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['clay'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=2.69, name='__profile__', 
    sheetSize=107.7, transform=
    mdb.models['Model-1'].parts['clay'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['clay'].faces.findAt((10.0, 4.0, 
    0.0), (0.0, 0.0, 1.0)), sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, 
    origin=(25.106817, 10.005322, 0.0)))
mdb.models['Model-1'].parts['clay'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-9.606817, 1.994678)
    , point2=(-9.606817, 9.9946779999941))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.606817, 
    5.994678))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.606817, 
    5.994678), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.856817, 
    1.994678))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.606817, 
    5.994678))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.856817, 
    1.994678), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.606817, 
    5.994678), ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-9.606817, 
    9.994678))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-15.856817, 
    9.994678))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-9.606817, 
    9.9946779999941), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-15.856817, 
    9.994678), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-10.106817, 
    1.994678), point2=(-10.106817, 9.9946779999941))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-10.106817, 
    5.994678))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-10.106817, 
    5.994678), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-10.106817, 
    -4.005322))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-10.106817, 
    5.994678))
mdb.models['Model-1'].sketches['__profile__'].ParallelConstraint(addUndoState=
    False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-10.106817, 
    -4.005322), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-10.106817, 
    5.994678), ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-10.106817, 
    9.994678))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-15.856817, 
    9.994678))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-10.106817, 
    9.9946779999941), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-15.856817, 
    9.994678), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-9.606817, 1.994678)
    , point2=(-6.60681700003995, 1.994678))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-8.106817, 
    1.994678))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-8.106817, 
    1.994678), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.856817, 
    1.994678))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-8.106817, 
    1.994678))
mdb.models['Model-1'].sketches['__profile__'].ParallelConstraint(addUndoState=
    False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-9.856817, 
    1.994678), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-8.106817, 
    1.994678), ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-6.606817, 
    1.994678))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-6.606817, 
    2.494678))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
    -6.60681700003995, 1.994678), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-6.606817, 
    2.494678), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-10.106817, 
    1.994678), point2=(-25.10681700004, 1.994678))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-17.606817, 
    1.994678))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-17.606817, 
    1.994678), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-10.106817, 
    -4.005322))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-17.606817, 
    1.994678))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-10.106817, 
    -4.005322), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-17.606817, 
    1.994678), ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-25.106817, 
    1.994678))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-25.106817, 
    -0.005322))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
    -25.10681700004, 1.994678), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-25.106817, 
    -0.005322), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-6.106817, 
    -5.005322), point2=(-6.106817, -10.0053220000059))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-6.106817, 
    -7.505322))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-6.106817, 
    -7.505322), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-6.106817, 
    2.494678))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-6.106817, 
    -7.505322))
mdb.models['Model-1'].sketches['__profile__'].ParallelConstraint(addUndoState=
    False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-6.106817, 
    2.494678), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-6.106817, 
    -7.505322), ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-6.106817, 
    -10.005322))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.643183, 
    -10.005322))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-6.106817, 
    -10.0053220000059), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.643183, 
    -10.005322), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-6.606817, 
    -5.005322), point2=(-6.606817, -10.0053220000059))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-6.606817, 
    -7.505322))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-6.606817, 
    -7.505322), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-6.356817, 
    -5.005322))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-6.606817, 
    -7.505322))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-6.356817, 
    -5.005322), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-6.606817, 
    -7.505322), ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-6.606817, 
    -10.005322))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.643183, 
    -10.005322))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((-6.606817, 
    -10.0053220000059), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.643183, 
    -10.005322), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-6.106817, 
    -5.005322), point2=(24.8931829999601, -5.005322))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((9.393183, 
    -5.005322))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((9.393183, 
    -5.005322), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-6.106817, 
    2.494678))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((9.393183, 
    -5.005322))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-6.106817, 
    2.494678), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((9.393183, 
    -5.005322), ))
mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((24.893183, 
    -5.005322))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((24.893183, 
    -0.005322))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices.findAt((
    24.8931829999601, -5.005322), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((24.893183, 
    -0.005322), ))
mdb.models['Model-1'].parts['clay'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['clay'].faces.findAt(((10.0, 4.0, 0.0), )), 
    sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(18.5, 20.0))
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
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(15.5, -3.0))
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(15.0, 12.0), 
    point2=(15.5, -3.0))
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='pile', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['pile'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['clay'].Surface(name='no_excavation', side1Edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt(((18.5, 10.25, 0.0), ), ((
    19.0, 8.75, 0.0), ), ((18.625, 5.0, 0.0), ), ))
mdb.models['Model-1'].parts['clay'].Surface(name='excavation', side1Edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt(((18.5, 18.0, 0.0), )))
mdb.models['Model-1'].parts['clay'].Set(faces=
    mdb.models['Model-1'].parts['clay'].faces.findAt(((10.0, 8.0, 0.0), ), ((
    10.0, 17.333333, 0.0), ), ((15.333333, 17.333333, 0.0), ), ((16.5, 
    14.666667, 0.0), ), ((17.5, 9.666667, 0.0), ), ((29.333333, 10.0, 0.0), ), 
    ((18.833333, 3.333333, 0.0), ), ((29.333333, 1.666667, 0.0), ), ), name=
    'clay')
mdb.models['Model-1'].parts['clay'].Set(edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt(((0.0, 3.0, 0.0), ), ((
    0.0, 14.0, 0.0), ), ), name='left_bc')
mdb.models['Model-1'].parts['clay'].Set(edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt(((50.0, 16.25, 0.0), ), ((
    50.0, 3.75, 0.0), ), ), name='right_bc')
mdb.models['Model-1'].parts['clay'].Set(edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt(((11.25, 0.0, 0.0), ), ((
    17.75, 0.0, 0.0), ), ((18.875, 0.0, 0.0), ), ((42.25, 0.0, 0.0), ), ), 
    name='bottom_bc')
mdb.models['Model-1'].parts['clay'].Set(edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt(((15.0, 9.0, 0.0), ), ((
    15.5, 3.0, 0.0), ), ), name='pile_int_lateral')
mdb.models['Model-1'].parts['clay'].Set(edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt(((11.25, 12.0, 0.0), ), ((
    11.25, 0.0, 0.0), ), ((3.75, 20.0, 0.0), ), ((16.25, 12.0, 0.0), ), ((
    16.25, 20.0, 0.0), ), ((17.75, 0.0, 0.0), ), ((26.75, 5.0, 0.0), ), ((
    26.75, 20.0, 0.0), ), ((42.25, 0.0, 0.0), ), ), name='lateral_edge')
mdb.models['Model-1'].parts['clay'].sets.changeKey(fromName='lateral_edge', 
    toName='horizon_edge')
mdb.models['Model-1'].parts['clay'].Set(edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt(((0.0, 3.0, 0.0), ), ((
    15.0, 9.0, 0.0), ), ((15.0, 18.0, 0.0), ), ((0.0, 14.0, 0.0), ), ((15.5, 
    18.0, 0.0), ), ((18.5, 18.0, 0.0), ), ((15.5, 3.0, 0.0), ), ((18.5, 3.75, 
    0.0), ), ((18.5, 10.25, 0.0), ), ((50.0, 16.25, 0.0), ), ((19.0, 8.75, 
    0.0), ), ((19.0, 1.25, 0.0), ), ((50.0, 3.75, 0.0), ), ), name=
    'vertical_edge')
mdb.models['Model-1'].parts['clay'].Surface(name='pile_int', side1Edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt(((15.0, 9.0, 0.0), ), ((
    15.375, 12.0, 0.0), ), ((15.5, 3.0, 0.0), ), ))
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=1.07, name='__profile__', 
    sheetSize=43.13, transform=
    mdb.models['Model-1'].parts['pile'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['pile'].faces.findAt((15.333333, 
    7.0, 0.0), (0.0, 0.0, 1.0)), sketchPlaneSide=SIDE1, 
    sketchOrientation=RIGHT, origin=(15.25, 4.5, 0.0)))
mdb.models['Model-1'].parts['pile'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(0.25, -4.5))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-0.25, -4.5))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-0.25, -4.5), 
    point2=(0.25, -4.5))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, -4.5))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, -4.5), 
    ))
mdb.models['Model-1'].parts['pile'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['pile'].faces.findAt(((15.333333, 7.0, 0.0), ))
    , sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['pile'].Set(faces=
    mdb.models['Model-1'].parts['pile'].faces.findAt(((15.333333, -1.0, 0.0), 
    ), ((15.166667, 4.0, 0.0), ), ), name='pile')
mdb.models['Model-1'].parts['pile'].Set(edges=
    mdb.models['Model-1'].parts['pile'].edges.findAt(((15.5, 3.0, 0.0), ), ((
    15.0, 9.0, 0.0), ), ), name='pile_int_lateral')
mdb.models['Model-1'].parts['pile'].Set(edges=
    mdb.models['Model-1'].parts['pile'].edges.findAt(((15.0, -0.75, 0.0), ), ((
    15.5, -2.25, 0.0), ), ), name='pile_no_int_lateral')
mdb.models['Model-1'].parts['pile'].Surface(name='pile_int', side1Edges=
    mdb.models['Model-1'].parts['pile'].edges.findAt(((15.5, 3.0, 0.0), ), ((
    15.375, 12.0, 0.0), ), ((15.0, 9.0, 0.0), ), ))
mdb.models['Model-1'].parts['pile'].Set(edges=
    mdb.models['Model-1'].parts['pile'].edges.findAt(((15.125, -3.0, 0.0), )), 
    name='bottom')
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=1.37, name='__profile__', 
    sheetSize=55.17, transform=
    mdb.models['Model-1'].parts['wall'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['wall'].faces.findAt((18.833333, 
    15.0, 0.0), (0.0, 0.0, 1.0)), sketchPlaneSide=SIDE1, 
    sketchOrientation=RIGHT, origin=(18.75, 12.5, 0.0)))
mdb.models['Model-1'].parts['wall'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(0.25, -0.5))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-0.25, -0.5))
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
mdb.models['Model-1'].parts['wall'].Set(faces=
    mdb.models['Model-1'].parts['wall'].faces.findAt(((18.833333, 9.666667, 
    0.0), ), ((18.666667, 14.666667, 0.0), ), ), name='wall')
mdb.models['Model-1'].parts['wall'].Surface(name='excavation', side1Edges=
    mdb.models['Model-1'].parts['wall'].edges.findAt(((18.5, 18.0, 0.0), )))
mdb.models['Model-1'].parts['wall'].Surface(name='no_excavation', side1Edges=
    mdb.models['Model-1'].parts['wall'].edges.findAt(((18.5, 10.25, 0.0), ), ((
    18.625, 5.0, 0.0), ), ((19.0, 6.75, 0.0), ), ((19.0, 14.0, 0.0), ), ))
mdb.models['Model-1'].parts['wall'].Set(edges=
    mdb.models['Model-1'].parts['wall'].edges.findAt(((18.5, 10.25, 0.0), ), ((
    19.0, 6.75, 0.0), ), ((19.0, 14.0, 0.0), ), ((18.5, 18.0, 0.0), ), ), name=
    'lateral')
mdb.models['Model-1'].parts['wall'].Set(edges=
    mdb.models['Model-1'].parts['wall'].edges.findAt(((18.625, 5.0, 0.0), )), 
    name='bottom')
mdb.models['Model-1'].parts['clay'].Set(faces=
    mdb.models['Model-1'].parts['clay'].faces.findAt(((10.0, 17.333333, 0.0), 
    )), name='excavation')
mdb.models['Model-1'].Material(name='clay')
mdb.models['Model-1'].materials['clay'].Density(table=((1616.0, ), ))
mdb.models['Model-1'].materials['clay'].Elastic(table=((12000000.0, 0.3), ))
mdb.models['Model-1'].materials['clay'].MaxpsDamageInitiation(table=((20000.0, 
    ), ))
mdb.models['Model-1'].materials['clay'].maxpsDamageInitiation.DamageEvolution(
    mixedModeBehavior=POWER_LAW, power=1.0, table=((10000.0, 10000.0, 10000.0), 
    ), type=ENERGY)
mdb.models['Model-1'].materials['clay'].maxpsDamageInitiation.DamageStabilizationCohesive(
    cohesiveCoeff=0.0001)
mdb.models['Model-1'].materials['clay'].GapFlow(table=((1e-06, ), ))
mdb.models['Model-1'].materials['clay'].FluidLeakoff(table=((5.879e-16, 
    5.879e-16), ))
mdb.models['Model-1'].materials['clay'].Permeability(inertialDragCoefficient=
    0.142887, specificWeight=10000.0, table=((2.518e-05, 0.0), ))
mdb.models['Model-1'].Material(name='pile_wall')
mdb.models['Model-1'].materials['pile_wall'].Density(table=((1616.0, ), ))
mdb.models['Model-1'].materials['pile_wall'].Elastic(table=((90000000000.0, 
    0.1), ))
mdb.models['Model-1'].HomogeneousSolidSection(material='clay', name='clay', 
    thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='pile_wall', name='pile'
    , thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='pile_wall', name='wall'
    , thickness=None)
mdb.models['Model-1'].parts['clay'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['clay'].sets['clay'], sectionName='clay', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['pile'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['pile'].sets['pile'], sectionName='pile', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['wall'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['wall'].sets['wall'], sectionName='wall', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(17.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(17.0, 1.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(17.0, 0.0), point2=(
    17.0, 1.0))
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
mdb.models['Model-1'].parts['crack'].Set(edges=
    mdb.models['Model-1'].parts['crack'].edges.findAt(((17.0, 0.25, 0.0), )), 
    name='crack')
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='clay-1', part=
    mdb.models['Model-1'].parts['clay'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='crack-1', part=
    mdb.models['Model-1'].parts['crack'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='pile-1', part=
    mdb.models['Model-1'].parts['pile'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='wall-1', part=
    mdb.models['Model-1'].parts['wall'])
mdb.models['Model-1'].GeostaticStep(name='gravity', previous='Initial')
mdb.models['Model-1'].StaticStep(matrixSolver=DIRECT, matrixStorage=UNSYMMETRIC
    , name='release_wall', previous='gravity')
mdb.models['Model-1'].StaticStep(matrixSolver=DIRECT, matrixStorage=UNSYMMETRIC
    , name='release_pile', previous='release_wall')
mdb.models['Model-1'].StaticStep(matrixSolver=DIRECT, matrixStorage=UNSYMMETRIC
    , name='excavation', previous='release_pile')
mdb.models['Model-1'].SoilsStep(cetol=None, creep=OFF, end=None, initialInc=
    0.05, matrixSolver=DIRECT, matrixStorage=UNSYMMETRIC, maxInc=5.0, minInc=
    1e-12, name='injection', previous='excavation', timePeriod=100.0, utol=
    1000000000.0)
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValuesInStep(
    stepName='release_wall', variables=('S', 'PE', 'PEEQ', 'PEMAG', 'LE', 'U', 
    'RF', 'CF', 'CSTRESS', 'CDISP', 'PHILSM', 'PSILSM'))
mdb.models['Model-1'].ContactProperty('pile_wall')
mdb.models['Model-1'].interactionProperties['pile_wall'].TangentialBehavior(
    dependencies=0, directionality=ISOTROPIC, elasticSlipStiffness=None, 
    formulation=PENALTY, fraction=0.005, maximumElasticSlip=FRACTION, 
    pressureDependency=OFF, shearStressLimit=None, slipRateDependency=OFF, 
    table=((0.15, ), ), temperatureDependency=OFF)
mdb.models['Model-1'].interactionProperties['pile_wall'].NormalBehavior(
    allowSeparation=ON, constraintEnforcementMethod=DEFAULT, 
    pressureOverclosure=HARD)
mdb.models['Model-1'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='Initial', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='pile_wall', master=
    mdb.models['Model-1'].rootAssembly.instances['wall-1'].surfaces['excavation']
    , name='clay_wall_no_excavation', slave=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].surfaces['excavation']
    , sliding=FINITE, thickness=ON)
mdb.models['Model-1'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='Initial', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='pile_wall', master=
    mdb.models['Model-1'].rootAssembly.instances['pile-1'].surfaces['pile_int']
    , name='clay_pile', slave=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].surfaces['pile_int']
    , sliding=FINITE, thickness=ON)
mdb.models['Model-1'].interactions.changeKey(fromName='clay_wall_no_excavation'
    , toName='clay_wall_excavation')
mdb.models['Model-1'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='Initial', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='pile_wall', master=
    mdb.models['Model-1'].rootAssembly.instances['wall-1'].surfaces['no_excavation']
    , name='clay_wall_no_excavation', slave=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].surfaces['no_excavation']
    , sliding=FINITE, thickness=ON)
mdb.models['Model-1'].rootAssembly.engineeringFeatures.XFEMCrack(crackDomain=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].sets['clay'], 
    crackLocation=
    mdb.models['Model-1'].rootAssembly.instances['crack-1'].sets['crack'], 
    name='Crack-1')
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['crack-1'].edges.findAt(((
    17.0, 0.25, 0.0), )), faces=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].faces.findAt(((10.0, 
    8.0, 0.0), (0.0, 0.0, 1.0)), ((10.0, 17.333333, 0.0), (0.0, 0.0, 1.0)), ((
    15.333333, 17.333333, 0.0), (0.0, 0.0, 1.0)), ((16.5, 14.666667, 0.0), (
    0.0, 0.0, 1.0)), ((17.5, 9.666667, 0.0), (0.0, 0.0, 1.0)), ((29.333333, 
    10.0, 0.0), (0.0, 0.0, 1.0)), ((18.833333, 3.333333, 0.0), (0.0, 0.0, 
    1.0)), ((29.333333, 1.666667, 0.0), (0.0, 0.0, 1.0)), )+\
    mdb.models['Model-1'].rootAssembly.instances['pile-1'].faces.findAt(((
    15.333333, -1.0, 0.0), (0.0, 0.0, 1.0)), ((15.166667, 4.0, 0.0), (0.0, 0.0, 
    1.0)), )+\
    mdb.models['Model-1'].rootAssembly.instances['wall-1'].faces.findAt(((
    18.833333, 9.666667, 0.0), (0.0, 0.0, 1.0)), ((18.666667, 14.666667, 0.0), 
    (0.0, 0.0, 1.0)), ), name='manual_whole')
mdb.models['Model-1'].Gravity(comp2=-10.0, createStepName='gravity', 
    distributionType=UNIFORM, field='', name='gravity', region=
    mdb.models['Model-1'].rootAssembly.sets['manual_whole'])
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='gravity', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'left_bc', region=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].sets['left_bc'], u1=
    0.0, u2=UNSET, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='gravity', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'right_bc', region=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].sets['right_bc'], 
    u1=0.0, u2=UNSET, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='gravity', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'bottom_bc', region=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].sets['bottom_bc'], 
    u1=0.0, u2=0.0, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='gravity', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'wall_lateral', region=
    mdb.models['Model-1'].rootAssembly.instances['wall-1'].sets['lateral'], u1=
    0.0, u2=UNSET, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='gravity', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'wall_bottom', region=
    mdb.models['Model-1'].rootAssembly.instances['wall-1'].sets['bottom'], u1=
    UNSET, u2=0.0, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='gravity', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'pile_no_int_lateral', region=
    mdb.models['Model-1'].rootAssembly.instances['pile-1'].sets['pile_no_int_lateral']
    , u1=0.0, u2=0.0, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='gravity', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'pile_int_lateral', region=
    mdb.models['Model-1'].rootAssembly.instances['pile-1'].sets['pile_int_lateral']
    , u1=0.0, u2=UNSET, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='gravity', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'pile_bottom', region=
    mdb.models['Model-1'].rootAssembly.instances['pile-1'].sets['bottom'], u1=
    0.0, u2=0.0, ur3=UNSET)
mdb.models['Model-1'].VoidsRatio(distributionType=UNIFORM, name='void', region=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].sets['clay'], 
    variation=CONSTANT_RATIO, voidsRatio1=0.64)
mdb.models['Model-1'].ExpressionField(description='', expression='20 -  Y ', 
    localCsys=None, name='AnalyticalField-1')
mdb.models['Model-1'].PorePressure(distributionType=FIELD, field=
    'AnalyticalField-1', name='pore', porePressure1=10000.0, region=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].sets['clay'], 
    variation=CONSTANT_RATIO)
mdb.models['Model-1'].parts['clay'].seedEdgeBySize(constraint=FINER, 
    deviationFactor=0.1, edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt(((11.25, 12.0, 0.0), ), ((
    11.25, 0.0, 0.0), ), ((3.75, 20.0, 0.0), ), ((16.25, 12.0, 0.0), ), ((
    16.25, 20.0, 0.0), ), ((17.75, 0.0, 0.0), ), ((26.75, 5.0, 0.0), ), ((
    26.75, 20.0, 0.0), ), ((42.25, 0.0, 0.0), ), ), size=1.0)
mdb.models['Model-1'].parts['clay'].seedEdgeBySize(constraint=FINER, 
    deviationFactor=0.1, edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt(((0.0, 3.0, 0.0), ), ((
    15.0, 9.0, 0.0), ), ((15.0, 18.0, 0.0), ), ((0.0, 14.0, 0.0), ), ((15.5, 
    18.0, 0.0), ), ((18.5, 18.0, 0.0), ), ((15.5, 3.0, 0.0), ), ((18.5, 3.75, 
    0.0), ), ((18.5, 10.25, 0.0), ), ((50.0, 16.25, 0.0), ), ((19.0, 8.75, 
    0.0), ), ((19.0, 1.25, 0.0), ), ((50.0, 3.75, 0.0), ), ), size=1.0)
mdb.models['Model-1'].parts['clay'].setMeshControls(algorithm=MEDIAL_AXIS, 
    elemShape=QUAD, regions=mdb.models['Model-1'].parts['clay'].faces.findAt(((
    10.0, 8.0, 0.0), ), ((10.0, 17.333333, 0.0), ), ((15.333333, 17.333333, 
    0.0), ), ((16.5, 14.666667, 0.0), ), ((17.5, 9.666667, 0.0), ), ((
    29.333333, 10.0, 0.0), ), ((18.833333, 3.333333, 0.0), ), ((29.333333, 
    1.666667, 0.0), ), ))
mdb.models['Model-1'].parts['clay'].setElementType(elemTypes=(ElemType(
    elemCode=CPE4P, elemLibrary=STANDARD), ElemType(elemCode=UNKNOWN_TRI, 
    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['clay'].faces.findAt(((10.0, 8.0, 0.0), ), ((
    10.0, 17.333333, 0.0), ), ((15.333333, 17.333333, 0.0), ), ((16.5, 
    14.666667, 0.0), ), ((17.5, 9.666667, 0.0), ), ((29.333333, 10.0, 0.0), ), 
    ((18.833333, 3.333333, 0.0), ), ((29.333333, 1.666667, 0.0), ), ), ))
mdb.models['Model-1'].parts['clay'].generateMesh()
mdb.models['Model-1'].parts['pile'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=1.0)
mdb.models['Model-1'].parts['pile'].setMeshControls(algorithm=MEDIAL_AXIS, 
    elemShape=QUAD, regions=mdb.models['Model-1'].parts['pile'].faces.findAt(((
    15.333333, -1.0, 0.0), ), ((15.166667, 4.0, 0.0), ), ))
mdb.models['Model-1'].parts['pile'].setElementType(elemTypes=(ElemType(
    elemCode=CPE4, elemLibrary=STANDARD), ElemType(elemCode=CPE3, 
    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['pile'].faces.findAt(((15.333333, -1.0, 0.0), 
    ), ((15.166667, 4.0, 0.0), ), ), ))
mdb.models['Model-1'].parts['pile'].generateMesh()
mdb.models['Model-1'].parts['wall'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=1.0)
mdb.models['Model-1'].parts['wall'].setMeshControls(algorithm=MEDIAL_AXIS, 
    elemShape=QUAD, regions=mdb.models['Model-1'].parts['wall'].faces.findAt(((
    18.833333, 9.666667, 0.0), ), ((18.666667, 14.666667, 0.0), ), ))
mdb.models['Model-1'].parts['wall'].setElementType(elemTypes=(ElemType(
    elemCode=CPE4, elemLibrary=STANDARD), ElemType(elemCode=CPE3, 
    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['wall'].faces.findAt(((18.833333, 9.666667, 
    0.0), ), ((18.666667, 14.666667, 0.0), ), ), ))
mdb.models['Model-1'].parts['wall'].generateMesh()
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].boundaryConditions['wall_bottom'].deactivate(
    'release_wall')
mdb.models['Model-1'].boundaryConditions['wall_lateral'].deactivate(
    'release_wall')
mdb.models['Model-1'].boundaryConditions['pile_int_lateral'].deactivate(
    'release_pile')
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name='Job-standard', nodalOutputPrecision=
    SINGLE, numCpus=1, numGPUs=0, queue=None, resultsFormat=ODB, scratch='', 
    type=ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)

mdb.models['Model-1'].materials.changeKey(fromName='pile_wall', toName=
    'manual_structure')
mdb.models['Model-1'].sections['pile'].setValues(material='manual_structure', 
    thickness=None)
mdb.models['Model-1'].sections['wall'].setValues(material='manual_structure', 
    thickness=None)
mdb.jobs['Job-standard'].submit(consistencyChecking=OFF, datacheckJob=True)

mdb.models['Model-1'].steps['gravity'].setValues(matrixSolver=DIRECT, 
    matrixStorage=UNSYMMETRIC)
mdb.models['Model-1'].parts['clay'].Set(edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt(((18.5, 18.0, 0.0), ), ((
    18.5, 10.25, 0.0), ), ((19.0, 8.75, 0.0), ), ), name='wall_lateral')
mdb.models['Model-1'].parts['clay'].Set(edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt(((18.625, 5.0, 0.0), )), 
    name='wall_bottom')
mdb.models['Model-1'].parts['clay'].Set(edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt(((15.0, 9.0, 0.0), ), ((
    15.5, 3.0, 0.0), ), ), name='pile_lateral')
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='gravity', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'clay_wall_lateral', region=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].sets['wall_lateral']
    , u1=0.0, u2=UNSET, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='gravity', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'clay_wall_bottom', region=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].sets['wall_bottom'], 
    u1=UNSET, u2=0.0, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='gravity', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'clay_pile_lateral', region=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].sets['pile_lateral']
    , u1=0.0, u2=UNSET, ur3=UNSET)
mdb.models['Model-1'].boundaryConditions['clay_pile_lateral'].deactivate(
    'release_pile')
mdb.models['Model-1'].boundaryConditions['clay_wall_bottom'].deactivate(
    'release_wall')
mdb.models['Model-1'].boundaryConditions['clay_wall_lateral'].deactivate(
    'release_wall')
# Save by augustus on 2019_01_09-23.48.17; build 2016 2015_09_25-04.31.09 126547
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
mdb.models['Model-1'].ModelChange(activeInStep=False, createStepName=
    'excavation', includeStrain=False, name='excavation', region=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].sets['excavation'])

# Save by augustus on 2019_01_10-15.09.19; build 2016 2015_09_25-04.31.09 126547
