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


horizon_right_limit = 58.5
horizon_left_limit = 0
vertical_up_limit = 20
vertical_mid_limit = 0
vertical_bottom_limit = -5
wall_horizon_left_limit = 8
wall_horizon_right_limit = 8.5
wall_vertical_bottom_limit = 5.0
excava_vertical_limit_3 = 12.0
excava_vertical_limit_2 = 15.0
excava_vertical_limit_1 = 18.0
crack_horizon_limit = 9.0
crack_bottom_limit = 0.0
crack_top_limit = 1.0





mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(horizon_right_limit, vertical_up_limit))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(horizon_right_limit, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(0.0, vertical_up_limit))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(wall_horizon_left_limit, vertical_up_limit))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(wall_horizon_left_limit, wall_vertical_bottom_limit))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(wall_horizon_right_limit, vertical_up_limit))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(wall_horizon_right_limit, wall_vertical_bottom_limit))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(
    0.0, vertical_up_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, vertical_up_limit/2))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, vertical_up_limit/2), 
    ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, vertical_up_limit), point2=(
    wall_horizon_left_limit, vertical_up_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_horizon_left_limit/2, vertical_up_limit))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_horizon_left_limit/2, vertical_up_limit), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, vertical_up_limit/2))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_horizon_left_limit/2, vertical_up_limit))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, vertical_up_limit/2), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    wall_horizon_left_limit/2, vertical_up_limit), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(wall_horizon_left_limit, vertical_up_limit), point2=(
    wall_horizon_left_limit, wall_vertical_bottom_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_horizon_left_limit, (wall_vertical_bottom_limit+vertical_up_limit)/2))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_horizon_left_limit, (wall_vertical_bottom_limit+vertical_up_limit)/2),))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_horizon_left_limit, (wall_vertical_bottom_limit+vertical_up_limit)/2))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_horizon_left_limit/2, vertical_up_limit), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    wall_horizon_left_limit, (wall_vertical_bottom_limit+vertical_up_limit)/2), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(wall_horizon_left_limit, wall_vertical_bottom_limit), point2=(
    wall_horizon_right_limit, wall_vertical_bottom_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt(((wall_horizon_left_limit+wall_horizon_right_limit)/2, wall_vertical_bottom_limit))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt(((wall_horizon_left_limit+wall_horizon_right_limit)/2, wall_vertical_bottom_limit), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_horizon_left_limit, (wall_vertical_bottom_limit+vertical_up_limit)/2))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt(((wall_horizon_left_limit+wall_horizon_right_limit)/2, wall_vertical_bottom_limit))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_horizon_left_limit, (wall_vertical_bottom_limit+vertical_up_limit)/2), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    (wall_horizon_left_limit+wall_horizon_right_limit)/2, wall_vertical_bottom_limit), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(wall_horizon_right_limit, wall_vertical_bottom_limit), point2=(
    wall_horizon_right_limit, vertical_up_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_horizon_right_limit, (wall_vertical_bottom_limit+vertical_up_limit)/2))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_horizon_right_limit, (wall_vertical_bottom_limit+vertical_up_limit)/2), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt(((wall_horizon_left_limit+wall_horizon_right_limit)/2, wall_vertical_bottom_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_horizon_right_limit, (wall_vertical_bottom_limit+vertical_up_limit)/2))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(addUndoState=False, entity1=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt(((wall_horizon_left_limit+wall_horizon_right_limit)/2, wall_vertical_bottom_limit), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    wall_horizon_right_limit, (wall_vertical_bottom_limit+vertical_up_limit)/2), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(wall_horizon_right_limit, vertical_up_limit), point2=(
    horizon_right_limit, vertical_up_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt(((horizon_right_limit+wall_horizon_left_limit)/2, vertical_up_limit))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt(((horizon_right_limit+wall_horizon_left_limit)/2, vertical_up_limit), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_horizon_right_limit, (wall_vertical_bottom_limit+vertical_up_limit)/2))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt(((horizon_right_limit+wall_horizon_left_limit)/2, vertical_up_limit))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_horizon_right_limit, (wall_vertical_bottom_limit+vertical_up_limit)/2), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    (horizon_right_limit+wall_horizon_left_limit)/2, vertical_up_limit), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(horizon_right_limit, vertical_up_limit), point2=
    (horizon_right_limit, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((horizon_right_limit, vertical_up_limit/2))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((horizon_right_limit, vertical_up_limit/2), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt(((horizon_right_limit+wall_horizon_left_limit)/2, vertical_up_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((horizon_right_limit, vertical_up_limit/2))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt(((horizon_right_limit+wall_horizon_left_limit)/2, vertical_up_limit), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    horizon_right_limit, vertical_up_limit/2), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(horizon_right_limit, 0.0), point2=(
    0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((horizon_right_limit/2, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((horizon_right_limit/2, 0.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((horizon_right_limit, vertical_up_limit/2))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((horizon_right_limit/2, 0.0))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((horizon_right_limit, vertical_up_limit/2), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    horizon_right_limit/2, 0.0), ))
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='up-soil', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['up-soil'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(horizon_right_limit, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(horizon_right_limit, vertical_bottom_limit))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(0.0, vertical_bottom_limit))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(
    horizon_right_limit, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((horizon_right_limit/2, 0.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((horizon_right_limit/2, 0.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(horizon_right_limit, 0.0), point2=(
    horizon_right_limit, -wall_vertical_bottom_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((horizon_right_limit, vertical_bottom_limit/2))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((horizon_right_limit, vertical_bottom_limit/2), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((horizon_right_limit/2, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((horizon_right_limit, vertical_bottom_limit/2))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((horizon_right_limit/2, 0.0), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    horizon_right_limit, vertical_bottom_limit/2), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(horizon_right_limit, -wall_vertical_bottom_limit), point2=
    (0.0, -wall_vertical_bottom_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((horizon_right_limit/2, -wall_vertical_bottom_limit))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((horizon_right_limit/2, 
    -wall_vertical_bottom_limit), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((horizon_right_limit, vertical_bottom_limit/2))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((horizon_right_limit/2, -wall_vertical_bottom_limit))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((horizon_right_limit, vertical_bottom_limit/2), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    horizon_right_limit/2, -wall_vertical_bottom_limit), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, -wall_vertical_bottom_limit), point2=(
    0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, vertical_bottom_limit/2))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, vertical_bottom_limit/2), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((horizon_right_limit/2, -wall_vertical_bottom_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, vertical_bottom_limit/2))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((horizon_right_limit/2, 
    -wall_vertical_bottom_limit), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, vertical_bottom_limit/2), 
    ))
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='bed-soil', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['bed-soil'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(wall_horizon_right_limit, wall_vertical_bottom_limit))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(wall_horizon_left_limit, wall_vertical_bottom_limit))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(wall_horizon_left_limit, vertical_up_limit))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(wall_horizon_right_limit, vertical_up_limit))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(wall_horizon_left_limit, vertical_up_limit), point2=(
    wall_horizon_right_limit, vertical_up_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt(((wall_horizon_left_limit+wall_horizon_right_limit)/2, vertical_up_limit))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt(((wall_horizon_left_limit+wall_horizon_right_limit)/2, vertical_up_limit), 
    ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(wall_horizon_right_limit, vertical_up_limit), point2=(
    wall_horizon_right_limit, wall_vertical_bottom_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_horizon_right_limit, (vertical_up_limit+wall_vertical_bottom_limit)/2))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_horizon_right_limit, (vertical_up_limit+wall_vertical_bottom_limit)/2), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt(((wall_horizon_left_limit+wall_horizon_right_limit)/2, vertical_up_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_horizon_right_limit, (vertical_up_limit+wall_vertical_bottom_limit)/2))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt(((wall_horizon_left_limit+wall_horizon_right_limit)/2, vertical_up_limit), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    wall_horizon_right_limit, (vertical_up_limit+wall_vertical_bottom_limit)/2), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(wall_horizon_right_limit, wall_vertical_bottom_limit), point2=(
    wall_horizon_left_limit, wall_vertical_bottom_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt(((wall_horizon_left_limit+wall_horizon_right_limit)/2, wall_vertical_bottom_limit))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt(((wall_horizon_left_limit+wall_horizon_right_limit)/2, wall_vertical_bottom_limit), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_horizon_right_limit, (vertical_up_limit+wall_vertical_bottom_limit)/2))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt(((wall_horizon_left_limit+wall_horizon_right_limit)/2, wall_vertical_bottom_limit))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_horizon_right_limit, (vertical_up_limit+wall_vertical_bottom_limit)/2), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    (wall_horizon_left_limit+wall_horizon_right_limit)/2, wall_vertical_bottom_limit), ))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(wall_horizon_left_limit, wall_vertical_bottom_limit), point2=(
    wall_horizon_left_limit, vertical_up_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_horizon_left_limit, (vertical_up_limit+wall_vertical_bottom_limit)/2))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_horizon_left_limit, (vertical_up_limit+wall_vertical_bottom_limit)/2), 
    ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt(((wall_horizon_left_limit+wall_horizon_right_limit)/2, wall_vertical_bottom_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((wall_horizon_left_limit, (vertical_up_limit+wall_vertical_bottom_limit)/2))
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt(((wall_horizon_left_limit+wall_horizon_right_limit)/2, wall_vertical_bottom_limit), 
    ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
    wall_horizon_left_limit, (vertical_up_limit+wall_vertical_bottom_limit)/2), ))
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='wall', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['wall'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['up-soil'].DatumPointByCoordinate(coords=(wall_horizon_right_limit, 
    excava_vertical_limit_3, 0.0))
mdb.models['Model-1'].parts['up-soil'].DatumPointByCoordinate(coords=(wall_horizon_left_limit, 
    excava_vertical_limit_3, 0.0))
del mdb.models['Model-1'].parts['up-soil'].features['Datum pt-1']
mdb.models['Model-1'].parts['up-soil'].DatumPointByCoordinate(coords=(0.0, 
    excava_vertical_limit_3, 0.0))
mdb.models['Model-1'].parts['up-soil'].DatumPointByCoordinate(coords=(wall_horizon_left_limit, 0.0, 
    0.0))
mdb.models['Model-1'].parts['up-soil'].DatumPointByCoordinate(coords=(wall_horizon_right_limit, 0.0, 
    0.0))
mdb.models['Model-1'].parts['up-soil'].DatumPointByCoordinate(coords=(wall_horizon_left_limit, wall_vertical_bottom_limit, 
    0.0))
mdb.models['Model-1'].parts['up-soil'].DatumPointByCoordinate(coords=(wall_horizon_right_limit, wall_vertical_bottom_limit, 
    0.0))
mdb.models['Model-1'].parts['up-soil'].DatumPointByCoordinate(coords=(horizon_right_limit, 
    wall_vertical_bottom_limit, 0.0))
mdb.models['Model-1'].parts['up-soil'].PartitionFaceByShortestPath(faces=
    mdb.models['Model-1'].parts['up-soil'].faces.findAt(((58.5/2, wall_vertical_bottom_limit/2, 
    0.0), )), point1=mdb.models['Model-1'].parts['up-soil'].datums[4], point2=
    mdb.models['Model-1'].parts['up-soil'].datums[3])
mdb.models['Model-1'].parts['up-soil'].PartitionFaceByShortestPath(faces=
    mdb.models['Model-1'].parts['up-soil'].faces.findAt(((wall_horizon_left_limit, vertical_up_limit/2, 
    0.0), )), point1=mdb.models['Model-1'].parts['up-soil'].datums[7], point2=
    mdb.models['Model-1'].parts['up-soil'].datums[5])
mdb.models['Model-1'].parts['up-soil'].PartitionFaceByShortestPath(faces=
    mdb.models['Model-1'].parts['up-soil'].faces.findAt((((wall_horizon_left_limit+wall_horizon_right_limit)/2, wall_vertical_bottom_limit/2, 
    0.0), )), point1=mdb.models['Model-1'].parts['up-soil'].datums[8], point2=
    mdb.models['Model-1'].parts['up-soil'].datums[6])
mdb.models['Model-1'].parts['up-soil'].PartitionFaceByShortestPath(faces=
    mdb.models['Model-1'].parts['up-soil'].faces.findAt(((horizon_right_limit/2, wall_vertical_bottom_limit/2, 
    0.0), )), point1=mdb.models['Model-1'].parts['up-soil'].datums[8], point2=
    mdb.models['Model-1'].parts['up-soil'].datums[9])
mdb.models['Model-1'].parts['wall'].DatumPointByCoordinate(coords=(wall_horizon_left_limit, excava_vertical_limit_3, 
    0.0))
mdb.models['Model-1'].parts['wall'].DatumPointByCoordinate(coords=(wall_horizon_right_limit, excava_vertical_limit_3, 
    0.0))
mdb.models['Model-1'].parts['wall'].DatumPointByCoordinate(coords=(0.0, 0.0, 
    0.0))
mdb.models['Model-1'].parts['wall'].PartitionFaceByShortestPath(faces=
    mdb.models['Model-1'].parts['wall'].faces.findAt((((wall_horizon_left_limit+wall_horizon_right_limit)/2, vertical_up_limit/2, 0.0), ))
    , point1=mdb.models['Model-1'].parts['wall'].datums[2], point2=
    mdb.models['Model-1'].parts['wall'].datums[3])
mdb.models['Model-1'].parts['bed-soil'].DatumPointByCoordinate(coords=(wall_horizon_left_limit, 
    0.0, 0.0))
mdb.models['Model-1'].parts['bed-soil'].DatumPointByCoordinate(coords=(wall_horizon_left_limit, 
    -wall_vertical_bottom_limit, 0.0))
mdb.models['Model-1'].parts['bed-soil'].DatumPointByCoordinate(coords=(wall_horizon_right_limit, 
    0.0, 0.0))
mdb.models['Model-1'].parts['bed-soil'].DatumPointByCoordinate(coords=(wall_horizon_right_limit, 
    -wall_vertical_bottom_limit, 0.0))
mdb.models['Model-1'].parts['bed-soil'].PartitionFaceByShortestPath(faces=
    mdb.models['Model-1'].parts['bed-soil'].faces.findAt(((horizon_right_limit/2, vertical_bottom_limit/2, 
    0.0), )), point1=mdb.models['Model-1'].parts['bed-soil'].datums[2], point2=
    mdb.models['Model-1'].parts['bed-soil'].datums[3])
mdb.models['Model-1'].parts['bed-soil'].PartitionFaceByShortestPath(faces=
    mdb.models['Model-1'].parts['bed-soil'].faces.findAt(((horizon_right_limit/2, 
    vertical_bottom_limit/2, 0.0), )), point1=
    mdb.models['Model-1'].parts['bed-soil'].datums[4], point2=
    mdb.models['Model-1'].parts['bed-soil'].datums[5])
mdb.models['Model-1'].parts['up-soil'].DatumPointByCoordinate(coords=(0.0, 
    excava_vertical_limit_1, 0.0))
mdb.models['Model-1'].parts['up-soil'].DatumPointByCoordinate(coords=(wall_horizon_left_limit, 
    excava_vertical_limit_1, 0.0))
mdb.models['Model-1'].parts['up-soil'].DatumPointByCoordinate(coords=(0.0, 
    excava_vertical_limit_2, 0.0))
mdb.models['Model-1'].parts['up-soil'].DatumPointByCoordinate(coords=(wall_horizon_left_limit, 
    excava_vertical_limit_2, 0.0))
mdb.models['Model-1'].parts['up-soil'].PartitionFaceByShortestPath(faces=
    mdb.models['Model-1'].parts['up-soil'].faces.findAt(((wall_horizon_left_limit/2, (excava_vertical_limit_2+excava_vertical_limit_3)/2,
    0.0), )), point1=mdb.models['Model-1'].parts['up-soil'].datums[14], point2=
    mdb.models['Model-1'].parts['up-soil'].datums[15])
mdb.models['Model-1'].parts['up-soil'].PartitionFaceByShortestPath(faces=
    mdb.models['Model-1'].parts['up-soil'].faces.findAt(((wall_horizon_left_limit/2, (excava_vertical_limit_1+excava_vertical_limit_2)/2, 0.0),
    )), point1=mdb.models['Model-1'].parts['up-soil'].datums[16], point2=
    mdb.models['Model-1'].parts['up-soil'].datums[17])
mdb.models['Model-1'].parts['up-soil'].Set(edges=
    mdb.models['Model-1'].parts['up-soil'].edges.findAt(((horizon_right_limit, vertical_up_limit/2, 0.0), ), 
    ((horizon_right_limit, wall_vertical_bottom_limit/2, 0.0), ), ), name='right')
mdb.models['Model-1'].parts['up-soil'].Set(edges=
    mdb.models['Model-1'].parts['up-soil'].edges.findAt(((0.0, (excava_vertical_limit_1+vertical_up_limit)/2, 0.0), ), 
    ((0.0,(excava_vertical_limit_1+excava_vertical_limit_2)/2 , 0.0), ), ((0.0, (excava_vertical_limit_2+excava_vertical_limit_3)/2, 0.0), ), ((0.0, excava_vertical_limit_3/2, 0.0), ), ), name=
    'left')
mdb.models['Model-1'].parts['up-soil'].Set(faces=
    mdb.models['Model-1'].parts['up-soil'].faces.findAt(((wall_horizon_left_limit/2, (excava_vertical_limit_1+vertical_up_limit)/2, 
    0.0), )), name='excavation-1')
mdb.models['Model-1'].parts['up-soil'].Set(faces=
    mdb.models['Model-1'].parts['up-soil'].faces.findAt(((wall_horizon_left_limit, (excava_vertical_limit_2+excava_vertical_limit_1)/2, 0.0), 
    )), name='excavation-2')
mdb.models['Model-1'].parts['up-soil'].Set(faces=
    mdb.models['Model-1'].parts['up-soil'].faces.findAt(((wall_horizon_left_limit, (excava_vertical_limit_3+excava_vertical_limit_2)/2, 0.0), 
    )), name='excavation-3')
mdb.models['Model-1'].parts['up-soil'].Surface(name='excavation-1', side1Edges=
    mdb.models['Model-1'].parts['up-soil'].edges.findAt(((wall_horizon_left_limit, (excava_vertical_limit_1+vertical_up_limit)/2, 0.0), )))
mdb.models['Model-1'].parts['up-soil'].Surface(name='excavation-2', side1Edges=
    mdb.models['Model-1'].parts['up-soil'].edges.findAt(((wall_horizon_left_limit, (excava_vertical_limit_2+excava_vertical_limit_1)/2, 0.0), )))
mdb.models['Model-1'].parts['up-soil'].Surface(name='excavation-3', side1Edges=
    mdb.models['Model-1'].parts['up-soil'].edges.findAt(((wall_horizon_left_limit, (excava_vertical_limit_3+excava_vertical_limit_2)/2, 0.0), )))
mdb.models['Model-1'].parts['up-soil'].Surface(name='non-excavation', 
    side1Edges=mdb.models['Model-1'].parts['up-soil'].edges.findAt(((wall_horizon_right_limit, (wall_vertical_bottom_limit+vertical_up_limit)/2, 
    0.0), ), (((wall_horizon_left_limit+wall_horizon_right_limit)/2 , wall_vertical_bottom_limit, 0.0), ), ((wall_horizon_left_limit, (excava_vertical_limit_3+wall_vertical_bottom_limit)/2, 0.0), ), ))
mdb.models['Model-1'].parts['up-soil'].Surface(name='bottom', side1Edges=
    mdb.models['Model-1'].parts['up-soil'].edges.findAt((((wall_horizon_right_limit+horizon_right_limit)/2, 0.0, 0.0), ), (
    ((wall_horizon_left_limit+wall_horizon_right_limit)/2, 0.0, 0.0), ), ((wall_horizon_left_limit/2, 0.0, 0.0), ), ))
mdb.models['Model-1'].parts['up-soil'].Set(faces=
    mdb.models['Model-1'].parts['up-soil'].faces.findAt(((wall_horizon_left_limit/2, (excava_vertical_limit_2+excava_vertical_limit_1)/2, 0.0), 
    ), ((wall_horizon_left_limit/2, (excava_vertical_limit_1+vertical_up_limit)/2, 0.0), ), (((wall_horizon_right_limit+horizon_right_limit)/2, (wall_vertical_bottom_limit+vertical_up_limit)/2, 0.0), ), (((wall_horizon_right_limit+horizon_right_limit)/2, 
    wall_vertical_bottom_limit/2, 0.0), ), (((wall_horizon_left_limit+wall_horizon_right_limit)/2, wall_vertical_bottom_limit/2, 0.0), ), ((wall_horizon_left_limit/2, (excava_vertical_limit_3+excava_vertical_limit_2)/2, 0.0), 
    ), ((wall_horizon_left_limit/2, excava_vertical_limit_3/2, 0.0), ), ), name='up-soil')
mdb.models['Model-1'].parts['bed-soil'].Set(faces=
    mdb.models['Model-1'].parts['bed-soil'].faces.findAt((((wall_horizon_right_limit+horizon_right_limit)/2, 
    vertical_bottom_limit/2, 0.0), ), (((wall_horizon_left_limit+wall_horizon_right_limit)/2, vertical_bottom_limit/2, 0.0), ), ((wall_horizon_left_limit/2, vertical_bottom_limit/2, 
    0.0), ), ), name='bed-soil')
mdb.models['Model-1'].parts['bed-soil'].Set(edges=
    mdb.models['Model-1'].parts['bed-soil'].edges.findAt(((0.0,vertical_bottom_limit/2, 0.0), ))
    , name='left')
mdb.models['Model-1'].parts['bed-soil'].Set(edges=
    mdb.models['Model-1'].parts['bed-soil'].edges.findAt(((horizon_right_limit, vertical_bottom_limit/2, 0.0), 
    )), name='right')
mdb.models['Model-1'].parts['bed-soil'].Set(edges=
    mdb.models['Model-1'].parts['bed-soil'].edges.findAt((((wall_horizon_right_limit+horizon_right_limit)/2, vertical_bottom_limit, 0.0), ), 
    (((wall_horizon_left_limit+wall_horizon_right_limit)/2, vertical_bottom_limit, 0.0), ), ((wall_horizon_left_limit/2, vertical_bottom_limit, 0.0), ), ), name='bottom')
mdb.models['Model-1'].parts['bed-soil'].Surface(name='up', side1Edges=
    mdb.models['Model-1'].parts['bed-soil'].edges.findAt((((wall_horizon_right_limit+horizon_right_limit)/2, 0.0, 0.0), ), 
    (((wall_horizon_left_limit+wall_horizon_right_limit)/2, 0.0, 0.0), ), ((wall_horizon_left_limit/2, 0.0, 0.0), ), ))
mdb.models['Model-1'].parts['wall'].Set(faces=
    mdb.models['Model-1'].parts['wall'].faces.findAt((((wall_horizon_left_limit+wall_horizon_right_limit)/2, (excava_vertical_limit_3+vertical_up_limit)/2,
    0.0), ), (((wall_horizon_left_limit+wall_horizon_right_limit)/2, (excava_vertical_limit_3+wall_vertical_bottom_limit)/2, 0.0), ), ), name='wall')
mdb.models['Model-1'].parts['wall'].DatumPointByCoordinate(coords=(wall_horizon_left_limit, excava_vertical_limit_2,
    0.0))
mdb.models['Model-1'].parts['wall'].DatumPointByCoordinate(coords=(wall_horizon_right_limit, excava_vertical_limit_2,
    0.0))
mdb.models['Model-1'].parts['wall'].DatumPointByCoordinate(coords=(wall_horizon_left_limit, excava_vertical_limit_1,
    0.0))
mdb.models['Model-1'].parts['wall'].DatumPointByCoordinate(coords=(wall_horizon_right_limit, excava_vertical_limit_1,
    0.0))
mdb.models['Model-1'].parts['wall'].PartitionFaceByShortestPath(faces=
    mdb.models['Model-1'].parts['wall'].faces.findAt((((wall_horizon_left_limit+wall_horizon_right_limit)/2, (excava_vertical_limit_3+excava_vertical_limit_2)/2, 
    0.0), )), point1=mdb.models['Model-1'].parts['wall'].datums[7], point2=
    mdb.models['Model-1'].parts['wall'].datums[8])
mdb.models['Model-1'].parts['wall'].PartitionFaceByShortestPath(faces=
    mdb.models['Model-1'].parts['wall'].faces.findAt((((wall_horizon_left_limit+wall_horizon_right_limit)/2, (excava_vertical_limit_2+excava_vertical_limit_1)/2, 
    0.0), )), point1=mdb.models['Model-1'].parts['wall'].datums[9], point2=
    mdb.models['Model-1'].parts['wall'].datums[10])
mdb.models['Model-1'].parts['wall'].Set(edges=
    mdb.models['Model-1'].parts['wall'].edges.findAt(((wall_horizon_left_limit, (excava_vertical_limit_1+vertical_up_limit)/2, 0.0), ), ((
    wall_horizon_left_limit, (excava_vertical_limit_2+excava_vertical_limit_1)/2, 0.0), ), ((wall_horizon_left_limit, (excava_vertical_limit_3+excava_vertical_limit_2)/2, 0.0), ), ((wall_horizon_left_limit, (excava_vertical_limit_3+wall_vertical_bottom_limit)/2, 0.0), ), ), name=
    'left')
mdb.models['Model-1'].parts['wall'].Set(edges=
    mdb.models['Model-1'].parts['wall'].edges.findAt(((wall_horizon_right_limit, (excava_vertical_limit_1+vertical_up_limit)/2, 0.0), ), ((
    wall_horizon_right_limit, (excava_vertical_limit_2+excava_vertical_limit_1)/2, 0.0), ), ((wall_horizon_right_limit, (excava_vertical_limit_3+excava_vertical_limit_2)/2, 0.0), ), ((wall_horizon_right_limit, (excava_vertical_limit_3+wall_vertical_bottom_limit)/2, 0.0), ), ), name=
    'right')
mdb.models['Model-1'].parts['wall'].Set(edges=
    mdb.models['Model-1'].parts['wall'].edges.findAt((((wall_horizon_left_limit+wall_horizon_right_limit)/2, wall_vertical_bottom_limit, 0.0), )), 
    name='bottom')
mdb.models['Model-1'].parts['wall'].Surface(name='excavation-1', side1Edges=
    mdb.models['Model-1'].parts['wall'].edges.findAt(((wall_horizon_left_limit, (excava_vertical_limit_1+vertical_up_limit)/2, 0.0), )))
mdb.models['Model-1'].parts['wall'].Surface(name='excavation-2', side1Edges=
    mdb.models['Model-1'].parts['wall'].edges.findAt(((wall_horizon_left_limit, (excava_vertical_limit_2+excava_vertical_limit_1)/2, 0.0), )))
mdb.models['Model-1'].parts['wall'].Surface(name='excavation-3', side1Edges=
    mdb.models['Model-1'].parts['wall'].edges.findAt(((wall_horizon_left_limit, (excava_vertical_limit_3+excava_vertical_limit_2)/2, 0.0), )))
mdb.models['Model-1'].parts['wall'].Surface(name='non-excavation', side1Edges=
    mdb.models['Model-1'].parts['wall'].edges.findAt(((wall_horizon_right_limit, (excava_vertical_limit_1+vertical_up_limit)/2, 0.0), ), ((
    wall_horizon_right_limit, (excava_vertical_limit_2+excava_vertical_limit_1)/2, 0.0), ), ((wall_horizon_right_limit, (excava_vertical_limit_3+excava_vertical_limit_2)/2, 0.0), ), ((wall_horizon_left_limit, (excava_vertical_limit_3+wall_vertical_bottom_limit)/2, 0.0), ), (((wall_horizon_left_limit+wall_horizon_right_limit)/2, 
    wall_vertical_bottom_limit, 0.0), ), ((wall_horizon_right_limit, (excava_vertical_limit_3+wall_vertical_bottom_limit)/2, 0.0), ), ))
mdb.models['Model-1'].Material(name='up-soil')
mdb.models['Model-1'].materials['up-soil'].Density(table=((1500.0, ), ))
mdb.models['Model-1'].materials['up-soil'].Elastic(table=((10000000.0, 0.3), ))
mdb.models['Model-1'].materials['up-soil'].MaxpsDamageInitiation(position=
    CRACKTIP, table=((10000.0, ), ), tolerance=0.1)
mdb.models['Model-1'].materials['up-soil'].maxpsDamageInitiation.DamageEvolution(
    mixedModeBehavior=POWER_LAW, power=1.0, table=((10000.0, 10000.0, 10000.0), 
    ), type=ENERGY)
mdb.models['Model-1'].materials['up-soil'].maxpsDamageInitiation.DamageStabilizationCohesive(
    cohesiveCoeff=1e-05)
mdb.models['Model-1'].materials['up-soil'].GapFlow(table=((1e-06, ), ))
mdb.models['Model-1'].materials['up-soil'].FluidLeakoff(table=((5.879e-16, 
    5.879e-16), ))
mdb.models['Model-1'].materials['up-soil'].Permeability(
    inertialDragCoefficient=0.142887, specificWeight=10000.0, table=((
    2.618e-05, 0.0), ))
mdb.models['Model-1'].Material(name='bed-soil')
mdb.models['Model-1'].materials['bed-soil'].Density(table=((1500.0, ), ))
mdb.models['Model-1'].materials['bed-soil'].Elastic(table=((1000000000.0, 0.3), 
    ))
mdb.models['Model-1'].Material(name='wall')
mdb.models['Model-1'].materials['wall'].Density(table=((1500.0, ), ))
mdb.models['Model-1'].materials['wall'].Elastic(table=((1000000000.0, 0.3), ))
mdb.models['Model-1'].HomogeneousSolidSection(material='up-soil', name=
    'up-soil', thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='bed-soil', name=
    'bed-soil', thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='wall', name='wall', 
    thickness=None)
mdb.models['Model-1'].parts['wall'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['wall'].sets['wall'], sectionName='wall', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['up-soil'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['up-soil'].sets['up-soil'], sectionName=
    'up-soil', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['bed-soil'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['bed-soil'].sets['bed-soil'], sectionName=
    'bed-soil', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='bed-soil-1', 
    part=mdb.models['Model-1'].parts['bed-soil'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='up-soil-1', 
    part=mdb.models['Model-1'].parts['up-soil'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='wall-1', part=
    mdb.models['Model-1'].parts['wall'])
mdb.models['Model-1'].parts['bed-soil'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=1.0)
mdb.models['Model-1'].parts['bed-soil'].setMeshControls(algorithm=MEDIAL_AXIS, 
    elemShape=QUAD, regions=
    mdb.models['Model-1'].parts['bed-soil'].faces.findAt((((horizon_right_limit+wall_horizon_right_limit)/2, 
    vertical_bottom_limit/2, 0.0), ), (((wall_horizon_left_limit+wall_horizon_right_limit)/2, vertical_bottom_limit/2, 0.0), ), ((wall_horizon_left_limit/2, vertical_bottom_limit/2, 
    0.0), ), ))
mdb.models['Model-1'].parts['bed-soil'].setElementType(elemTypes=(ElemType(
    elemCode=CPE4, elemLibrary=STANDARD), ElemType(elemCode=CPE3, 
    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['bed-soil'].faces.findAt((((horizon_right_limit+wall_horizon_right_limit)/2, 
    vertical_bottom_limit/2, 0.0), ), (((wall_horizon_left_limit+wall_horizon_right_limit)/2, vertical_bottom_limit/2, 0.0), ), ((wall_horizon_left_limit/2, vertical_bottom_limit/2, 
    0.0), ), ), ))
mdb.models['Model-1'].parts['bed-soil'].generateMesh()
mdb.models['Model-1'].parts['up-soil'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=1.0)
mdb.models['Model-1'].parts['up-soil'].setMeshControls(algorithm=MEDIAL_AXIS, 
    elemShape=QUAD, regions=
    mdb.models['Model-1'].parts['up-soil'].faces.findAt(((wall_horizon_left_limit/2, (excava_vertical_limit_2+excava_vertical_limit_1)/2, 0.0), 
    ), ((wall_horizon_left_limit/2, (excava_vertical_limit_1+vertical_up_limit)/2, 0.0), ), (((wall_horizon_right_limit+horizon_right_limit)/2, (wall_vertical_bottom_limit+excava_vertical_limit_3)/2, 0.0), ), (((wall_horizon_right_limit+horizon_right_limit)/2, 
    wall_vertical_bottom_limit/2, 0.0), ), (((wall_horizon_left_limit+wall_horizon_right_limit)/2, wall_vertical_bottom_limit/2, 0.0), ), ((wall_horizon_left_limit/2, (excava_vertical_limit_3+excava_vertical_limit_2)/2, 0.0), 
    ), ((wall_horizon_left_limit/2, wall_vertical_bottom_limit/2, 0.0), ), ))
mdb.models['Model-1'].parts['up-soil'].setElementType(elemTypes=(ElemType(
    elemCode=CPE4P, elemLibrary=STANDARD), ElemType(elemCode=UNKNOWN_TRI, 
    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['up-soil'].faces.findAt(((wall_horizon_left_limit/2,  (excava_vertical_limit_2+excava_vertical_limit_1)/2, 0.0), 
    ), ((wall_horizon_left_limit/2, (excava_vertical_limit_1+vertical_up_limit)/2, 0.0), ), (((wall_horizon_right_limit+horizon_right_limit)/2, (wall_vertical_bottom_limit+excava_vertical_limit_3)/2, 0.0), ), (((wall_horizon_right_limit+horizon_right_limit)/2, 
    wall_vertical_bottom_limit/2, 0.0), ), (((wall_horizon_left_limit+wall_horizon_right_limit)/2, wall_vertical_bottom_limit/2, 0.0), ), ((wall_horizon_left_limit/2, (excava_vertical_limit_3+excava_vertical_limit_2)/2, 0.0), 
    ), ((wall_horizon_left_limit/2, wall_vertical_bottom_limit/2, 0.0), ), ), ))
mdb.models['Model-1'].parts['up-soil'].generateMesh()
mdb.models['Model-1'].parts['wall'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=1.0)
mdb.models['Model-1'].parts['wall'].setMeshControls(algorithm=MEDIAL_AXIS, 
    elemShape=QUAD, regions=mdb.models['Model-1'].parts['wall'].faces.findAt(((
   (wall_horizon_left_limit+wall_horizon_right_limit)/2,(excava_vertical_limit_1+vertical_up_limit)/2, 0.0), ), (((wall_horizon_left_limit+wall_horizon_right_limit)/2, (excava_vertical_limit_2+excava_vertical_limit_1)/2, 0.0), ), (((wall_horizon_left_limit+wall_horizon_right_limit)/2, (excava_vertical_limit_3+excava_vertical_limit_2)/2, 
    0.0), ), (((wall_horizon_left_limit+wall_horizon_right_limit)/2, (excava_vertical_limit_3+wall_vertical_bottom_limit)/2, 0.0), ), ))
mdb.models['Model-1'].parts['wall'].setElementType(elemTypes=(ElemType(
    elemCode=CPE4, elemLibrary=STANDARD), ElemType(elemCode=CPE3, 
    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['wall'].faces.findAt((((wall_horizon_left_limit+wall_horizon_right_limit)/2,(excava_vertical_limit_1+vertical_up_limit)/2, 
    0.0), ), (((wall_horizon_left_limit+wall_horizon_right_limit)/2,(excava_vertical_limit_2+excava_vertical_limit_1)/2, 0.0), ), (((wall_horizon_left_limit+wall_horizon_right_limit)/2, (excava_vertical_limit_3+excava_vertical_limit_2)/2, 0.0), ), (((wall_horizon_left_limit+wall_horizon_right_limit)/2, 
    (excava_vertical_limit_3+wall_vertical_bottom_limit)/2, 0.0), ), ), ))
mdb.models['Model-1'].parts['wall'].generateMesh()
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].parts['up-soil'].Set(elements=
    mdb.models['Model-1'].parts['up-soil'].elements[0:1165], name='eall')
mdb.models['Model-1'].parts['up-soil'].Set(name='nall', nodes=
    mdb.models['Model-1'].parts['up-soil'].nodes[0:1260])
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].GeostaticStep(name='gra', previous='Initial')
mdb.models['Model-1'].SoilsStep(cetol=None, creep=OFF, end=None, name=
    'excavation-1', previous='gra', utol=1000000000.0)
mdb.models['Model-1'].SoilsStep(cetol=None, creep=OFF, end=None, name=
    'excavtion-2', previous='excavation-1', utol=1000000000.0)
mdb.models['Model-1'].SoilsStep(cetol=None, creep=OFF, end=None, name=
    'excavtion-3', previous='excavtion-2', utol=1000000000.0)
mdb.models['Model-1'].SoilsStep(cetol=None, creep=OFF, end=None, minInc=1e-12, 
    name='injection', previous='excavtion-3', utol=1000000000.0)
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
    'S', 'LE', 'U', 'RF', 'CF', 'CSTRESS', 'CDISP', 'PHILSM', 'PSILSM', 
    'VOIDR', 'SAT', 'POR'))
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(crack_horizon_limit, crack_bottom_limit))
mdb.models['Model-1'].sketches['__profile__'].Spot(point=(crack_horizon_limit, crack_top_limit))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(crack_horizon_limit, crack_top_limit), point2=(
    crack_horizon_limit, crack_bottom_limit))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((crack_horizon_limit, (crack_top_limit+crack_bottom_limit)/2))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((crack_horizon_limit, (crack_top_limit+crack_bottom_limit)/2), 
    ))
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='crack', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['crack'].BaseWire(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['crack'].Set(edges=
    mdb.models['Model-1'].parts['crack'].edges.findAt(((crack_horizon_limit, (crack_top_limit+crack_bottom_limit)/2, 0.0), )), 
    name='crack')
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='crack-1', part=
    mdb.models['Model-1'].parts['crack'])
mdb.models['Model-1'].rootAssembly.engineeringFeatures.XFEMCrack(crackDomain=
    mdb.models['Model-1'].rootAssembly.instances['up-soil-1'].sets['up-soil'], 
    crackLocation=
    mdb.models['Model-1'].rootAssembly.instances['crack-1'].sets['crack'], 
    name='Crack-1')
mdb.models['Model-1'].ContactProperty('IntProp-1')
mdb.models['Model-1'].interactionProperties['IntProp-1'].TangentialBehavior(
    dependencies=0, directionality=ISOTROPIC, elasticSlipStiffness=None, 
    formulation=PENALTY, fraction=0.005, maximumElasticSlip=FRACTION, 
    pressureDependency=OFF, shearStressLimit=None, slipRateDependency=OFF, 
    table=((0.15, ), ), temperatureDependency=OFF)
mdb.models['Model-1'].interactionProperties['IntProp-1'].NormalBehavior(
    allowSeparation=ON, constraintEnforcementMethod=DEFAULT, 
    pressureOverclosure=HARD)
mdb.models['Model-1'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='Initial', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='IntProp-1', master=
    mdb.models['Model-1'].rootAssembly.instances['wall-1'].surfaces['non-excavation']
    , name='non-excavation', slave=
    mdb.models['Model-1'].rootAssembly.instances['up-soil-1'].surfaces['non-excavation']
    , sliding=FINITE, thickness=ON)
mdb.models['Model-1'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='Initial', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='IntProp-1', master=
    mdb.models['Model-1'].rootAssembly.instances['wall-1'].surfaces['excavation-1']
    , name='exca-1', slave=
    mdb.models['Model-1'].rootAssembly.instances['up-soil-1'].surfaces['excavation-1']
    , sliding=FINITE, thickness=ON)
mdb.models['Model-1'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='Initial', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='IntProp-1', master=
    mdb.models['Model-1'].rootAssembly.instances['wall-1'].surfaces['excavation-2']
    , name='exca-2', slave=
    mdb.models['Model-1'].rootAssembly.instances['up-soil-1'].surfaces['excavation-2']
    , sliding=FINITE, thickness=ON)
mdb.models['Model-1'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='Initial', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='IntProp-1', master=
    mdb.models['Model-1'].rootAssembly.instances['wall-1'].surfaces['excavation-3']
    , name='exca-3', slave=
    mdb.models['Model-1'].rootAssembly.instances['up-soil-1'].surfaces['excavation-3']
    , sliding=FINITE, thickness=ON)
mdb.models['Model-1'].ModelChange(activeInStep=False, createStepName=
    'excavation-1', includeStrain=False, name='excavation-1', region=
    mdb.models['Model-1'].rootAssembly.instances['up-soil-1'].sets['excavation-1'])
mdb.models['Model-1'].ModelChange(activeInStep=False, createStepName=
    'excavation-1', includeStrain=False, name='excavation-2', region=
    mdb.models['Model-1'].rootAssembly.instances['up-soil-1'].sets['excavation-2'])
mdb.models['Model-1'].interactions['excavation-2'].move('excavation-1', 
    'excavtion-2')
mdb.models['Model-1'].interactions['exca-1'].deactivate('excavation-1')
mdb.models['Model-1'].interactions['exca-2'].deactivate('excavtion-2')
mdb.models['Model-1'].interactions['exca-3'].deactivate('excavtion-3')
mdb.models['Model-1'].ModelChange(activeInStep=False, createStepName=
    'excavation-1', includeStrain=False, name='excavation-3', region=
    mdb.models['Model-1'].rootAssembly.instances['up-soil-1'].sets['excavation-3'])
mdb.models['Model-1'].interactions['excavation-3'].move('excavation-1', 
    'excavtion-2')
mdb.models['Model-1'].interactions['excavation-3'].move('excavtion-2', 
    'excavtion-3')
mdb.models['Model-1'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='Initial', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='IntProp-1', master=
    mdb.models['Model-1'].rootAssembly.instances['bed-soil-1'].surfaces['up'], 
    name='up-bed', slave=
    mdb.models['Model-1'].rootAssembly.instances['up-soil-1'].surfaces['bottom']
    , sliding=FINITE, thickness=ON)
mdb.models['Model-1'].Gravity(comp2=-10.0, createStepName='gra', 
    distributionType=UNIFORM, field='', name='gravity')
mdb.models['Model-1'].XsymmBC(createStepName='Initial', localCsys=None, name=
    'up-left', region=
    mdb.models['Model-1'].rootAssembly.instances['up-soil-1'].sets['left'])
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='up-right', 
    region=
    mdb.models['Model-1'].rootAssembly.instances['up-soil-1'].sets['right'], 
    u1=SET, u2=UNSET, ur3=UNSET)
mdb.models['Model-1'].XsymmBC(createStepName='Initial', localCsys=None, name=
    'bed-left', region=
    mdb.models['Model-1'].rootAssembly.instances['bed-soil-1'].sets['left'])
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='bed-right', 
    region=
    mdb.models['Model-1'].rootAssembly.instances['bed-soil-1'].sets['right'], 
    u1=SET, u2=UNSET, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='bed-bottom', 
    region=
    mdb.models['Model-1'].rootAssembly.instances['bed-soil-1'].sets['bottom'], 
    u1=SET, u2=SET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='wall-left', 
    region=mdb.models['Model-1'].rootAssembly.instances['wall-1'].sets['left'], 
    u1=SET, u2=UNSET, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='wall-right', 
    region=mdb.models['Model-1'].rootAssembly.instances['wall-1'].sets['right']
    , u1=SET, u2=UNSET, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='wall-bottom', 
    region=
    mdb.models['Model-1'].rootAssembly.instances['wall-1'].sets['bottom'], u1=
    UNSET, u2=SET, ur3=UNSET)
mdb.models['Model-1'].boundaryConditions['wall-left'].deactivate(
    'excavation-1')
mdb.models['Model-1'].boundaryConditions['wall-right'].deactivate(
    'excavation-1')
mdb.models['Model-1'].boundaryConditions['wall-bottom'].deactivate(
    'excavation-1')
mdb.models['Model-1'].ExpressionField(description='', expression='20 -  Y ', 
    localCsys=None, name='AnalyticalField-1')
mdb.models['Model-1'].PorePressure(distributionType=FIELD, field=
    'AnalyticalField-1', name='pore', porePressure1=10000.0, region=
    mdb.models['Model-1'].rootAssembly.instances['up-soil-1'].sets['nall'], 
    variation=CONSTANT_RATIO)
mdb.models['Model-1'].VoidsRatio(distributionType=UNIFORM, name='void', region=
    mdb.models['Model-1'].rootAssembly.instances['up-soil-1'].sets['nall'], 
    variation=CONSTANT_RATIO, voidsRatio1=1.0)
mdb.models['Model-1'].GeostaticStress(lateralCoeff1=0.6, lateralCoeff2=None, 
    name='geo', region=
    mdb.models['Model-1'].rootAssembly.instances['up-soil-1'].sets['up-soil'], 
    stressMag1=0.0, stressMag2=-300000.0, vCoord1=vertical_up_limit, vCoord2=0.0)
mdb.models['Model-1'].predefinedFields.changeKey(fromName='geo', toName=
    'geo-up')
mdb.models['Model-1'].GeostaticStress(lateralCoeff1=0.6, lateralCoeff2=None, 
    name='geo-bed', region=
    mdb.models['Model-1'].rootAssembly.instances['bed-soil-1'].sets['bed-soil']
    , stressMag1=-300000.0, stressMag2=-375000.0, vCoord1=0.0, vCoord2=-wall_vertical_bottom_limit)
mdb.models['Model-1'].predefinedFields['geo-up'].setValues(stressMag2=
    -200000.0)
mdb.models['Model-1'].predefinedFields['geo-bed'].setValues(stressMag1=
    -200000.0, stressMag2=-275000.0)
mdb.models['Model-1'].boundaryConditions['wall-left'].reset('excavation-1')
mdb.models['Model-1'].boundaryConditions['wall-right'].reset('excavation-1')
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name='Job-centrifuge', nodalOutputPrecision=
    SINGLE, numCpus=1, numGPUs=0, queue=None, resultsFormat=ODB, scratch='', 
    type=ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
mdb.jobs['Job-centrifuge'].submit(consistencyChecking=OFF)
# Save by augustus on 2019_03_10-10.1wall_horizon_left_limit4; build 2016 2015_09_25-04.31.09 126547
