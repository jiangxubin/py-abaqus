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
mdb.Model(modelType=STANDARD_EXPLICIT, name='Model-1')

from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup

import datetime
import os
import sys
sys.path.append("D:\\thesis\\mini-thesis\\py_thesis\\src")
from auto_inp import PYXFEM


in_inp_path = "D:\\thesis\\mini-thesis\\centrifuge\\Job-centrifuge.inp"
out_inp_path = "D:\\thesis\\mini-thesis\\centrifuge\\Job-centrifuge-modify.inp"
root_path = "D:\\thesis\\mini-thesis\\centrifuge\\"
# now = datetime.datetime.now()
# job_name = "Centrifuge-{}".format(now.strftime("%Y-%m-%d-%H:%M"))


parameter = dict()
parameter['max_horizon_limit'] = 41.5
parameter['mid_horizon_limit'] = 0.0
parameter['min_horizon_limit'] = -41.5

parameter['max_vertical_limit'] = 20.0
parameter['mid_vertical_limit'] = 0.0
parameter['min_vertical_limit'] = -5.0

parameter['excavation_bottom'] = 12.0
parameter['max_excavation_vertical_limit'] = 10.0
parameter['min_excavation_vertical_limit'] = 2.0


parameter['flow_rate'] = 5e-5




# excavation=13
# parameter['max_excavation_horizon_limit'] = 6.5
# parameter['min_execavation_horizon_limit'] = -6.5
# parameter['crack_horizon_limit'] = 0.0
# parameter['crack_node_left'] = 140
# parameter['crack_node_right'] = 141

# excavation=15
# parameter['max_excavation_horizon_limit'] = 7.5
# parameter['min_execavation_horizon_limit'] = -7.5
# parameter['crack_horizon_limit_bottom'] = 0.0
# parameter['crack_horizon_limit_mid'] = 0.0
# parameter['crack_horizon_limit_top'] = 0.0
# parameter['crack_vertical_limit_bottom'] = 0.0
# parameter['crack_vertical_limit_mid'] = 0.5
# parameter['crack_vertical_limit_top'] = 1.0
# parameter['crack_node_left'] = 143
# parameter['crack_node_right'] = 144


# excavation=17
parameter['max_excavation_horizon_limit'] = 8.5
parameter['min_execavation_horizon_limit'] = -8.5
parameter['crack_horizon_limit_bottom'] = 0.0
parameter['crack_horizon_limit_mid'] = 0.0
parameter['crack_horizon_limit_top'] = 0.0
parameter['crack_vertical_limit_bottom'] = 0.0
parameter['crack_vertical_limit_mid'] = 0.5
parameter['crack_vertical_limit_top'] = 1.0
parameter['crack_node_left'] = 146
parameter['crack_node_right'] = 147

# parameter['max_excavation_horizon_limit'] = 8.5
# parameter['min_execavation_horizon_limit'] = -8.5
# parameter['crack_horizon_limit_bottom'] = 0.8
# parameter['crack_horizon_limit_mid'] = 1.0
# parameter['crack_horizon_limit_top'] = 1.2
# parameter['crack_vertical_limit_bottom'] = 1.0
# parameter['crack_vertical_limit_mid'] = 1.5
# parameter['crack_vertical_limit_top'] = 2.0
# parameter['crack_node_left'] = 1058
# parameter['crack_node_right'] = 1047

# excavation=19
# parameter['max_excavation_horizon_limit'] = 9.5
# parameter['min_execavation_horizon_limit'] = -9.5
# parameter['crack_horizon_limit_bottom'] = 0.0
# parameter['crack_horizon_limit_mid'] = 0.0
# parameter['crack_horizon_limit_top'] = 0.0
# parameter['crack_vertical_limit_bottom'] = 0.0
# parameter['crack_vertical_limit_mid'] = 0.5
# parameter['crack_vertical_limit_top'] = 1.0
# parameter['crack_node_left'] = 149
# parameter['crack_node_right'] = 150

# excavation=21
# parameter['max_excavation_horizon_limit'] = 10.5
# parameter['min_execavation_horizon_limit'] = -10.5
# parameter['crack_horizon_limit_bottom'] = 0.0
# parameter['crack_horizon_limit_mid'] = 0.0
# parameter['crack_horizon_limit_top'] = 0.0
# parameter['crack_vertical_limit_bottom'] = 0.0
# parameter['crack_vertical_limit_mid'] = 0.5
# parameter['crack_vertical_limit_top'] = 1.0
# parameter['crack_node_left'] = 152
# parameter['crack_node_right'] = 153


# excavation=23
# parameter['max_excavation_horizon_limit'] = 11.5
# parameter['min_execavation_horizon_limit'] = -11.5
# parameter['crack_horizon_limit'] = 0.0
# parameter['crack_node_left'] = 155
# parameter['crack_node_right'] = 156

# excavation=25
# parameter['max_excavation_horizon_limit'] = 12.5
# parameter['min_execavation_horizon_limit'] = -12.5
# parameter['crack_horizon_limit'] = 0.0
# parameter['crack_node_left'] = 158
# parameter['crack_node_right'] = 159







