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

clay_left_horizon_limit = 0
pile_left_horizon_limit = 15
before_pile_equal_horizon_limit = pile_left_horizon_limit/2
pile_right_horizon_limit = 15.5
pile_equal_mid_horizon_limit = (pile_left_horizon_limit+pile_right_horizon_limit)/2
wall_left_horizon_limit = 18.5
wall_right_horizon_limit = 19
wall_equal_horizon_limit = (wall_left_horizon_limit+wall_right_horizon_limit)/2
clay_right_horizon_limit = 48.5
after_wall_equal_horizon_limit = (wall_right_horizon_limit+clay_right_horizon_limit)/2
after_pile_equal_horizon_limit = (pile_right_horizon_limit+clay_right_horizon_limit)/2

pile_bottom_vertical_limit = -3
pile_mid_vertical_limit = 0
clay_bottom_vertical_limit = 0
wall_bottom_vertical_limit = 5
wall_mid_vertical_limit = 12
wall_top_vertical_limit = 20
pile_top_vertical_limit = 12
pile_equal_vertical_limit = (pile_top_vertical_limit+pile_mid_vertical_limit)/2
clay_top_vertical_limit = 20
wall_equal_vertical_limit = (wall_top_vertical_limit+wall_bottom_vertical_limit)/2

clay_left_horizon_limit_p = -25
pile_left_horizon_limit_p = -0.25
pile_right_horizon_limit_p = 0.25
wall_left_horizon_limit_p = -0.25
wall_right_horizon_limit_p = 0.25
clay_right_horizon_limit_p = 25

