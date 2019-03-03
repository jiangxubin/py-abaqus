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
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(0.0, 25.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(80.5, 25.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(80.5, 5.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(0.0, 5.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(20.0, 25.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(20.5, 25.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(20.0, 5.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(20.5, 5.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 5.0), point2=(
    0.0, 25.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 15.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 15.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 25.0), point2=(
    20.0, 25.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((10.0, 25.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((10.0, 25.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 15.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((10.0, 25.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 15.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    10.0, 25.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(20.0, 25.0), point2=
    (20.0, 5.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.0, 15.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.0, 15.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((10.0, 25.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.0, 15.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((10.0, 25.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    20.0, 15.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(20.0, 5.0), point2=(
    20.5, 5.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.25, 5.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.25, 5.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.0, 15.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.25, 5.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.0, 15.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    20.25, 5.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(20.5, 5.0), point2=(
    20.5, 25.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.5, 15.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.5, 15.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.25, 5.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.5, 15.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.25, 5.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    20.5, 15.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(20.5, 25.0), point2=
    (80.5, 25.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((50.5, 25.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((50.5, 25.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.5, 15.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((50.5, 25.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.5, 15.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    50.5, 25.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(80.5, 25.0), point2=
    (80.5, 5.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((80.5, 15.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((80.5, 15.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((50.5, 25.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((80.5, 15.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((50.5, 25.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    80.5, 15.0), ))
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(0.0, 5.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(0.0, 25.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(20.0, 25.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(20.0, 10.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(20.5, 10.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(20.5, 25.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(80.5, 25.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(80.5, 5.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 5.0), point2=(
    80.5, 5.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((40.25, 5.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((40.25, 5.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(80.5, 5.0), point2=(
    80.5, 25.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((80.5, 15.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((80.5, 15.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((40.25, 5.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((80.5, 15.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((40.25, 5.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    80.5, 15.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(80.5, 25.0), point2=
    (20.5, 25.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((50.5, 25.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((50.5, 25.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((80.5, 15.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((50.5, 25.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((80.5, 15.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    50.5, 25.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(20.5, 25.0), point2=
    (20.5, 10.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.5, 17.5))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.5, 17.5), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((50.5, 25.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.5, 17.5))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((50.5, 25.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    20.5, 17.5), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(20.5, 10.0), point2=
    (20.0, 10.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.25, 10.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.25, 
    10.0), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.5, 17.5))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.25, 10.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.5, 17.5), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    20.25, 10.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(20.0, 10.0), point2=
    (20.0, 25.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.0, 17.5))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.0, 17.5), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.25, 10.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.0, 17.5))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.25, 
    10.0), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.0, 17.5), 
    ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(20.0, 25.0), point2=
    (0.0, 25.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((10.0, 25.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((10.0, 25.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.0, 17.5))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((10.0, 25.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.0, 17.5), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    10.0, 25.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 25.0), point2=(
    0.0, 5.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 15.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 15.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((10.0, 25.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 15.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((10.0, 25.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    0.0, 15.0), ))
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='up-soil', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['up-soil'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(20.0, 10.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(20.0, 25.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(20.5, 10.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(20.5, 20.0))
mdb.models['Model-1'].sketches['__profile__'].undo()
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(20.5, 25.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(20.0, 25.0), point2=
    (20.5, 25.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.25, 25.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.25, 
    25.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(20.5, 25.0), point2=
    (20.5, 10.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.5, 17.5))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.5, 17.5), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.25, 25.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.5, 17.5))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.25, 
    25.0), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.5, 17.5), 
    ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(20.5, 10.0), point2=
    (20.0, 10.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.25, 10.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.25, 
    10.0), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.5, 17.5))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.25, 10.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.5, 17.5), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    20.25, 10.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(20.0, 10.0), point2=
    (20.0, 25.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.0, 17.5))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.0, 17.5), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.25, 10.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.0, 17.5))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.25, 
    10.0), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((20.0, 17.5), 
    ))
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='wall', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['wall'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(18.5, 5.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(18.5, 6.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(18.5, 6.0), point2=(
    18.5, 5.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((18.5, 5.5))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((18.5, 5.5), 
    ))
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='crack', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['crack'].BaseWire(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['up-soil'].DatumPointByCoordinate(coords=(20.0, 
    5.0, 0.0))
mdb.models['Model-1'].parts['up-soil'].DatumPointByCoordinate(coords=(20.5, 
    5.0, 0.0))
mdb.models['Model-1'].parts['up-soil'].DatumPointByCoordinate(coords=(20.0, 
    10.0, 0.0))
mdb.models['Model-1'].parts['up-soil'].DatumPointByCoordinate(coords=(20.5, 
    10.0, 0.0))
mdb.models['Model-1'].parts['up-soil'].DatumPointByCoordinate(coords=(80.5, 
    10.0, 0.0))
mdb.models['Model-1'].parts['up-soil'].DatumPointByCoordinate(coords=(20.0, 
    17.0, 0.0))
mdb.models['Model-1'].parts['up-soil'].DatumPointByCoordinate(coords=(20.5, 
    17.0, 0.0))
del mdb.models['Model-1'].parts['up-soil'].features['Datum pt-7']
mdb.models['Model-1'].parts['up-soil'].DatumPointByCoordinate(coords=(0.0, 
    17.0, 0.0))
mdb.models['Model-1'].parts['up-soil'].PartitionFaceByShortestPath(faces=
    mdb.models['Model-1'].parts['up-soil'].faces.findAt(((13.333333, 20.0, 
    0.0), )), point1=mdb.models['Model-1'].parts['up-soil'].datums[4], point2=
    mdb.models['Model-1'].parts['up-soil'].datums[2])
mdb.models['Model-1'].parts['up-soil'].PartitionFaceByShortestPath(faces=
    mdb.models['Model-1'].parts['up-soil'].faces.findAt(((13.333333, 6.666667, 
    0.0), )), point1=mdb.models['Model-1'].parts['up-soil'].datums[9], point2=
    mdb.models['Model-1'].parts['up-soil'].datums[7])
mdb.models['Model-1'].parts['up-soil'].PartitionFaceByShortestPath(faces=
    mdb.models['Model-1'].parts['up-soil'].faces.findAt(((20.166667, 8.333333, 
    0.0), )), point1=mdb.models['Model-1'].parts['up-soil'].datums[5], point2=
    mdb.models['Model-1'].parts['up-soil'].datums[6])
mdb.models['Model-1'].parts['up-soil'].PartitionFaceByShortestPath(faces=
    mdb.models['Model-1'].parts['up-soil'].faces.findAt(((60.5, 8.333333, 0.0), 
    )), point1=mdb.models['Model-1'].parts['up-soil'].datums[5], point2=
    mdb.models['Model-1'].parts['up-soil'].datums[3])

mdb.models['Model-1'].parts['wall'].DatumPointByCoordinate(coords=(20.0, 17.0, 
    0.0))
mdb.models['Model-1'].parts['wall'].DatumPointByCoordinate(coords=(20.5, 17.0, 
    0.0))
mdb.models['Model-1'].parts['wall'].DatumPointByCoordinate(coords=(0.0, 0.0, 
    0.0))
mdb.models['Model-1'].parts['wall'].PartitionFaceByShortestPath(faces=
    mdb.models['Model-1'].parts['wall'].faces.findAt(((20.166667, 15.0, 0.0), 
    )), point1=mdb.models['Model-1'].parts['wall'].datums[2], point2=
    mdb.models['Model-1'].parts['wall'].datums[3])
mdb.models['Model-1'].Material(name='up-soil')
mdb.models['Model-1'].materials['up-soil'].Density(table=((1500.0, ), ))
mdb.models['Model-1'].materials['up-soil'].Elastic(table=((1000000.0, 0.3), ))
mdb.models['Model-1'].materials['up-soil'].MaxpsDamageInitiation(table=((
    5000.0, ), ))
mdb.models['Model-1'].materials['up-soil'].maxpsDamageInitiation.DamageEvolution(
    mixedModeBehavior=POWER_LAW, power=1.0, table=((10000.0, 10000.0, 10000.0), 
    ), type=ENERGY)
mdb.models['Model-1'].materials['up-soil'].maxpsDamageInitiation.DamageStabilizationCohesive(
    cohesiveCoeff=1e-05)
mdb.models['Model-1'].materials['up-soil'].Permeability(
    inertialDragCoefficient=0.142887, specificWeight=10000.0, table=((
    2.418e-06, 0.0), ))
mdb.models['Model-1'].materials['up-soil'].GapFlow(table=((1e-06, ), ))
mdb.models['Model-1'].materials['up-soil'].FluidLeakoff(table=((5.879e-16, 
    5.879e-16), ))
mdb.models['Model-1'].Material(name='wall')
mdb.models['Model-1'].materials['wall'].Density(table=((1500.0, ), ))
mdb.models['Model-1'].materials['wall'].Elastic(table=((1000000000.0, 0.3), ))
mdb.models['Model-1'].HomogeneousSolidSection(material='up-soil', name=
    'up-soil', thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='wall', name='wall', 
    thickness=None)
mdb.models['Model-1'].parts['up-soil'].Set(faces=
    mdb.models['Model-1'].parts['up-soil'].faces.findAt(((40.5, 6.666667, 0.0), 
    ), ((40.5, 15.0, 0.0), ), ((6.666667, 19.666667, 0.0), ), ((20.333333, 
    8.333333, 0.0), ), ((13.333333, 14.666667, 0.0), ), ), name='up-soil')
mdb.models['Model-1'].parts['up-soil'].Set(edges=
    mdb.models['Model-1'].parts['up-soil'].edges.findAt(((0.0, 23.0, 0.0), ), (
    (0.0, 14.0, 0.0), ), ), name='left')
mdb.models['Model-1'].parts['up-soil'].Set(edges=
    mdb.models['Model-1'].parts['up-soil'].edges.findAt(((80.5, 6.25, 0.0), ), 
    ((80.5, 13.75, 0.0), ), ), name='right')
mdb.models['Model-1'].parts['up-soil'].Surface(name='excavation', side1Edges=
    mdb.models['Model-1'].parts['up-soil'].edges.findAt(((20.0, 19.0, 0.0), )))
mdb.models['Model-1'].parts['up-soil'].Surface(name='non-excavation', 
    side1Edges=mdb.models['Model-1'].parts['up-soil'].edges.findAt(((20.5, 
    21.25, 0.0), ), ((20.375, 10.0, 0.0), ), ((20.0, 11.75, 0.0), ), ))
mdb.models['Model-1'].parts['wall'].Set(faces=
    mdb.models['Model-1'].parts['wall'].faces.findAt(((20.166667, 19.666667, 
    0.0), ), ((20.333333, 14.666667, 0.0), ), ), name='wall')
mdb.models['Model-1'].parts['wall'].Set(edges=
    mdb.models['Model-1'].parts['wall'].edges.findAt(((20.5, 23.0, 0.0), ), ((
    20.0, 19.0, 0.0), ), ((20.0, 11.75, 0.0), ), ((20.5, 15.25, 0.0), ), ), 
    name='wall-left-right')
mdb.models['Model-1'].parts['wall'].Set(edges=
    mdb.models['Model-1'].parts['wall'].edges.findAt(((20.375, 10.0, 0.0), )), 
    name='wall-bottom')
mdb.models['Model-1'].parts['wall'].Surface(name='excavation', side1Edges=
    mdb.models['Model-1'].parts['wall'].edges.findAt(((20.0, 19.0, 0.0), )))
mdb.models['Model-1'].parts['wall'].Surface(name='non-excavation', side1Edges=
    mdb.models['Model-1'].parts['wall'].edges.findAt(((20.5, 23.0, 0.0), ), ((
    20.0, 11.75, 0.0), ), ((20.375, 10.0, 0.0), ), ((20.5, 15.25, 0.0), ), ))
mdb.models['Model-1'].parts['up-soil'].Surface(name='bottom', side1Edges=
    mdb.models['Model-1'].parts['up-soil'].edges.findAt(((35.5, 5.0, 0.0), ), (
    (20.125, 5.0, 0.0), ), ((5.0, 5.0, 0.0), ), ))
mdb.models['Model-1'].parts['up-soil'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['up-soil'].sets['up-soil'], sectionName=
    'up-soil', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['wall'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['wall'].sets['wall'], sectionName='wall', 
    thicknessAssignment=FROM_SECTION)
# mdb.models['Model-1'].GeostaticStep(matrixSolver=DIRECT, matrixStorage=
#         UNSYMMETRIC, name='gra', nlgeom=ON, previous='Initial', timeIncrementationMethod=FIXED)
mdb.models['Model-1'].GeostaticStep(matrixSolver=DIRECT, matrixStorage=
        UNSYMMETRIC, name='gra', nlgeom=ON, previous='Initial', timeIncrementationMethod=AUTOMATIC,utol=0.01)
mdb.models['Model-1'].StaticStep(name='excavation-1', previous='gra')
mdb.models['Model-1'].StaticStep(name='excavation-2', previous='excavation-1')
mdb.models['Model-1'].StaticStep(name='excavation-3', previous='excavation-2')
mdb.models['Model-1'].SoilsStep(cetol=None, creep=OFF, end=None, name=
    'injection', previous='excavation-3', utol=1000000000.0)
mdb.models['Model-1'].FieldOutputRequest(name='F-Output-1', createStepName='gra')
mdb.models['Model-1'].HistoryOutputRequest(name='H-Output-1', createStepName='gra')
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValuesInStep(
    stepName='gra', variables=('S', 'LE', 'U', 'RF', 'CF', 'PHILSM', 
    'PSILSM', 'VOIDR', 'SAT', 'POR', 'PFL', 'PFLA', 'PTL', 'PTLA'))
mdb.models['Model-1'].ContactProperty('IntProp-1')
mdb.models['Model-1'].interactionProperties['IntProp-1'].TangentialBehavior(
    dependencies=0, directionality=ISOTROPIC, elasticSlipStiffness=None, 
    formulation=PENALTY, fraction=0.005, maximumElasticSlip=FRACTION, 
    pressureDependency=OFF, shearStressLimit=None, slipRateDependency=OFF, 
    table=((0.15, ), ), temperatureDependency=OFF)
mdb.models['Model-1'].interactionProperties['IntProp-1'].NormalBehavior(
    allowSeparation=ON, constraintEnforcementMethod=DEFAULT, 
    pressureOverclosure=HARD)
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='crack-1', part=
    mdb.models['Model-1'].parts['crack'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='up-soil-1', 
    part=mdb.models['Model-1'].parts['up-soil'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='wall-1', part=
    mdb.models['Model-1'].parts['wall'])
mdb.models['Model-1'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='gra', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='IntProp-1', master=
    mdb.models['Model-1'].rootAssembly.instances['wall-1'].surfaces['excavation']
    , name='wall-excavation', slave=
    mdb.models['Model-1'].rootAssembly.instances['up-soil-1'].surfaces['excavation']
    , sliding=FINITE, thickness=ON)
mdb.models['Model-1'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='gra', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='IntProp-1', master=
    mdb.models['Model-1'].rootAssembly.instances['wall-1'].surfaces['non-excavation']
    , name='wall-non-excavation', slave=
    mdb.models['Model-1'].rootAssembly.instances['up-soil-1'].surfaces['non-excavation']
    , sliding=FINITE, thickness=ON)
mdb.models['Model-1'].parts['up-soil'].Set(faces=
    mdb.models['Model-1'].parts['up-soil'].faces.findAt(((6.666667, 19.666667, 
    0.0), )), name='excavation')
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].Gravity(comp2=-10.0, createStepName='gra', 
    distributionType=UNIFORM, field='', name='gra')
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='gra', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'up-left', region=
    mdb.models['Model-1'].rootAssembly.instances['up-soil-1'].sets['left'], u1=
    0.0, u2=UNSET, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='gra', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'up-right', region=
    mdb.models['Model-1'].rootAssembly.instances['up-soil-1'].sets['right'], 
    u1=0.0, u2=UNSET, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='gra', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'wall-left-right', region=
    mdb.models['Model-1'].rootAssembly.instances['wall-1'].sets['wall-left-right']
    , u1=0.0, u2=0.0, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='gra', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'wall-bottom', region=
    mdb.models['Model-1'].rootAssembly.instances['wall-1'].sets['wall-bottom'], 
    u1=0.0, u2=0.0, ur3=0.0)
mdb.models['Model-1'].rootAssembly.Set(faces=
    mdb.models['Model-1'].rootAssembly.instances['up-soil-1'].faces.findAt(((
    40.5, 6.666667, 0.0), (0.0, 0.0, 1.0)), ((40.5, 15.0, 0.0), (0.0, 0.0, 
    1.0)), ((6.666667, 19.666667, 0.0), (0.0, 0.0, 1.0)), ((20.333333, 
    8.333333, 0.0), (0.0, 0.0, 1.0)), ((13.333333, 14.666667, 0.0), (0.0, 0.0, 
    1.0)), )+\
    mdb.models['Model-1'].rootAssembly.instances['wall-1'].faces.findAt(((
    20.166667, 19.666667, 0.0), (0.0, 0.0, 1.0)), ((20.333333, 14.666667, 0.0), 
    (0.0, 0.0, 1.0)), ), name='all')
mdb.models['Model-1'].GeostaticStress(lateralCoeff1=0.6, lateralCoeff2=None, 
    name='geo-up', region=
    mdb.models['Model-1'].rootAssembly.instances['up-soil-1'].sets['up-soil'], 
    stressMag1=0.0, stressMag2=-200000.0, vCoord1=25.0, vCoord2=5.0)
mdb.models['Model-1'].VoidsRatio(distributionType=UNIFORM, name='void', region=
    mdb.models['Model-1'].rootAssembly.instances['up-soil-1'].sets['up-soil'], 
    variation=CONSTANT_RATIO, voidsRatio1=0.5)
mdb.models['Model-1'].ExpressionField(description='', expression='25 -  Y ', 
    localCsys=None, name='AnalyticalField-1')
mdb.models['Model-1'].PorePressure(distributionType=FIELD, field=
    'AnalyticalField-1', name='pore', porePressure1=10000.0, region=
    mdb.models['Model-1'].rootAssembly.instances['up-soil-1'].sets['up-soil'], 
    variation=CONSTANT_RATIO)
mdb.models['Model-1'].parts['up-soil'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=1.0)
mdb.models['Model-1'].parts['up-soil'].setMeshControls(algorithm=MEDIAL_AXIS, 
    elemShape=QUAD, regions=
    mdb.models['Model-1'].parts['up-soil'].faces.findAt(((40.5, 6.666667, 0.0), 
    ), ((40.5, 15.0, 0.0), ), ((6.666667, 19.666667, 0.0), ), ((20.333333, 
    8.333333, 0.0), ), ((13.333333, 14.666667, 0.0), ), ))
mdb.models['Model-1'].parts['up-soil'].setElementType(elemTypes=(ElemType(
    elemCode=CPE4P, elemLibrary=STANDARD), ElemType(elemCode=UNKNOWN_TRI, 
    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['up-soil'].faces.findAt(((40.5, 6.666667, 0.0), 
    ), ((40.5, 15.0, 0.0), ), ((6.666667, 19.666667, 0.0), ), ((20.333333, 
    8.333333, 0.0), ), ((13.333333, 14.666667, 0.0), ), ), ))
mdb.models['Model-1'].parts['up-soil'].generateMesh()

mdb.models['Model-1'].parts['wall'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=1.0)
mdb.models['Model-1'].parts['wall'].setMeshControls(algorithm=MEDIAL_AXIS, 
    elemShape=QUAD, regions=mdb.models['Model-1'].parts['wall'].faces.findAt(((
    20.166667, 19.666667, 0.0), ), ((20.333333, 14.666667, 0.0), ), ))
mdb.models['Model-1'].parts['wall'].setElementType(elemTypes=(ElemType(
    elemCode=CPE4, elemLibrary=STANDARD), ElemType(elemCode=CPE3, 
    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['wall'].faces.findAt(((20.166667, 19.666667, 
    0.0), ), ((20.333333, 14.666667, 0.0), ), ), ))
mdb.models['Model-1'].parts['wall'].generateMesh()
mdb.models['Model-1'].parts['crack'].Set(edges=
    mdb.models['Model-1'].parts['crack'].edges.findAt(((18.5, 5.75, 0.0), )), 
    name='crack')
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].rootAssembly.engineeringFeatures.XFEMCrack(crackDomain=
    mdb.models['Model-1'].rootAssembly.instances['up-soil-1'].sets['up-soil'], 
    crackLocation=
    mdb.models['Model-1'].rootAssembly.instances['crack-1'].sets['crack'], 
    name='Crack-1')
mdb.models['Model-1'].rootAssembly.makeIndependent(instances=(
    mdb.models['Model-1'].rootAssembly.instances['crack-1'], 
    mdb.models['Model-1'].rootAssembly.instances['up-soil-1'], 
    mdb.models['Model-1'].rootAssembly.instances['wall-1']))
mdb.models['Model-1'].materials['wall'].elastic.setValues(table=((1000000.0, 
    0.3), ))

mdb.models['Model-1'].parts['up-soil'].DatumPointByCoordinate(coords=(0.0, 
    20.0, 0.0))
mdb.models['Model-1'].parts['up-soil'].DatumPointByCoordinate(coords=(20.0, 
    20.0, 0.0))
mdb.models['Model-1'].parts['up-soil'].DatumPointByCoordinate(coords=(0.0, 
    23.0, 0.0))
mdb.models['Model-1'].parts['up-soil'].DatumPointByCoordinate(coords=(20.0, 
    23.0, 0.0))
mdb.models['Model-1'].parts['up-soil'].PartitionFaceByShortestPath(faces=
    mdb.models['Model-1'].parts['up-soil'].faces.findAt(((6.666667, 19.666667, 
    0.0), )), point1=mdb.models['Model-1'].parts['up-soil'].datums[24], point2=
    mdb.models['Model-1'].parts['up-soil'].datums[25])
mdb.models['Model-1'].parts['up-soil'].PartitionFaceByShortestPath(faces=
    mdb.models['Model-1'].parts['up-soil'].faces.findAt(((6.666667, 21.666667, 
    0.0), )), point1=mdb.models['Model-1'].parts['up-soil'].datums[26], point2=
    mdb.models['Model-1'].parts['up-soil'].datums[27])
mdb.models['Model-1'].parts['wall'].DatumPointByCoordinate(coords=(0.0, 20.0, 
    0.0))
del mdb.models['Model-1'].parts['wall'].features['Datum pt-4']
mdb.models['Model-1'].parts['wall'].DatumPointByCoordinate(coords=(20.0, 20.0, 
    0.0))
mdb.models['Model-1'].parts['wall'].DatumPointByCoordinate(coords=(20.5, 20.0, 
    0.0))
mdb.models['Model-1'].parts['wall'].DatumPointByCoordinate(coords=(20.0, 23.0, 
    0.0))
mdb.models['Model-1'].parts['wall'].DatumPointByCoordinate(coords=(20.5, 23.0, 
    0.0))
mdb.models['Model-1'].parts['wall'].PartitionFaceByShortestPath(faces=
    mdb.models['Model-1'].parts['wall'].faces.findAt(((20.166667, 19.666667, 
    0.0), )), point1=mdb.models['Model-1'].parts['wall'].datums[15], point2=
    mdb.models['Model-1'].parts['wall'].datums[16])
mdb.models['Model-1'].parts['wall'].PartitionFaceByShortestPath(faces=
    mdb.models['Model-1'].parts['wall'].faces.findAt(((20.166667, 21.666667, 
    0.0), )), point1=mdb.models['Model-1'].parts['wall'].datums[17], point2=
    mdb.models['Model-1'].parts['wall'].datums[18])
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].parts['up-soil'].Set(edges=
    mdb.models['Model-1'].parts['up-soil'].edges.findAt(((35.5, 5.0, 0.0), ), (
    (20.125, 5.0, 0.0), ), ((5.0, 5.0, 0.0), ), ), name='bottom')
mdb.models['Model-1'].parts['up-soil'].Set(faces=
    mdb.models['Model-1'].parts['up-soil'].faces.findAt(((6.666667, 23.666667, 
    0.0), )), name='exca-1')
mdb.models['Model-1'].parts['up-soil'].Set(faces=
    mdb.models['Model-1'].parts['up-soil'].faces.findAt(((13.333333, 22.0, 
    0.0), )), name='exca-2')
mdb.models['Model-1'].parts['up-soil'].Set(faces=
    mdb.models['Model-1'].parts['up-soil'].faces.findAt(((13.333333, 19.0, 
    0.0), )), name='exca-3')
mdb.models['Model-1'].parts['up-soil'].Surface(name='exca-1', side1Edges=
    mdb.models['Model-1'].parts['up-soil'].edges.findAt(((20.0, 23.5, 0.0), )))
mdb.models['Model-1'].parts['up-soil'].Surface(name='exca-2', side1Edges=
    mdb.models['Model-1'].parts['up-soil'].edges.findAt(((20.0, 20.75, 0.0), 
    )))
mdb.models['Model-1'].parts['up-soil'].Surface(name='exca-3', side1Edges=
    mdb.models['Model-1'].parts['up-soil'].edges.findAt(((20.0, 17.75, 0.0), 
    )))
mdb.models['Model-1'].parts['wall'].Surface(name='exca-1', side1Edges=
    mdb.models['Model-1'].parts['wall'].edges.findAt(((20.0, 23.5, 0.0), )))
mdb.models['Model-1'].parts['wall'].Surface(name='exca-2', side1Edges=
    mdb.models['Model-1'].parts['wall'].edges.findAt(((20.0, 20.75, 0.0), )))
mdb.models['Model-1'].parts['wall'].Surface(name='exca-3', side1Edges=
    mdb.models['Model-1'].parts['wall'].edges.findAt(((20.0, 17.75, 0.0), )))
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].interactions['wall-excavation'].move('gra', 
    'excavation-1')
mdb.models['Model-1'].interactions['wall-excavation'].move('excavation-1', 
    'gra')
mdb.models['Model-1'].ModelChange(activeInStep=False, createStepName=
    'excavation-1', includeStrain=False, name='exca-1', region=
    mdb.models['Model-1'].rootAssembly.instances['up-soil-1'].sets['exca-1'])
mdb.models['Model-1'].ModelChange(activeInStep=False, createStepName=
    'excavation-1', includeStrain=False, name='exca-2', region=
    mdb.models['Model-1'].rootAssembly.instances['up-soil-1'].sets['exca-2'])
mdb.models['Model-1'].interactions['exca-2'].move('excavation-1', 
    'excavation-2')
mdb.models['Model-1'].ModelChange(activeInStep=False, createStepName=
    'excavation-3', includeStrain=False, name='exca-3', region=
    mdb.models['Model-1'].rootAssembly.instances['up-soil-1'].sets['exca-3'])
mdb.models['Model-1'].interactions.changeKey(fromName='wall-excavation', 
    toName='wall-up-1')
mdb.models['Model-1'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='gra', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='IntProp-1', master=
    mdb.models['Model-1'].rootAssembly.instances['wall-1'].surfaces['exca-1'], 
    name='wall-up', slave=
    mdb.models['Model-1'].rootAssembly.instances['up-soil-1'].surfaces['exca-1']
    , sliding=FINITE, thickness=ON)
mdb.models['Model-1'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='gra', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='IntProp-1', master=
    mdb.models['Model-1'].rootAssembly.instances['wall-1'].surfaces['exca-2'], 
    name='wall-up-2', slave=
    mdb.models['Model-1'].rootAssembly.instances['up-soil-1'].surfaces['exca-2']
    , sliding=FINITE, thickness=ON)
mdb.models['Model-1'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='gra', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='IntProp-1', master=
    mdb.models['Model-1'].rootAssembly.instances['wall-1'].surfaces['exca-3'], 
    name='wall-up-3', slave=
    mdb.models['Model-1'].rootAssembly.instances['up-soil-1'].surfaces['exca-3']
    , sliding=FINITE, thickness=ON)
mdb.models['Model-1'].interactions['wall-up-1'].deactivate('excavation-1')
mdb.models['Model-1'].interactions['wall-up-2'].deactivate('excavation-2')
mdb.models['Model-1'].interactions['wall-up-3'].deactivate('excavation-3')

mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='up-bottom', 
    region=
    mdb.models['Model-1'].rootAssembly.instances['up-soil-1'].sets['bottom'], 
    u1=SET, u2=SET, ur3=UNSET)
mdb.models['Model-1'].boundaryConditions['up-bottom'].move('Initial', 'gra')
mdb.models['Model-1'].rootAssembly.makeDependent(instances=(
    mdb.models['Model-1'].rootAssembly.instances['crack-1'], ))
mdb.models['Model-1'].rootAssembly.makeDependent(instances=(
    mdb.models['Model-1'].rootAssembly.instances['up-soil-1'], ))
mdb.models['Model-1'].rootAssembly.makeDependent(instances=(
    mdb.models['Model-1'].rootAssembly.instances['wall-1'], ))
mdb.models['Model-1'].parts['up-soil'].setElementType(elemTypes=(ElemType(
    elemCode=CPE4P, elemLibrary=STANDARD), ElemType(elemCode=UNKNOWN_TRI, 
    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['up-soil'].faces.findAt(((6.666667, 23.666667, 
    0.0), ), ((13.333333, 22.0, 0.0), ), ((40.5, 6.666667, 0.0), ), ((40.5, 
    15.0, 0.0), ), ((13.333333, 19.0, 0.0), ), ((20.333333, 8.333333, 0.0), ), 
    ((13.333333, 14.666667, 0.0), ), ), ))
mdb.models['Model-1'].parts['up-soil'].generateMesh()
mdb.models['Model-1'].parts['wall'].setElementType(elemTypes=(ElemType(
    elemCode=CPE4, elemLibrary=STANDARD), ElemType(elemCode=CPE3, 
    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['wall'].faces.findAt(((20.166667, 23.666667, 
    0.0), ), ((20.333333, 22.0, 0.0), ), ((20.333333, 19.0, 0.0), ), ((
    20.333333, 14.666667, 0.0), ), ), ))
mdb.models['Model-1'].parts['wall'].generateMesh()
mdb.models['Model-1'].rootAssembly.regenerate()
# mdb.models['Model-1'].boundaryConditions['up-bottom'].suppress()
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].predefinedFields['geo-up'].suppress()
mdb.models['Model-1'].boundaryConditions['up-bottom'].resume()