# parameter['crack_horizon_limit'] = 1.0
# parameter['crack_node_left'] = 147
# parameter['crack_node_right'] = 148

# parameter['crack_horizon_limit'] = 2.0
# parameter['crack_node_left'] = 148
# parameter['crack_node_right'] = 149

# parameter['crack_horizon_limit'] = 6.0
# parameter['crack_node_left'] = 152
# parameter['crack_node_right'] = 153


def pre_process(parameter):
    mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
    mdb.models['Model-1'].sketches['__profile__'].Spot(point=(parameter['max_horizon_limit'], parameter['max_vertical_limit']))
    mdb.models['Model-1'].sketches['__profile__'].Spot(point=(parameter['max_horizon_limit'], 0.0))
    mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-parameter['max_horizon_limit'], parameter['max_vertical_limit']))
    mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-parameter['max_horizon_limit'], 0.0))
    mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-parameter['max_horizon_limit'], parameter['max_vertical_limit']), 
        point2=(parameter['max_horizon_limit'], 0.0))
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
    mdb.models['Model-1'].sketches['__profile__'].Spot(point=(parameter['max_excavation_horizon_limit'], parameter['max_excavation_vertical_limit']))
    mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-parameter['max_excavation_horizon_limit'], parameter['max_excavation_vertical_limit']))
    mdb.models['Model-1'].sketches['__profile__'].Spot(point=(parameter['max_excavation_horizon_limit'], parameter['min_excavation_vertical_limit']))
    mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-parameter['max_excavation_horizon_limit'], parameter['min_excavation_vertical_limit']))
    mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-parameter['max_excavation_horizon_limit'], parameter['max_excavation_vertical_limit']), point2=
        (-parameter['max_excavation_horizon_limit'], parameter['min_excavation_vertical_limit']))
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-parameter['max_excavation_horizon_limit'], 6.0))
    mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
        False, entity=
        mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-parameter['max_excavation_horizon_limit'], 6.0), 
        ))
    mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-parameter['max_excavation_horizon_limit'], parameter['min_excavation_vertical_limit']), point2=(
        parameter['max_excavation_horizon_limit'], parameter['min_excavation_vertical_limit']))
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, parameter['min_excavation_vertical_limit']))
    mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
        addUndoState=False, entity=
        mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, parameter['min_excavation_vertical_limit']), 
        ))
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-parameter['max_excavation_horizon_limit'], 6.0))
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, parameter['min_excavation_vertical_limit']))
    mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
        addUndoState=False, entity1=
        mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-parameter['max_excavation_horizon_limit'], 6.0), 
        ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
        0.0, parameter['min_excavation_vertical_limit']), ))
    mdb.models['Model-1'].sketches['__profile__'].Line(point1=(parameter['max_excavation_horizon_limit'], parameter['min_excavation_vertical_limit']), point2=(
        parameter['max_excavation_horizon_limit'], parameter['max_excavation_vertical_limit']))
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((parameter['max_excavation_horizon_limit'], 6.0))
    mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
        False, entity=
        mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((parameter['max_excavation_horizon_limit'], 6.0), 
        ))
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, parameter['min_excavation_vertical_limit']))
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((parameter['max_excavation_horizon_limit'], 6.0))
    mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
        addUndoState=False, entity1=
        mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, parameter['min_excavation_vertical_limit']), )
        , entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
        parameter['max_excavation_horizon_limit'], 6.0), ))
    mdb.models['Model-1'].parts['soil'].PartitionFaceBySketch(faces=
        mdb.models['Model-1'].parts['soil'].faces.findAt(((10.0, 13.333333, 0.0), 
        )), sketch=mdb.models['Model-1'].sketches['__profile__'])
    del mdb.models['Model-1'].sketches['__profile__']
    mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
    mdb.models['Model-1'].sketches['__profile__'].Spot(point=(parameter['max_horizon_limit'], 0.0))
    mdb.models['Model-1'].sketches['__profile__'].Spot(point=(parameter['max_horizon_limit'], parameter['min_vertical_limit']))
    mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-parameter['max_horizon_limit'], 0.0))
    mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-parameter['max_horizon_limit'], parameter['min_vertical_limit']))
    mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-parameter['max_horizon_limit'], 0.0), point2=
        (-parameter['max_horizon_limit'], parameter['min_vertical_limit']))
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-parameter['max_horizon_limit'], -2.5))
    mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
        False, entity=
        mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-parameter['max_horizon_limit'], 
        -2.5), ))
    mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-parameter['max_horizon_limit'], parameter['min_vertical_limit']), 
        point2=(parameter['max_horizon_limit'], parameter['min_vertical_limit']))
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, parameter['min_vertical_limit']))
    mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
        addUndoState=False, entity=
        mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, parameter['min_vertical_limit']), 
        ))
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-parameter['max_horizon_limit'], -2.5))
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, parameter['min_vertical_limit']))
    mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
        addUndoState=False, entity1=
        mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-parameter['max_horizon_limit'], 
        -2.5), ), entity2=
        mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, parameter['min_vertical_limit']), 
        ))
    mdb.models['Model-1'].sketches['__profile__'].Line(point1=(parameter['max_horizon_limit'], parameter['min_vertical_limit']), point2=
        (parameter['max_horizon_limit'], 0.0))
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((parameter['max_horizon_limit'], -2.5))
    mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
        False, entity=
        mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((parameter['max_horizon_limit'], -2.5), 
        ))
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, parameter['min_vertical_limit']))
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((parameter['max_horizon_limit'], -2.5))
    mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
        addUndoState=False, entity1=
        mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, parameter['min_vertical_limit']), 
        ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
        parameter['max_horizon_limit'], -2.5), ))
    mdb.models['Model-1'].sketches['__profile__'].Line(point1=(parameter['max_horizon_limit'], 0.0), point2=(
        -parameter['max_horizon_limit'], 0.0))
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 0.0))
    mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
        addUndoState=False, entity=
        mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 0.0), 
        ))
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((parameter['max_horizon_limit'], -2.5))
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 0.0))
    mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
        addUndoState=False, entity1=
        mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((parameter['max_horizon_limit'], -2.5), 
        ), entity2=mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((
        0.0, 0.0), ))
    mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='rock', type=
        DEFORMABLE_BODY)
    mdb.models['Model-1'].parts['rock'].BaseShell(sketch=
        mdb.models['Model-1'].sketches['__profile__'])
    del mdb.models['Model-1'].sketches['__profile__']
    # mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
    # mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-7.0, 0.0))
    # mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-7.0, 1.0))
    # mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-7.0, 1.0), point2=(
    #     -7.0, 0.0))
    # mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-7.0, 0.5))
    # mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    #     False, entity=
    #     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-7.0, 0.5), 
    #     ))
    # mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='left-crack', 
    #     type=DEFORMABLE_BODY)
    # mdb.models['Model-1'].parts['left-crack'].BaseWire(sketch=
    #     mdb.models['Model-1'].sketches['__profile__'])
    # del mdb.models['Model-1'].sketches['__profile__']
    # mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
    # mdb.models['Model-1'].sketches['__profile__'].Spot(point=(7.0, 0.0))
    # mdb.models['Model-1'].sketches['__profile__'].Spot(point=(7.0, 1.0))
    # mdb.models['Model-1'].sketches['__profile__'].Line(point1=(7.0, 1.0), point2=(
    #     7.0, 0.0))
    # mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.0, 0.5))
    # mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    #     False, entity=
    #     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((7.0, 0.5), 
    #     ))
    # mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='right-crack', 
    #     type=DEFORMABLE_BODY)
    # mdb.models['Model-1'].parts['right-crack'].BaseWire(sketch=
    #     mdb.models['Model-1'].sketches['__profile__'])
    # del mdb.models['Model-1'].sketches['__profile__']
    # mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
    # mdb.models['Model-1'].sketches['__profile__'].Spot(point=(parameter['crack_horizon_limit_bottom'], parameter['crack_vertical_limit_bottom']))
    # mdb.models['Model-1'].sketches['__profile__'].Spot(point=(parameter['crack_horizon_limit_top'], parameter['crack_vertical_limit_top']))
    # mdb.models['Model-1'].sketches['__profile__'].Line(point1=(parameter['crack_horizon_limit_top'], parameter['crack_vertical_limit_top']), point2=(
    #     parameter['crack_horizon_limit_bottom'], parameter['crack_vertical_limit_bottom']))
    # mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((parameter['crack_horizon_limit_mid'], parameter['crack_vertical_limit_mid']))
    # mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    #     False, entity=
    #     mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((parameter['crack_horizon_limit_mid'], parameter['crack_vertical_limit_mid']), 
    #     ))
    # mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='middle-crack', 
    #     type=DEFORMABLE_BODY)
    # mdb.models['Model-1'].parts['middle-crack'].BaseWire(sketch=
    #     mdb.models['Model-1'].sketches['__profile__'])
    # del mdb.models['Model-1'].sketches['__profile__']

    mdb.models['Model-1'].Material(name='soil')
    mdb.models['Model-1'].materials['soil'].Density(table=((1616.0, ), ))
    mdb.models['Model-1'].materials['soil'].Elastic(table=((6e06, 0.17), ))
    mdb.models['Model-1'].materials['soil'].MaxpsDamageInitiation(position=CRACKTIP, table=((9e04, ),), tolerance=0.1)
    mdb.models['Model-1'].materials['soil'].maxpsDamageInitiation.DamageEvolution(
        mixedModeBehavior=POWER_LAW, power=1.0, table=((0.01, 0.01, 0.01), 
        ), type=ENERGY)
    mdb.models['Model-1'].materials['soil'].maxpsDamageInitiation.DamageStabilizationCohesive(
        cohesiveCoeff=0.0001)
    mdb.models['Model-1'].materials['soil'].FluidLeakoff(table=((5.879e-16, 
        5.879e-16), ))
    mdb.models['Model-1'].materials['soil'].GapFlow(table=((1e-06, ), ))
    mdb.models['Model-1'].materials['soil'].Permeability(inertialDragCoefficient=
        0.142887, specificWeight=10000.0, table=((2.418e-05, 0.0), ))
    # mdb.models['Model-1'].Material(name='rock')
    # mdb.models['Model-1'].materials['rock'].Density(table=((3000.0, ), ))
    # mdb.models['Model-1'].materials['rock'].Elastic(table=((5e08, 0.0), ))
    # mdb.models['Model-1'].materials['rock'].Permeability(inertialDragCoefficient=
    #     0.142887, specificWeight=10000.0, table=((2.418e-019, 0.0), ))
    mdb.models['Model-1'].HomogeneousSolidSection(material='soil', name='soil', 
        thickness=None)
    mdb.models['Model-1'].HomogeneousSolidSection(material='soil', name='rock', 
        thickness=None)
    mdb.models['Model-1'].parts['soil'].Set(faces=
        mdb.models['Model-1'].parts['soil'].faces.findAt(((0, parameter['max_vertical_limit'], 
        0.0), ), ((0, parameter['mid_vertical_limit']+1, 0.0), ), ), name='soil')
    mdb.models['Model-1'].parts['rock'].Set(faces=
        mdb.models['Model-1'].parts['rock'].faces.findAt(((0, parameter['min_vertical_limit']/2, 0.0), 
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
    # mdb.models['Model-1'].rootAssembly.Instance(dependent=OFF, name='left-crack-1', 
    #     part=mdb.models['Model-1'].parts['left-crack'])
    # mdb.models['Model-1'].rootAssembly.Instance(dependent=OFF, name='right-crack-1'
    #     , part=mdb.models['Model-1'].parts['right-crack'])
    # mdb.models['Model-1'].rootAssembly.Instance(dependent=OFF, name='middle-crack-1'
    #     , part=mdb.models['Model-1'].parts['middle-crack'])
    mdb.models['Model-1'].rootAssembly.Instance(dependent=OFF, name='rock-1', part=
        mdb.models['Model-1'].parts['rock'])
    mdb.models['Model-1'].rootAssembly.Instance(dependent=OFF, name='soil-1', part=
        mdb.models['Model-1'].parts['soil'])
    mdb.models['Model-1'].GeostaticStep(matrixSolver=DIRECT, matrixStorage=
        UNSYMMETRIC, name='gravity', nlgeom=ON, previous='Initial')
    mdb.models['Model-1'].SoilsStep(cetol=None, initialInc=1.0, matrixSolver=DIRECT
        , matrixStorage=UNSYMMETRIC, maxInc=1.0, minInc=1e-12, name='execavation', 
        previous='gravity', timePeriod=1, utol=1e09)
    mdb.models['Model-1'].SoilsStep(cetol=None, initialInc=0.05, matrixSolver=DIRECT
        , matrixStorage=UNSYMMETRIC, maxInc=1.0, minInc=1e-12, name='pore-balance', 
        previous='execavation', timePeriod=1.0, utol=1e09)
    mdb.models['Model-1'].SoilsStep(cetol=None, initialInc=0.05, matrixSolver=
        DIRECT, matrixStorage=UNSYMMETRIC, maxInc=5.0, minInc=1e-12, name=
        'injection', previous='pore-balance', timePeriod=100.0, utol=1e09)
    mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
        'S', 'LE', 'U', 'RF', 'CF', 'CSTRESS', 'CDISP', 'PHILSM', 'PSILSM', 
        'VOIDR', 'SAT', 'POR', 'JK', 'ENRRT', 'EFENRRTR', 'DMICRT', 'OPENBC'))
    # mdb.models['Model-1'].HistoryOutputRequest(name='H-Output-3', 
    # createStepName='injection', contourIntegral='Crack-1', 
    # sectionPoints=DEFAULT, rebar=EXCLUDE, numberOfContours=2)
    mdb.models['Model-1'].steps['injection'].control.setValues(allowPropagation=OFF
        , discontinuous=ON, resetDefaultValues=OFF, timeIncrementation=(8.0, 10.0, 
        9.0, 16.0, 10.0, 4.0, 12.0, 20.0, 6.0, 3.0, 50.0))
    mdb.models['Model-1'].ContactProperty('IntProp-1')
    mdb.models['Model-1'].ContactProperty('IntProp-2')
    mdb.models['Model-1'].interactionProperties['IntProp-2'].TangentialBehavior(
        formulation=FRICTIONLESS)
    mdb.models['Model-1'].interactionProperties['IntProp-2'].NormalBehavior(
        allowSeparation=ON, constraintEnforcementMethod=DEFAULT, 
        pressureOverclosure=HARD)
    mdb.models['Model-1'].rootAssembly.Surface(name='rock-master', side1Edges=
        mdb.models['Model-1'].rootAssembly.instances['rock-1'].edges.findAt(((0, 
        0.0, 0.0), )))
    mdb.models['Model-1'].rootAssembly.Surface(name='soil-slave', side1Edges=
        mdb.models['Model-1'].rootAssembly.instances['soil-1'].edges.findAt(((
        0, 0.0, 0.0), )))
    mdb.models['Model-1'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
        clearanceRegion=None, createStepName='Initial', datumAxis=None, 
        initialClearance=OMIT, interactionProperty='IntProp-2', master=
        mdb.models['Model-1'].rootAssembly.surfaces['rock-master'], name='Int-1', 
        slave=mdb.models['Model-1'].rootAssembly.surfaces['soil-slave'], sliding=
        FINITE, thickness=ON)
    mdb.models['Model-1'].rootAssembly.Set(faces=
        mdb.models['Model-1'].rootAssembly.instances['soil-1'].faces.findAt(((
        parameter['min_horizon_limit']/2, parameter['max_vertical_limit']/2, 0.0), (0.0, 0.0, 1.0)), ((parameter['max_horizon_limit']/2, parameter['max_vertical_limit']/2, 
        0.0), (0.0, 0.0, 1.0)), )+\
        mdb.models['Model-1'].rootAssembly.instances['rock-1'].faces.findAt(((parameter['max_horizon_limit']/2, 
        parameter['min_vertical_limit']/2, 0.0), (0.0, 0.0, 1.0)), ), name='gravity')
    mdb.models['Model-1'].Gravity(comp2=-10.0, createStepName='gravity', 
        distributionType=UNIFORM, field='', name='gravity', region=
        mdb.models['Model-1'].rootAssembly.sets['gravity'])
    mdb.models['Model-1'].TabularAmplitude(data=((0.0, 0.0), (25.0, -200.0),(50,-250.0) ), name=
        'volumerate', smooth=SOLVER_DEFAULT, timeSpan=STEP)
    mdb.models['Model-1'].rootAssembly.Surface(name='rock-up-bc-edge', side1Edges=
        mdb.models['Model-1'].rootAssembly.instances['rock-1'].edges.findAt(((0.0, 
        0.0, 0.0), )))
    mdb.models['Model-1'].rootAssembly.Set(edges=
        mdb.models['Model-1'].rootAssembly.instances['soil-1'].edges.findAt(((
        parameter['min_execavation_horizon_limit'], parameter['max_vertical_limit'], 0.0), )), name='left-prop-edge')
    mdb.models['Model-1'].rootAssembly.Set(edges=
        mdb.models['Model-1'].rootAssembly.instances['soil-1'].edges.findAt(((
        parameter['max_horizon_limit'], parameter['max_vertical_limit'], 0.0), )), name='right-prop-edge')
    mdb.models['Model-1'].rootAssembly.Set(edges=
        mdb.models['Model-1'].rootAssembly.instances['soil-1'].edges.findAt(((parameter['min_execavation_horizon_limit'],
        parameter['max_vertical_limit']-1, 0.0), ), ((0, parameter['excavation_bottom'], 0.0), ), ((parameter['max_excavation_horizon_limit'], parameter['max_vertical_limit']-1, 0.0), ), ((parameter['min_horizon_limit']+1, parameter['max_vertical_limit'],
        0.0), ), ((parameter['max_horizon_limit']-1, parameter['max_vertical_limit'], 0.0), ), ), name='soil-up-after-pore-bc-edge')
    mdb.models['Model-1'].rootAssembly.Set(edges=
        mdb.models['Model-1'].rootAssembly.instances['soil-1'].edges.findAt(((0.0, 
        parameter['max_vertical_limit'], 0.0), ), ((parameter['min_horizon_limit']+1, parameter['max_vertical_limit'], 0.0), ), ((parameter['max_horizon_limit']-1, parameter['max_vertical_limit'], 0.0), ), ), name=
        'soil-up-before-pore-bc-edge')
    mdb.models['Model-1'].rootAssembly.Set(edges=
        mdb.models['Model-1'].rootAssembly.instances['soil-1'].edges.findAt(((
        parameter['min_horizon_limit'], parameter['max_vertical_limit']-1, 0.0), ), )+\
        mdb.models['Model-1'].rootAssembly.instances['rock-1'].edges.findAt(((
        parameter['min_horizon_limit'], parameter['min_vertical_limit']+1, 0.0), ), ), name='left-bc-edge')
    mdb.models['Model-1'].rootAssembly.Set(edges=
        mdb.models['Model-1'].rootAssembly.instances['soil-1'].edges.findAt(((parameter['max_horizon_limit'], 
        parameter['max_vertical_limit']-1, 0.0), ), )+\
        mdb.models['Model-1'].rootAssembly.instances['rock-1'].edges.findAt(((parameter['max_horizon_limit'], 
        parameter['min_vertical_limit']+1, 0.0), ), ), name='right-bc-edge')
    mdb.models['Model-1'].rootAssembly.Set(edges=
        mdb.models['Model-1'].rootAssembly.instances['rock-1'].edges.findAt(((
        0.0, parameter['min_vertical_limit'], 0.0), )), name='rock-bottom-bc-edge')
    mdb.models['Model-1'].rootAssembly.Set(edges=
        mdb.models['Model-1'].rootAssembly.instances['rock-1'].edges.findAt(((0.0, 
        0.0, 0.0), )), name='rock-up-bc-edge')
    mdb.models['Model-1'].rootAssembly.Set(edges=
        mdb.models['Model-1'].rootAssembly.instances['soil-1'].edges.findAt(((
        parameter['min_horizon_limit'], parameter['max_vertical_limit']-1, 0.0), )), name='soil-left-pore-bc-edge')
    mdb.models['Model-1'].rootAssembly.Set(edges=
        mdb.models['Model-1'].rootAssembly.instances['soil-1'].edges.findAt(((parameter['max_horizon_limit'], 
        parameter['max_vertical_limit']-1, 0.0), )), name='soil-right-pore-bc-edge')
    mdb.models['Model-1'].rootAssembly.Set(edges=
        mdb.models['Model-1'].rootAssembly.instances['soil-1'].edges.findAt(((
        0.0, 0.0, 0.0), )), name='soil-bottom-pore-bc-edge')
    # mdb.models['Model-1'].rootAssembly.Set(edges=
    #     mdb.models['Model-1'].rootAssembly.instances['middle-crack-1'].edges.findAt(
    #     ((parameter['crack_horizon_limit_mid'], parameter['crack_vertical_limit_mid'], 0.0), )), name='middle-crack')
    mdb.models['Model-1'].rootAssembly.Set(faces=
        mdb.models['Model-1'].rootAssembly.instances['soil-1'].faces.findAt(((
        0, parameter['max_vertical_limit']-1, 0.0), )), name='excavation-face')
    # mdb.models['Model-1'].rootAssembly.engineeringFeatures.XFEMCrack(crackDomain=
    #     mdb.models['Model-1'].rootAssembly.instances['soil-1'].sets['soil'], 
    #     crackLocation=mdb.models['Model-1'].rootAssembly.sets['middle-crack'], 
    #     interactionProperty='IntProp-1', name='Crack-1')
    mdb.models['Model-1'].ModelChange(activeInStep=False, createStepName=
        'execavation', includeStrain=False, name='excavation', region=
        mdb.models['Model-1'].rootAssembly.sets['excavation-face'])
    mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
        distributionType=UNIFORM, fieldName='', localCsys=None, name='left-bc', 
        region=mdb.models['Model-1'].rootAssembly.sets['left-bc-edge'], u1=SET, u2=
        SET, ur3=UNSET)
    mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
        distributionType=UNIFORM, fieldName='', localCsys=None, name='right-bc', 
        region=mdb.models['Model-1'].rootAssembly.sets['right-bc-edge'], u1=SET, 
        u2=SET, ur3=UNSET)
    mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
        distributionType=UNIFORM, fieldName='', localCsys=None, name='rock-bottom-bc', 
        region=mdb.models['Model-1'].rootAssembly.sets['rock-bottom-bc-edge'], u1=
        SET, u2=SET, ur3=UNSET)
    mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
        distributionType=UNIFORM, fieldName='', localCsys=None, name='rock-up-bc', 
        region=mdb.models['Model-1'].rootAssembly.sets['rock-up-bc-edge'], u1=SET, 
        u2=SET, ur3=UNSET)
    mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName=
        'execavation', distributionType=UNIFORM, fieldName='', fixed=OFF, 
        localCsys=None, name='left-prop', region=
        mdb.models['Model-1'].rootAssembly.sets['left-prop-edge'], u1=0.0, u2=0.0, ur3=
        UNSET)
    mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName=
        'execavation', distributionType=UNIFORM, fieldName='', fixed=OFF, 
        localCsys=None, name='right-prop', region=
        mdb.models['Model-1'].rootAssembly.sets['right-prop-edge'], u1=0.0, u2=0.0, ur3=
        UNSET)
    mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName=
        'injection', distributionType=UNIFORM, fieldName='', fixed=OFF, 
        localCsys=None, name='prop_bc', region=
        mdb.models['Model-1'].rootAssembly.sets['soil-up-after-pore-bc-edge'], u1=
        0.0, u2=0.0, ur3=UNSET)
    # mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    #     distributionType=UNIFORM, fieldName='', localCsys=None, name='soil-bottom-bc', 
    #     region=mdb.models['Model-1'].rootAssembly.sets['soil-bottom-pore-bc-edge'], 
    #     u1=SET, u2=SET, ur3=UNSET)
    mdb.models['Model-1'].ExpressionField(description='', expression='20 -  Y ', 
        localCsys=None, name='AnalyticalField-1')
    mdb.models['Model-1'].PorePressureBC(amplitude=UNSET, createStepName='gravity', 
        distributionType=FIELD, fieldName='AnalyticalField-1', fixed=OFF, 
        magnitude=10000.0, name='left-pore-bc', region=
        mdb.models['Model-1'].rootAssembly.sets['soil-left-pore-bc-edge'])
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
        'pore-balance', distributionType=UNIFORM, fieldName='', fixed=OFF, 
        magnitude=0.0, name='after-exe-up-pore-bc', region=
        mdb.models['Model-1'].rootAssembly.sets['soil-up-after-pore-bc-edge'])
    mdb.models['Model-1'].GeostaticStress(lateralCoeff1=0.7, lateralCoeff2=None, 
        name='geo-soil', region=
        mdb.models['Model-1'].rootAssembly.instances['soil-1'].sets['soil'], 
        stressMag1=0.0, stressMag2=-323200.0, vCoord1=parameter['max_vertical_limit'], vCoord2=parameter['mid_vertical_limit'])
    mdb.models['Model-1'].GeostaticStress(lateralCoeff1=0.7, lateralCoeff2=None, 
        name='geo-rock', region=
        mdb.models['Model-1'].rootAssembly.instances['rock-1'].sets['rock'], 
        stressMag1=-323200.0, stressMag2=-404000.0, vCoord1=parameter['mid_vertical_limit'], vCoord2=parameter['min_vertical_limit'])
    # mdb.models['Model-1'].predefinedFields['geo-soil'].setValues(stressMag2=
    #     -323200.0)
    mdb.models['Model-1'].VoidsRatio(distributionType=UNIFORM, name='void-soil', region=
        mdb.models['Model-1'].rootAssembly.instances['soil-1'].sets['soil'], 
        variation=CONSTANT_RATIO, voidsRatio1=0.64)
    mdb.models['Model-1'].VoidsRatio(distributionType=UNIFORM, name='void-rock', region=
        mdb.models['Model-1'].rootAssembly.instances['rock-1'].sets['rock'], 
        variation=CONSTANT_RATIO, voidsRatio1=0.001)
    mdb.models['Model-1'].PorePressure(distributionType=FIELD, field=
        'AnalyticalField-1', name='pore', porePressure1=10000.0, region=
        mdb.models['Model-1'].rootAssembly.instances['soil-1'].sets['soil'], 
        variation=CONSTANT_RATIO)
    region = mdb.models['Model-1'].rootAssembly.surfaces['soil-slave']
    mdb.models['Model-1'].Pressure(name='uplift_pore', createStepName='injection', 
    region=region, distributionType=UNIFORM, field='', magnitude=2000000.0, 
    amplitude=UNSET)


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

    # mdb.models['Model-1'].rootAssembly.seedPartInstance(deviationFactor=0.1, 
    #     minSizeFactor=0.1, regions=(
    #     mdb.models['Model-1'].rootAssembly.instances['soil-1'], ), size=1.0)
    # mdb.models['Model-1'].rootAssembly.seedPartInstance(deviationFactor=0.1, 
    #     minSizeFactor=0.1, regions=(
    #     mdb.models['Model-1'].rootAssembly.instances['rock-1'], ), size=1.0)
    # mdb.models['Model-1'].rootAssembly.setMeshControls(algorithm=MEDIAL_AXIS, 
    #     elemShape=QUAD, regions=
    #     mdb.models['Model-1'].rootAssembly.instances['soil-1'].faces.findAt(((
    #     -2.666667, 14.666667, 0.0), ), ((-15.333333, 17.333333, 0.0), ), ))
    # mdb.models['Model-1'].rootAssembly.setElementType(elemTypes=(ElemType(
    #     elemCode=CPE4P, elemLibrary=STANDARD), ElemType(elemCode=UNKNOWN_TRI, 
    #     elemLibrary=STANDARD)), regions=(
    #     mdb.models['Model-1'].rootAssembly.instances['soil-1'].faces.findAt(((
    #     -2.666667, 14.666667, 0.0), ), ((-15.333333, 17.333333, 0.0), ), ), ))
    # mdb.models['Model-1'].rootAssembly.generateMesh(regions=(
    #     mdb.models['Model-1'].rootAssembly.instances['soil-1'], ))
    # mdb.models['Model-1'].rootAssembly.setMeshControls(algorithm=MEDIAL_AXIS, 
    #     elemShape=QUAD, regions=
    #     mdb.models['Model-1'].rootAssembly.instances['rock-1'].faces.findAt(((10.0, 
    #     -1.666667, 0.0), )))
    # mdb.models['Model-1'].rootAssembly.generateMesh(regions=(
    #     mdb.models['Model-1'].rootAssembly.instances['rock-1'], ))

    mdb.models['Model-1'].rootAssembly.seedPartInstance(deviationFactor=0.1, 
        minSizeFactor=0.1, regions=(
        mdb.models['Model-1'].rootAssembly.instances['soil-1'], ), size=1.0)
    mdb.models['Model-1'].rootAssembly.setMeshControls(algorithm=MEDIAL_AXIS, elemShape=QUAD, regions=
        mdb.models['Model-1'].rootAssembly.instances['soil-1'].faces.findAt(((
        -2.833333, 12.0, 0.0), ), ((-19.5, 16.0, 0.0), ), ))
    mdb.models['Model-1'].rootAssembly.setElementType(elemTypes=(ElemType(
        elemCode=CPE4P, elemLibrary=STANDARD), ElemType(elemCode=UNKNOWN_TRI, 
        elemLibrary=STANDARD)), regions=(
        mdb.models['Model-1'].rootAssembly.instances['soil-1'].faces.findAt(((
        -2.833333, 12.0, 0.0), ), ((-19.5, 16.0, 0.0), ), ), ))
    mdb.models['Model-1'].rootAssembly.seedPartInstance(deviationFactor=0.1, 
        minSizeFactor=0.1, regions=(
        mdb.models['Model-1'].rootAssembly.instances['rock-1'], ), size=2.0)
    mdb.models['Model-1'].rootAssembly.setMeshControls(algorithm=MEDIAL_AXIS, elemShape=QUAD, regions=
        mdb.models['Model-1'].rootAssembly.instances['rock-1'].faces.findAt(((
        13.833333, -1.666667, 0.0), )))
    mdb.models['Model-1'].rootAssembly.setElementType(elemTypes=(ElemType(
        elemCode=CPE4P, elemLibrary=STANDARD), ElemType(elemCode=UNKNOWN_TRI, 
        elemLibrary=STANDARD)), regions=(
        mdb.models['Model-1'].rootAssembly.instances['rock-1'].faces.findAt(((
        13.833333, -1.666667, 0.0), )), ))
    mdb.models['Model-1'].rootAssembly.generateMesh(regions=(
        mdb.models['Model-1'].rootAssembly.instances['rock-1'], ))
    mdb.models['Model-1'].rootAssembly.generateMesh(regions=(
        mdb.models['Model-1'].rootAssembly.instances['soil-1'], ))
    mdb.models['Model-1'].rootAssembly.Surface(face3Elements=
        mdb.models['Model-1'].rootAssembly.instances['soil-1'].elements[1640:1641], 
        name='penetration-surface')
    # mdb.models['Model-1'].SurfacePoreFluid(createStepName='injection', magnitude=
    #     200000.0, name='penetration-pore', region=
    #     mdb.models['Model-1'].rootAssembly.surfaces['penetration-surface'])
    # mdb.models['Model-1'].Pressure(amplitude=UNSET, createStepName='injection', 
    #     distributionType=UNIFORM, field='', magnitude=2000000.0, name='penetration-pore', 
    #     region=mdb.models['Model-1'].rootAssembly.surfaces['penetration-surface'])
    now = datetime.datetime.now()
    job_name = "Centrifuge-{}".format(now.strftime("%Y-%m-%d-%H-%M"))

    mdb.Job(activateLoadBalancing=False, atTime=None, contactPrint=OFF, 
        description='', echoPrint=OFF, explicitPrecision=SINGLE, 
        getMemoryFromAnalysis=True, historyPrint=OFF, memory=90, memoryUnits=
        PERCENTAGE, model='Model-1', modelPrint=OFF, multiprocessingMode=DEFAULT, 
        name=job_name, nodalOutputPrecision=SINGLE, numCpus=1, numDomains=1, 
        numGPUs=0, parallelizationMethodExplicit=DOMAIN, queue=None, resultsFormat=
        ODB, scratch='', type=ANALYSIS, userSubroutine='', waitHours=0, 
        waitMinutes=0)
    mdb.jobs[job_name].writeInput(consistencyChecking=OFF)
    mdb.jobs[job_name].submit(consistencyChecking=OFF)
    mdb.jobs[job_name].waitForCompletion()
    return job_name