pile_mid_vertical_limit_p = -4.5
clay_bottom_vertical_limit_p = -10
clay_top_vertical_limit_p = 10
wall_mid_vertical_limit_p = -0.5
pile_top_vertical_limit_p = 12
clay_top_vertical_limit_p = 10

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(0.0, clay_top_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(clay_right_horizon_limit, clay_top_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(clay_right_horizon_limit, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(wall_left_horizon_limit, clay_top_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(wall_right_horizon_limit, clay_top_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(wall_left_horizon_limit, wall_bottom_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(wall_right_horizon_limit, wall_bottom_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(pile_right_horizon_limit, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(pile_left_horizon_limit, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(pile_left_horizon_limit, wall_mid_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(pile_right_horizon_limit, wall_mid_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(
    0.0, clay_top_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, clay_top_vertical_limit/2))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, clay_top_vertical_limit/2), 
    ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, clay_top_vertical_limit), point2=(
    wall_left_horizon_limit, clay_top_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_left_horizon_limit/2, clay_top_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_left_horizon_limit/2, clay_top_vertical_limit), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, clay_top_vertical_limit/2))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_left_horizon_limit/2, clay_top_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, clay_top_vertical_limit/2), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    wall_left_horizon_limit/2, clay_top_vertical_limit), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(wall_left_horizon_limit, clay_top_vertical_limit), point2=
    (wall_left_horizon_limit, wall_bottom_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_left_horizon_limit, wall_equal_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_left_horizon_limit, wall_equal_vertical_limit), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_left_horizon_limit/2, clay_top_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_left_horizon_limit, wall_equal_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_left_horizon_limit/2, clay_top_vertical_limit), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    wall_left_horizon_limit, wall_equal_vertical_limit), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(wall_left_horizon_limit, wall_bottom_vertical_limit), point2=(
    wall_right_horizon_limit, wall_bottom_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_equal_horizon_limit, wall_bottom_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_equal_horizon_limit, wall_bottom_vertical_limit), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_left_horizon_limit, wall_equal_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_equal_horizon_limit, wall_bottom_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_left_horizon_limit, wall_equal_vertical_limit), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    wall_equal_horizon_limit, wall_bottom_vertical_limit), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(wall_right_horizon_limit, wall_bottom_vertical_limit), point2=(
    wall_right_horizon_limit, clay_top_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_right_horizon_limit, wall_equal_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_right_horizon_limit, wall_equal_vertical_limit), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_equal_horizon_limit, wall_bottom_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_right_horizon_limit, wall_equal_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_equal_horizon_limit, wall_bottom_vertical_limit), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    wall_right_horizon_limit, wall_equal_vertical_limit), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(wall_right_horizon_limit, clay_top_vertical_limit), point2=
    (clay_right_horizon_limit, clay_top_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((after_wall_equal_horizon_limit, clay_top_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((after_wall_equal_horizon_limit, clay_top_vertical_limit), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_right_horizon_limit, wall_equal_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((after_wall_equal_horizon_limit, clay_top_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_right_horizon_limit, wall_equal_vertical_limit), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    after_wall_equal_horizon_limit, clay_top_vertical_limit), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(clay_right_horizon_limit, clay_top_vertical_limit), point2=
    (clay_right_horizon_limit, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((clay_right_horizon_limit, clay_top_vertical_limit/2))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((clay_right_horizon_limit, clay_top_vertical_limit/2), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((after_wall_equal_horizon_limit, clay_top_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((clay_right_horizon_limit, clay_top_vertical_limit/2))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((after_wall_equal_horizon_limit, clay_top_vertical_limit), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    clay_right_horizon_limit, clay_top_vertical_limit/2), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(clay_right_horizon_limit, 0.0), point2=(
    pile_right_horizon_limit, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((after_pile_equal_horizon_limit, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((after_pile_equal_horizon_limit, 0.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((clay_right_horizon_limit, clay_top_vertical_limit/2))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((after_pile_equal_horizon_limit, 0.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((clay_right_horizon_limit, clay_top_vertical_limit/2), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    after_pile_equal_horizon_limit, 0.0), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(pile_right_horizon_limit, 0.0), point2=(
    pile_right_horizon_limit, wall_mid_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((pile_right_horizon_limit, pile_equal_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((pile_right_horizon_limit, pile_equal_vertical_limit), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((after_pile_equal_horizon_limit, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((pile_right_horizon_limit, pile_equal_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((after_pile_equal_horizon_limit, 0.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    pile_right_horizon_limit, pile_equal_vertical_limit), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(pile_right_horizon_limit, wall_mid_vertical_limit), point2=
    (pile_left_horizon_limit, wall_mid_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((pile_equal_mid_horizon_limit, wall_mid_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((pile_equal_mid_horizon_limit, 
    wall_mid_vertical_limit), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((pile_right_horizon_limit, pile_equal_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((pile_equal_mid_horizon_limit, wall_mid_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((pile_right_horizon_limit, pile_equal_vertical_limit), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    pile_equal_mid_horizon_limit, wall_mid_vertical_limit), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(pile_left_horizon_limit, wall_mid_vertical_limit), point2=
    (pile_left_horizon_limit, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((pile_left_horizon_limit, pile_equal_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((pile_left_horizon_limit, pile_equal_vertical_limit), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((pile_equal_mid_horizon_limit, wall_mid_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((pile_left_horizon_limit, pile_equal_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((pile_equal_mid_horizon_limit, 
    wall_mid_vertical_limit), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((pile_left_horizon_limit, pile_equal_vertical_limit), 
    ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(pile_left_horizon_limit, 0.0), point2=(
    0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((before_pile_equal_horizon_limit, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((before_pile_equal_horizon_limit, 0.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((pile_left_horizon_limit, pile_equal_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((before_pile_equal_horizon_limit, 0.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((pile_left_horizon_limit, pile_equal_vertical_limit), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    before_pile_equal_horizon_limit, 0.0), ))
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='clay', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['clay'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
datum_0 = mdb.models['Model-1'].parts['clay'].DatumPointByCoordinate(coords=(wall_left_horizon_limit, wall_bottom_vertical_limit, 
    0.0))
# print(type(datum_0))
# print(dir(datum_0))
# print(datum_0.__doc__)
# print(datum_0.name)
datum_1 = mdb.models['Model-1'].parts['clay'].DatumPointByCoordinate(coords=(wall_left_horizon_limit, clay_bottom_vertical_limit, 
    0.0))
datum_2 = mdb.models['Model-1'].parts['clay'].DatumPointByCoordinate(coords=(wall_right_horizon_limit, wall_bottom_vertical_limit, 
    0.0))
datum_3 = mdb.models['Model-1'].parts['clay'].DatumPointByCoordinate(coords=(wall_right_horizon_limit, clay_bottom_vertical_limit, 
    0.0))
datum_4 = mdb.models['Model-1'].parts['clay'].DatumPointByCoordinate(coords=(pile_left_horizon_limit, pile_top_vertical_limit, 
    0.0))
datum_5 = mdb.models['Model-1'].parts['clay'].DatumPointByCoordinate(coords=(pile_left_horizon_limit, clay_top_vertical_limit, 
    0.0))
datum_6 = mdb.models['Model-1'].parts['clay'].DatumPointByCoordinate(coords=(pile_right_horizon_limit, pile_top_vertical_limit, 
    0.0))
datum_7 = mdb.models['Model-1'].parts['clay'].DatumPointByCoordinate(coords=(pile_right_horizon_limit, clay_top_vertical_limit, 
    0.0))
datum_8 = mdb.models['Model-1'].parts['clay'].DatumPointByCoordinate(coords=(wall_left_horizon_limit, pile_top_vertical_limit, 
    0.0))
datum_9 = mdb.models['Model-1'].parts['clay'].DatumPointByCoordinate(coords=(clay_left_horizon_limit, pile_top_vertical_limit, 
    0.0))
datum_10 = mdb.models['Model-1'].parts['clay'].DatumPointByCoordinate(coords=(clay_right_horizon_limit, wall_bottom_vertical_limit, 
    0.0))
datums = mdb.models['Model-1'].parts['clay'].datums
# print(dir(datums))
# print(datums.__doc__)
# print(datums.keys())
# print(datums.values())
mdb.models['Model-1'].parts['clay'].PartitionFaceByShortestPath(faces=
    mdb.models['Model-1'].parts['clay'].faces.findAt(((pile_left_horizon_limit/2, (pile_top_vertical_limit+clay_top_vertical_limit)/2, 0.0), ))
    , point1=datums[datum_4.id], point2=datums[datum_5.id])
mdb.models['Model-1'].parts['clay'].PartitionFaceByShortestPath(faces=
    mdb.models['Model-1'].parts['clay'].faces.findAt((((pile_right_horizon_limit+wall_left_horizon_limit)/2, (pile_top_vertical_limit+clay_top_vertical_limit)/2, 0.0), ))
    , point1=datums[datum_6.id], point2=datums[datum_7.id])
mdb.models['Model-1'].parts['clay'].PartitionFaceByShortestPath(faces=
    mdb.models['Model-1'].parts['clay'].faces.findAt((((pile_right_horizon_limit+wall_left_horizon_limit)/2, pile_top_vertical_limit/2, 0.0), ))
    , point1=datums[datum_6.id], point2=datums[datum_8.id])
mdb.models['Model-1'].parts['clay'].PartitionFaceByShortestPath(faces=
    mdb.models['Model-1'].parts['clay'].faces.findAt((((pile_right_horizon_limit+wall_left_horizon_limit)/2, pile_top_vertical_limit/2, 0.0), ))
    , point1=datums[datum_0.id], point2=datums[datum_1.id])
mdb.models['Model-1'].parts['clay'].PartitionFaceByShortestPath(faces=
    mdb.models['Model-1'].parts['clay'].faces.findAt((((wall_right_horizon_limit+clay_right_horizon_limit)/2, wall_bottom_vertical_limit/2, 0.0), ))
    , point1=datums[datum_2.id], point2=datums[datum_3.id])
mdb.models['Model-1'].parts['clay'].PartitionFaceByShortestPath(faces=
    mdb.models['Model-1'].parts['clay'].faces.findAt((((wall_right_horizon_limit+clay_right_horizon_limit)/2, wall_bottom_vertical_limit/2, 0.0), ))
    , point1=datums[datum_2.id], point2=datums[datum_10.id])
mdb.models['Model-1'].parts['clay'].PartitionFaceByShortestPath(faces=
    mdb.models['Model-1'].parts['clay'].faces.findAt(((pile_left_horizon_limit/2, pile_top_vertical_limit/2, 0.0), ))
    , point1=datums[datum_9.id], point2=datums[datum_4.id])
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(wall_left_horizon_limit, clay_top_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(wall_right_horizon_limit, wall_bottom_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(wall_left_horizon_limit, clay_top_vertical_limit), 
    point2=(wall_right_horizon_limit, wall_bottom_vertical_limit))
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='wall', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['wall'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(pile_left_horizon_limit, wall_mid_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(pile_right_horizon_limit, pile_bottom_vertical_limit))
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(pile_left_horizon_limit, wall_mid_vertical_limit), 
    point2=(pile_right_horizon_limit, -3.0))
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='pile', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['pile'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['clay'].Surface(name='no_excavation', side1Edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt(((wall_left_horizon_limit, (wall_bottom_vertical_limit+pile_top_vertical_limit)/2, 0.0), ), ((
    wall_right_horizon_limit, (wall_bottom_vertical_limit+pile_top_vertical_limit)/2, 0.0), ), (((wall_left_horizon_limit+wall_right_horizon_limit)/2, wall_bottom_vertical_limit, 0.0), ), ))
mdb.models['Model-1'].parts['clay'].Surface(name='excavation', side1Edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt(((wall_left_horizon_limit, (pile_top_vertical_limit+clay_top_vertical_limit)/2, 0.0), )))
mdb.models['Model-1'].parts['clay'].Set(faces=
    mdb.models['Model-1'].parts['clay'].faces.findAt(((pile_left_horizon_limit/2, pile_top_vertical_limit/2, 0.0), ), ((
    wall_left_horizon_limit/2, (pile_top_vertical_limit+clay_top_vertical_limit)/2, 0.0), ), (((pile_left_horizon_limit+pile_right_horizon_limit)/2, (pile_top_vertical_limit+clay_top_vertical_limit)/2, 0.0), ), (((pile_right_horizon_limit+wall_left_horizon_limit)/2, 
    (pile_top_vertical_limit+clay_top_vertical_limit)/2, 0.0), ), (((pile_right_horizon_limit+wall_left_horizon_limit)/2, pile_top_vertical_limit/2, 0.0), ), (((wall_right_horizon_limit+clay_right_horizon_limit)/2, (wall_bottom_vertical_limit+clay_top_vertical_limit)/2, 0.0), ), 
    (((wall_left_horizon_limit+wall_right_horizon_limit)/2, wall_bottom_vertical_limit/2, 0.0), ), (((wall_right_horizon_limit+clay_right_horizon_limit)/2, wall_bottom_vertical_limit/2, 0.0), ), ), name=
    'clay')
mdb.models['Model-1'].parts['clay'].Set(edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt(((0.0, pile_top_vertical_limit/2, 0.0), ), ((
    0.0, (pile_top_vertical_limit+clay_top_vertical_limit)/2, 0.0), ), ), name='left_bc')
mdb.models['Model-1'].parts['clay'].Set(edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt(((clay_right_horizon_limit, (clay_top_vertical_limit+wall_bottom_vertical_limit)/2, 0.0), ), ((
    clay_right_horizon_limit, wall_bottom_vertical_limit/2, 0.0), ), ), name='right_bc')
mdb.models['Model-1'].parts['clay'].Set(edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt(((pile_left_horizon_limit/2, 0.0, 0.0), ), ((
    (pile_right_horizon_limit+wall_left_horizon_limit)/2, 0.0, 0.0), ), (((wall_left_horizon_limit+wall_right_horizon_limit)/2, 0.0, 0.0), ), (((wall_right_horizon_limit+clay_right_horizon_limit)/2, 0.0, 0.0), ), ), 
    name='bottom_bc')
mdb.models['Model-1'].parts['clay'].Set(edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt(((pile_left_horizon_limit, pile_top_vertical_limit/2, 0.0), ), ((
    pile_right_horizon_limit, pile_top_vertical_limit/2, 0.0), ), ), name='pile_int_lateral')
mdb.models['Model-1'].parts['clay'].Set(edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt(((pile_left_horizon_limit/2, wall_mid_vertical_limit, 0.0), ), ((
    pile_left_horizon_limit/2, 0.0, 0.0), ), ((pile_left_horizon_limit/2, clay_top_vertical_limit, 0.0), ), (((pile_right_horizon_limit+wall_left_horizon_limit)/2, wall_mid_vertical_limit, 0.0), ), ((
    (pile_right_horizon_limit+wall_left_horizon_limit)/2, clay_top_vertical_limit, 0.0), ), (((pile_right_horizon_limit+wall_left_horizon_limit)/2, 0.0, 0.0), ), (((wall_right_horizon_limit+clay_right_horizon_limit)/2, wall_bottom_vertical_limit, 0.0), ), ((
    (wall_right_horizon_limit+clay_right_horizon_limit)/2, clay_top_vertical_limit, 0.0), ), (((wall_right_horizon_limit+clay_right_horizon_limit)/2, 0.0, 0.0), ), ), name='horizon_edge')
# mdb.models['Model-1'].parts['clay'].sets.changeKey(fromName='lateral_edge', 
#     toName='horizon_edge')
mdb.models['Model-1'].parts['clay'].Set(edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt(((0.0, pile_top_vertical_limit/2, 0.0), ), ((
    pile_left_horizon_limit, pile_top_vertical_limit/2, 0.0), ), ((pile_left_horizon_limit, (pile_top_vertical_limit+clay_top_vertical_limit)/2, 0.0), ), ((0.0, (pile_top_vertical_limit+clay_top_vertical_limit)/2, 0.0), ), ((pile_right_horizon_limit, 
    (pile_top_vertical_limit+clay_top_vertical_limit)/2, 0.0), ), ((wall_left_horizon_limit, (pile_top_vertical_limit+clay_top_vertical_limit)/2, 0.0), ), ((pile_right_horizon_limit, pile_top_vertical_limit/2, 0.0), ), ((wall_left_horizon_limit, wall_bottom_vertical_limit/2, 
    0.0), ), ((wall_left_horizon_limit, (wall_bottom_vertical_limit+pile_top_vertical_limit)/2, 0.0), ), ((clay_right_horizon_limit, (clay_top_vertical_limit+wall_bottom_vertical_limit)/2, 0.0), ), ((wall_right_horizon_limit, (wall_bottom_vertical_limit+pile_top_vertical_limit)/2, 
    0.0), ), ((wall_right_horizon_limit, wall_bottom_vertical_limit/2, 0.0), ), ((clay_right_horizon_limit, wall_bottom_vertical_limit/2, 0.0), ), ), name=
    'vertical_edge')
mdb.models['Model-1'].parts['clay'].Surface(name='pile_int', side1Edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt(((pile_left_horizon_limit, pile_top_vertical_limit/2, 0.0), ), ((
    (pile_left_horizon_limit+pile_right_horizon_limit)/2, pile_top_vertical_limit, 0.0), ), ((pile_right_horizon_limit, pile_top_vertical_limit/2, 0.0), ), ))
mdb.models['Model-1'].parts['clay'].Set(edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt(((wall_left_horizon_limit, (wall_mid_vertical_limit+clay_top_vertical_limit)/2, 0.0), ), ((
    wall_left_horizon_limit, (wall_mid_vertical_limit+wall_bottom_vertical_limit)/2, 0.0), ), ((wall_right_horizon_limit, (wall_mid_vertical_limit+wall_bottom_vertical_limit)/2, 0.0), ),),name='clay_lateral')
mdb.models['Model-1'].parts['clay'].Set(edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt((((wall_left_horizon_limit+wall_right_horizon_limit)/2, wall_bottom_vertical_limit, 0.0), )), 
    name='wall_bottom')
mdb.models['Model-1'].parts['clay'].Set(edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt(((pile_left_horizon_limit, pile_top_vertical_limit/2, 0.0), ), ((
    pile_right_horizon_limit, pile_top_vertical_limit/2, 0.0), ), ), name='pile_lateral')
pile_datum_0 = mdb.models['Model-1'].parts['pile'].DatumPointByCoordinate(coords=(pile_left_horizon_limit, pile_mid_vertical_limit, 
    0.0))
pile_datum_1 = mdb.models['Model-1'].parts['pile'].DatumPointByCoordinate(coords=(pile_right_horizon_limit, pile_mid_vertical_limit, 
    0.0))
mdb.models['Model-1'].parts['pile'].PartitionFaceByShortestPath(faces=
    mdb.models['Model-1'].parts['pile'].faces.findAt((((pile_left_horizon_limit+pile_right_horizon_limit)/2, pile_top_vertical_limit/2, 0.0), 
    )), point1=mdb.models['Model-1'].parts['pile'].datums[pile_datum_0.id], point2=
    mdb.models['Model-1'].parts['pile'].datums[pile_datum_1.id])
mdb.models['Model-1'].parts['pile'].Set(faces=
    mdb.models['Model-1'].parts['pile'].faces.findAt((((pile_left_horizon_limit+pile_right_horizon_limit)/2, pile_bottom_vertical_limit/2, 0.0), 
    ), (((pile_left_horizon_limit+pile_right_horizon_limit)/2, pile_top_vertical_limit/2, 0.0), ), ), name='pile')
mdb.models['Model-1'].parts['pile'].Set(edges=
    mdb.models['Model-1'].parts['pile'].edges.findAt(((pile_right_horizon_limit, pile_top_vertical_limit/2, 0.0), ), ((
    pile_left_horizon_limit, pile_top_vertical_limit/2, 0.0), ), ), name='pile_int_lateral')
mdb.models['Model-1'].parts['pile'].Set(edges=
    mdb.models['Model-1'].parts['pile'].edges.findAt(((pile_left_horizon_limit, pile_bottom_vertical_limit/2, 0.0), ), ((
    pile_right_horizon_limit, pile_bottom_vertical_limit/2, 0.0), ), ), name='pile_no_int_lateral')
mdb.models['Model-1'].parts['pile'].Surface(name='pile_int', side1Edges=
    mdb.models['Model-1'].parts['pile'].edges.findAt(((pile_left_horizon_limit, pile_top_vertical_limit/2, 0.0), ), ((
    (pile_left_horizon_limit+pile_right_horizon_limit)/2, pile_top_vertical_limit, 0.0), ), ((pile_right_horizon_limit, pile_top_vertical_limit/2, 0.0), ), ))
mdb.models['Model-1'].parts['pile'].Set(edges=
    mdb.models['Model-1'].parts['pile'].edges.findAt((((pile_left_horizon_limit+pile_right_horizon_limit)/2, pile_bottom_vertical_limit, 0.0), )), 
    name='bottom')
wall_datum_0 = mdb.models['Model-1'].parts['wall'].DatumPointByCoordinate(coords=(wall_left_horizon_limit, pile_top_vertical_limit, 
    0.0))
wall_datum_1 = mdb.models['Model-1'].parts['wall'].DatumPointByCoordinate(coords=(wall_right_horizon_limit, pile_top_vertical_limit, 
    0.0))
mdb.models['Model-1'].parts['wall'].PartitionFaceByShortestPath(faces=
    mdb.models['Model-1'].parts['wall'].faces.findAt((((wall_left_horizon_limit+wall_right_horizon_limit)/2, (wall_bottom_vertical_limit+wall_top_vertical_limit)/2, 0.0), 
    )), point1=mdb.models['Model-1'].parts['wall'].datums[wall_datum_0.id], point2=
    mdb.models['Model-1'].parts['wall'].datums[wall_datum_1.id])
mdb.models['Model-1'].parts['wall'].Set(faces=
    mdb.models['Model-1'].parts['wall'].faces.findAt((((wall_left_horizon_limit+wall_right_horizon_limit)/2, (wall_bottom_vertical_limit+pile_top_vertical_limit)/2, 
    0.0), ), (((wall_left_horizon_limit+wall_right_horizon_limit)/2, (pile_top_vertical_limit+wall_top_vertical_limit)/2, 0.0), ), ), name='wall')
mdb.models['Model-1'].parts['wall'].Surface(name='excavation', side1Edges=
    mdb.models['Model-1'].parts['wall'].edges.findAt(((wall_left_horizon_limit, (clay_top_vertical_limit+pile_top_vertical_limit)/2, 0.0), )))
mdb.models['Model-1'].parts['wall'].Surface(name='no_excavation', side1Edges=
    mdb.models['Model-1'].parts['wall'].edges.findAt(((wall_left_horizon_limit, (pile_top_vertical_limit+wall_bottom_vertical_limit)/2, 0.0), ), ((
    (wall_left_horizon_limit+wall_right_horizon_limit)/2, wall_bottom_vertical_limit, 0.0), ), ((wall_right_horizon_limit, (pile_top_vertical_limit+wall_bottom_vertical_limit)/2, 0.0), ), ((wall_right_horizon_limit, (clay_top_vertical_limit+pile_top_vertical_limit)/2, 0.0), ), ))
mdb.models['Model-1'].parts['wall'].Set(edges=
    mdb.models['Model-1'].parts['wall'].edges.findAt(((wall_left_horizon_limit, (pile_top_vertical_limit+wall_bottom_vertical_limit)/2, 0.0), ), ((
    wall_right_horizon_limit, (pile_top_vertical_limit+wall_bottom_vertical_limit)/2, 0.0), ), ((wall_right_horizon_limit, (clay_top_vertical_limit+pile_top_vertical_limit)/2, 0.0), ), ((wall_left_horizon_limit, (clay_top_vertical_limit+pile_top_vertical_limit)/2, 0.0), ), ), name=
    'lateral')
mdb.models['Model-1'].parts['wall'].Set(edges=
    mdb.models['Model-1'].parts['wall'].edges.findAt((((wall_left_horizon_limit+wall_right_horizon_limit)/2, wall_bottom_vertical_limit, 0.0), )), 
    name='bottom')
mdb.models['Model-1'].parts['clay'].Set(faces=
    mdb.models['Model-1'].parts['clay'].faces.findAt(((pile_left_horizon_limit/2, (pile_top_vertical_limit+clay_top_vertical_limit)/2, 0.0), ), 
    (((pile_right_horizon_limit+wall_left_horizon_limit)/2, (pile_top_vertical_limit+clay_top_vertical_limit)/2, 0.0), ), (((pile_left_horizon_limit+pile_right_horizon_limit)/2, (pile_top_vertical_limit+clay_top_vertical_limit)/2, 0.0), ), ), name=
    'excavation')
mdb.models['Model-1'].Material(name='clay')
mdb.models['Model-1'].materials['clay'].Density(table=((1616, ), ))
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
    0.142887, specificWeight=10000.0, table=((2.418e-05, 0.0), ))
mdb.models['Model-1'].Material(name='manual_structure')
mdb.models['Model-1'].materials['manual_structure'].Density(table=((1616, ), ))
mdb.models['Model-1'].materials['manual_structure'].Elastic(table=((90000000000.0, 
    0.1), ))
mdb.models['Model-1'].HomogeneousSolidSection(material='clay', name='clay', 
    thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='manual_structure', name='pile'
    , thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='manual_structure', name='wall'
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
    0.05, matrixSolver=DIRECT, matrixStorage=UNSYMMETRIC, maxInc=wall_bottom_vertical_limit, minInc=
    1e-12, name='injection', previous='excavation', timePeriod=100.0, utol=
    1000000000.0)
# maunal script
mdb.models['Model-1'].FieldOutputRequest(name='F-Output-1',createStepName='gravity')
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
mdb.models['Model-1'].ModelChange(activeInStep=False, createStepName=
    'excavation', includeStrain=False, name='excavation', region=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].sets['excavation'])
mdb.models['Model-1'].rootAssembly.engineeringFeatures.XFEMCrack(crackDomain=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].sets['clay'], 
    crackLocation=
    mdb.models['Model-1'].rootAssembly.instances['crack-1'].sets['crack'], 
    name='Crack-1')
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['crack-1'].edges.findAt(((
    17.0, 0.25, 0.0), )), faces=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].faces.findAt(((pile_left_horizon_limit/2, 
    pile_top_vertical_limit/2, 0.0), (0.0, 0.0, 1.0)), ((pile_left_horizon_limit/2, (pile_top_vertical_limit+clay_top_vertical_limit)/2, 0.0), (0.0, 0.0, 1.0)), ((
    (pile_left_horizon_limit+pile_right_horizon_limit)/2, (pile_top_vertical_limit+clay_top_vertical_limit)/2, 0.0), (0.0, 0.0, 1.0)), (((pile_right_horizon_limit+wall_left_horizon_limit)/2, (pile_top_vertical_limit+clay_top_vertical_limit)/2, 0.0), (
    0.0, 0.0, 1.0)), (((pile_right_horizon_limit+wall_left_horizon_limit)/2, pile_top_vertical_limit/2, 0.0), (0.0, 0.0, 1.0)), (((wall_left_horizon_limit+clay_right_horizon_limit)/2, 
    (wall_bottom_vertical_limit+clay_top_vertical_limit)/2, 0.0), (0.0, 0.0, 1.0)), (((wall_left_horizon_limit+wall_right_horizon_limit)/2, wall_bottom_vertical_limit/2, 0.0), (0.0, 0.0, 
    1.0)), (((wall_right_horizon_limit+clay_right_horizon_limit)/2, wall_bottom_vertical_limit/2, 0.0), (0.0, 0.0, 1.0)), )+\
    mdb.models['Model-1'].rootAssembly.instances['pile-1'].faces.findAt(((
    (pile_left_horizon_limit+pile_right_horizon_limit)/2, pile_bottom_vertical_limit/2, 0.0), (0.0, 0.0, 1.0)), (((pile_left_horizon_limit+pile_right_horizon_limit)/2, pile_top_vertical_limit/2, 0.0), (0.0, 0.0, 
    1.0)), )+\
    mdb.models['Model-1'].rootAssembly.instances['wall-1'].faces.findAt(((
    (wall_left_horizon_limit+wall_right_horizon_limit)/2, (wall_bottom_vertical_limit+wall_mid_vertical_limit)/2, 0.0), (0.0, 0.0, 1.0)), (((wall_left_horizon_limit+wall_right_horizon_limit)/2, (wall_mid_vertical_limit+clay_top_vertical_limit)/2, 0.0), 
    (0.0, 0.0, 1.0)), ), name='manual_whole')
mdb.models['Model-1'].Gravity(comp2=-clay_top_vertical_limit/2, createStepName='gravity', 
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
    mdb.models['Model-1'].parts['clay'].edges.findAt(((pile_left_horizon_limit/2, wall_mid_vertical_limit, 0.0), ), ((
    pile_left_horizon_limit/2, 0.0, 0.0), ), ((pile_left_horizon_limit/2, clay_top_vertical_limit, 0.0), ), (((pile_right_horizon_limit+wall_left_horizon_limit)/2, wall_mid_vertical_limit, 0.0), ), ((
    (pile_right_horizon_limit+wall_left_horizon_limit)/2, clay_top_vertical_limit, 0.0), ), (((pile_right_horizon_limit+wall_left_horizon_limit)/2, 0.0, 0.0), ), (((wall_right_horizon_limit+clay_right_horizon_limit)/2, wall_bottom_vertical_limit, 0.0), ), ((
    (wall_right_horizon_limit+clay_right_horizon_limit)/2, clay_top_vertical_limit, 0.0), ), (((wall_right_horizon_limit+clay_right_horizon_limit)/2, 0.0, 0.0), ), ), size=1.0)
mdb.models['Model-1'].parts['clay'].seedEdgeBySize(constraint=FINER, 
    deviationFactor=0.1, edges=
    mdb.models['Model-1'].parts['clay'].edges.findAt(((0.0, pile_top_vertical_limit/2, 0.0), ), ((
    pile_left_horizon_limit, pile_top_vertical_limit/2, 0.0), ), ((pile_left_horizon_limit, (pile_top_vertical_limit+clay_top_vertical_limit)/2, 0.0), ), ((0.0, (pile_top_vertical_limit+clay_top_vertical_limit)/2, 0.0), ), ((pile_right_horizon_limit, 
    (pile_top_vertical_limit+clay_top_vertical_limit)/2, 0.0), ), ((wall_left_horizon_limit, (pile_top_vertical_limit+clay_top_vertical_limit)/2, 0.0), ), ((pile_right_horizon_limit, pile_top_vertical_limit/2, 0.0), ), ((wall_left_horizon_limit, wall_bottom_vertical_limit/2, 
    0.0), ), ((wall_left_horizon_limit, (wall_bottom_vertical_limit+pile_top_vertical_limit)/2, 0.0), ), ((clay_right_horizon_limit, (wall_bottom_vertical_limit+clay_top_vertical_limit)/2, 0.0), ), ((wall_right_horizon_limit, (pile_top_vertical_limit+wall_bottom_vertical_limit)/2, 
    0.0), ), ((wall_right_horizon_limit, wall_bottom_vertical_limit/2, 0.0), ), ((clay_right_horizon_limit, wall_bottom_vertical_limit/2, 0.0), ), ), size=1.0)
mdb.models['Model-1'].parts['clay'].setMeshControls(algorithm=MEDIAL_AXIS, 
    elemShape=QUAD, regions=mdb.models['Model-1'].parts['clay'].faces.findAt(((
    pile_left_horizon_limit/2, pile_top_vertical_limit/2, 0.0), ), ((pile_left_horizon_limit/2, (pile_top_vertical_limit+clay_top_vertical_limit)/2, 0.0), ), (((pile_left_horizon_limit+pile_right_horizon_limit)/2, (pile_top_vertical_limit+clay_top_vertical_limit)/2, 
    0.0), ), (((pile_right_horizon_limit+wall_left_horizon_limit)/2, (pile_top_vertical_limit+clay_top_vertical_limit)/2, 0.0), ), (((pile_right_horizon_limit+wall_left_horizon_limit)/2, pile_top_vertical_limit/2, 0.0), ), ((
    (wall_right_horizon_limit+clay_right_horizon_limit)/2, (clay_top_vertical_limit+wall_bottom_vertical_limit)/2, 0.0), ), (((wall_left_horizon_limit+wall_right_horizon_limit)/2, wall_bottom_vertical_limit/2, 0.0), ), (((wall_right_horizon_limit+clay_right_horizon_limit)/2, 
    wall_bottom_vertical_limit/2, 0.0), ), ))
mdb.models['Model-1'].parts['clay'].setElementType(elemTypes=(ElemType(
    elemCode=CPE4P, elemLibrary=STANDARD), ElemType(elemCode=UNKNOWN_TRI, 
    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['clay'].faces.findAt(((pile_top_vertical_limit/2, pile_left_horizon_limit/2, 0.0), ), ((
    pile_top_vertical_limit/2, (pile_top_vertical_limit+clay_top_vertical_limit)/2, 0.0), ), (((pile_left_horizon_limit+pile_right_horizon_limit)/2, (pile_top_vertical_limit+clay_top_vertical_limit)/2, 0.0), ), (((pile_right_horizon_limit+wall_left_horizon_limit)/2, 
    (pile_top_vertical_limit+clay_top_vertical_limit)/2, 0.0), ), (((pile_right_horizon_limit+wall_left_horizon_limit)/2, pile_top_vertical_limit/2, 0.0), ), (((wall_right_horizon_limit+clay_right_horizon_limit)/2, clay_top_vertical_limit/2, 0.0),),
    (((wall_left_horizon_limit+wall_right_horizon_limit)/2, wall_bottom_vertical_limit/2, 0.0), ), (((wall_right_horizon_limit+clay_right_horizon_limit)/2, wall_bottom_vertical_limit/2, 0.0), ), ), ))
mdb.models['Model-1'].parts['clay'].generateMesh()
mdb.models['Model-1'].parts['pile'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=1.0)
mdb.models['Model-1'].parts['pile'].setMeshControls(algorithm=MEDIAL_AXIS, 
    elemShape=QUAD, regions=mdb.models['Model-1'].parts['pile'].faces.findAt(((
    (pile_left_horizon_limit+pile_right_horizon_limit)/2, pile_bottom_vertical_limit/2, 0.0), ), (((pile_left_horizon_limit+pile_right_horizon_limit)/2, pile_top_vertical_limit/2, 0.0), ), ))
mdb.models['Model-1'].parts['pile'].setElementType(elemTypes=(ElemType(
    elemCode=CPE4, elemLibrary=STANDARD), ElemType(elemCode=CPE3, 
    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['pile'].faces.findAt((((pile_left_horizon_limit+pile_right_horizon_limit)/2, pile_bottom_vertical_limit/2, 0.0), 
    ), (((pile_left_horizon_limit+pile_right_horizon_limit)/2, pile_top_vertical_limit/2, 0.0), ), ), ))
mdb.models['Model-1'].parts['pile'].generateMesh()
mdb.models['Model-1'].parts['wall'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=1.0)
mdb.models['Model-1'].parts['wall'].setMeshControls(algorithm=MEDIAL_AXIS, 
    elemShape=QUAD, regions=mdb.models['Model-1'].parts['wall'].faces.findAt(((
    (wall_left_horizon_limit+wall_right_horizon_limit)/2, (wall_bottom_vertical_limit+wall_mid_vertical_limit)/2, 0.0), ), (((wall_left_horizon_limit+wall_right_horizon_limit)/2, (wall_mid_vertical_limit+clay_top_vertical_limit)/2, 0.0), ), ))
mdb.models['Model-1'].parts['wall'].setElementType(elemTypes=(ElemType(
    elemCode=CPE4, elemLibrary=STANDARD), ElemType(elemCode=CPE3, 
    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['wall'].faces.findAt((((wall_left_horizon_limit+wall_right_horizon_limit)/2,(wall_bottom_vertical_limit+wall_mid_vertical_limit)/2, 
    0.0), ), (((wall_left_horizon_limit+wall_right_horizon_limit)/2, (wall_mid_vertical_limit+clay_top_vertical_limit)/2, 0.0), ), ), ))
mdb.models['Model-1'].parts['wall'].generateMesh()
mdb.models['Model-1'].steps['gravity'].setValues(matrixSolver=DIRECT, 
    matrixStorage=UNSYMMETRIC)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='gravity', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'clay_wall_lateral', region=
    mdb.models['Model-1'].rootAssembly.instances['clay-1'].sets['clay_lateral']
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
mdb.models['Model-1'].boundaryConditions['wall_bottom'].deactivate(
    'release_wall')
mdb.models['Model-1'].boundaryConditions['wall_lateral'].deactivate(
    'release_wall')
mdb.models['Model-1'].boundaryConditions['pile_int_lateral'].deactivate(
    'release_pile')
mdb.models['Model-1'].boundaryConditions['wall_bottom'].reset('release_wall')
mdb.models['Model-1'].boundaryConditions['clay_pile_lateral'].deactivate(
    'release_pile')
mdb.models['Model-1'].boundaryConditions['clay_wall_bottom'].deactivate(
    'release_wall')
mdb.models['Model-1'].boundaryConditions['clay_wall_lateral'].deactivate(
    'release_wall')
mdb.Job(activateLoadBalancing=False, atTime=None, contactPrint=OFF, 
        description='', echoPrint=OFF, explicitPrecision=SINGLE, 
        getMemoryFromAnalysis=True, historyPrint=OFF, memory=90, memoryUnits=
        PERCENTAGE, model='Model-1', modelPrint=OFF, multiprocessingMode=DEFAULT, 
        name='Job-centrifuge-wall-pile-standard', nodalOutputPrecision=SINGLE, numCpus=1, numDomains=1, 
        numGPUs=0, parallelizationMethodExplicit=DOMAIN, queue=None, resultsFormat=
        ODB, scratch='', type=ANALYSIS, userSubroutine='', waitHours=0, 
        waitMinutes=0)
# Save by augustus on 2019_01_09-23.48.17; build 2016 2015_09_25-04.31.09 126547

# Save by augustus on 2019_01_10-pile_left_horizon_limit9.19; build 2016 2015_09_25-04.31.09 126547