def clear_results(job_name):
    suffixs = [".com", ".dat", ".ipm", ".log", ".mdl", ".msg", ".prt", ".sim", ".sta", ".stt"]
    for item in suffixs:
        full_file_name = job_name + item
        full_path = os.path.join(root_path, full_file_name)
        if os.path.exists(full_path):
            try:
                os.remove(full_path)
            except WindowsError:
                pass
    if os.path.exists(in_inp_path):
        try:
            os.remove(in_inp_path)
        except WindowsError:
            pass
    if os.path.exists(out_inp_path):
        try:
            os.remove(out_inp_path)
        except WindowsError:
            pass
    return None

def post_process(odb_name, query_variable):
    odb_full_path = root_path + odb_name + ".odb"
    o = session.openOdb(name=odb_full_path)
    odb = session.odbs[odb_full_path]
    session.viewports['Viewport: 1'].setValues(displayedObject=o)
    session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='injection', frame=93)
    # leaf = dgo.LeafFromNodeSets(nodeSets=('EXCAVATION-FACE', 
    # ))
    # print(leaf.__doc__)
    # print(dir(leaf))
    # print(len(leaf.nodeSets[0]))
    # for item in leaf.nodeSets[0]:
    #     print(item)
    ra = odb.rootAssembly
    # print(dir(ra))
    nodeSets = ra.nodeSets
    # print(len(ns))
    target_ns = nodeSets["addedNX_XFEM+001ASSEMBLY_SOIL-1_SOIL"]
    node_0 = target_ns.nodes[0]
    for item in node_0:
        print(item)


    # for item in nodes:
    #     print(item)
    # xy_data = session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    # 'PFOPENXFEM', WHOLE_ELEMENT), ), nodeLabels=(('SOIL-1', ('146')), ))
    # print("XYdata created succeed!")
    # x_data = [item[0] for item in xy_data[0]]
    # y_data = [item[1] for item in xy_data[0]]
    # with open("D:\\thesis\\mini-thesis\\py_thesis\\data\\abqus_script_result\\x_{}.txt".format(odb_name), "w") as f_x:
    #     for item in x_data:
    #         f_x.write(str(item)+"\n")
    # with open("D:\\thesis\\mini-thesis\\py_thesis\\data\\abqus_script_result\\y_{}.txt".format(odb_name), "w") as f_y:
    #     for item in y_data:
    #         f_y.write(str(item)+"\n")
    # return x_data, y_data


if __name__ == "__main__":
    job_name = pre_process(parameter)
    clear_results(job_name)
    # post_process(job_name, "PHILSM")


