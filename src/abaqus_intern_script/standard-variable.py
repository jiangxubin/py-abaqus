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



top_vertical_limit = 31.0
bottom_vertical_limit = 0.0
right_horizon_limit = 15.5
left_horizon_limit = -right_horizon_limit
crack_top_vertical_limit = 1.0
crack_bottom_vertical_limit = 0.0
crack_horizon_limit = 0.0




    mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
    mdb.models['Model-1'].sketches['__profile__'].Spot(point=(right_horizon_limit, top_vertical_limit))
    mdb.models['Model-1'].sketches['__profile__'].Spot(point=(-right_horizon_limit, 0.0))
    mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-right_horizon_limit, 0.0), 
        point2=(right_horizon_limit, top_vertical_limit))
    mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='soil', type=
        DEFORMABLE_BODY)
    mdb.models['Model-1'].parts['soil'].BaseShell(sketch=
        mdb.models['Model-1'].sketches['__profile__'])
    del mdb.models['Model-1'].sketches['__profile__']
    mdb.models['Model-1'].parts['soil'].Set(faces=
        mdb.models['Model-1'].parts['soil'].faces.findAt(((0.0, top_vertical_limit/2, 
        0.0), )), name='soil')
    mdb.models['Model-1'].parts['soil'].Set(edges=
        mdb.models['Model-1'].parts['soil'].edges.findAt(((-right_horizon_limit, top_vertical_limit/2, 0.0), )), 
        name='left')
    mdb.models['Model-1'].parts['soil'].Set(edges=
        mdb.models['Model-1'].parts['soil'].edges.findAt(((right_horizon_limit, top_vertical_limit/2, 0.0), )), 
        name='right')
    mdb.models['Model-1'].parts['soil'].Set(edges=
        mdb.models['Model-1'].parts['soil'].edges.findAt((((right_horizon_limit+left_horizon_limit)/2, bottom_vertical_limit, 0.0), )), 
        name='bottom')
    mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
    mdb.models['Model-1'].sketches['__profile__'].Spot(point=(crack_horizon_limit, crack_bottom_vertical_limit))
    mdb.models['Model-1'].sketches['__profile__'].Spot(point=(crack_horizon_limit, crack_top_vertical_limit))
    mdb.models['Model-1'].sketches['__profile__'].Line(point1=(crack_horizon_limit, crack_top_vertical_limit), point2=(
        crack_horizon_limit, crack_bottom_vertical_limit))
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 0.5))
    mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
        False, entity=
        mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 0.5), 
        ))
    mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='crack', type=
        DEFORMABLE_BODY)
    mdb.models['Model-1'].parts['crack'].BaseWire(sketch=
        mdb.models['Model-1'].sketches['__profile__'])
    del mdb.models['Model-1'].sketches['__profile__']
    mdb.models['Model-1'].parts['crack'].Set(edges=
        mdb.models['Model-1'].parts['crack'].edges.findAt(((0.0, 0.75, 0.0), )), 
        name='crack')
    mdb.models['Model-1'].Material(name='soil')
    mdb.models['Model-1'].materials['soil'].Density(table=((1500.0, ), ))
    mdb.models['Model-1'].materials['soil'].Elastic(table=((5000000.0, 0.4), ))
    mdb.models['Model-1'].materials['soil'].MaxpsDamageInitiation(position=CRACKTIP
        , table=((30000.0, ), ), tolerance=0.1)
    mdb.models['Model-1'].materials['soil'].maxpsDamageInitiation.DamageEvolution(
        mixedModeBehavior=POWER_LAW, power=1.0, table=((10000.0, 10000.0, 10000.0), 
        ), type=ENERGY)
    mdb.models['Model-1'].materials['soil'].maxpsDamageInitiation.DamageStabilizationCohesive(
        cohesiveCoeff=1e-05)
    mdb.models['Model-1'].materials['soil'].GapFlow(table=((1e-06, ), ))
    mdb.models['Model-1'].materials['soil'].FluidLeakoff(table=((5.879e-16, 
        5.879e-16), ))
    mdb.models['Model-1'].materials['soil'].Permeability(inertialDragCoefficient=
        0.142887, specificWeight=10000.0, table=((2.618e-06, 2.618e-06), ))
    mdb.models['Model-1'].HomogeneousSolidSection(material='soil', name='soil', 
        thickness=None)
    mdb.models['Model-1'].parts['soil'].SectionAssignment(offset=0.0, offsetField=
        '', offsetType=MIDDLE_SURFACE, region=
        mdb.models['Model-1'].parts['soil'].sets['soil'], sectionName='soil', 
        thicknessAssignment=FROM_SECTION)
    mdb.models['Model-1'].parts['soil'].seedPart(deviationFactor=0.1, 
        minSizeFactor=0.1, size=1.0)
    mdb.models['Model-1'].parts['soil'].setMeshControls(algorithm=MEDIAL_AXIS, 
        elemShape=QUAD, regions=mdb.models['Model-1'].parts['soil'].faces.findAt(((
        -5.166667, 10.333333, 0.0), )))
    mdb.models['Model-1'].parts['soil'].setElementType(elemTypes=(ElemType(
        elemCode=CPE4P, elemLibrary=STANDARD), ElemType(elemCode=UNKNOWN_TRI, 
        elemLibrary=STANDARD)), regions=(
        mdb.models['Model-1'].parts['soil'].faces.findAt(((-5.166667, 10.333333, 
        0.0), )), ))
    mdb.models['Model-1'].parts['soil'].generateMesh()
    mdb.models['Model-1'].parts['soil'].Set(name='nall', nodes=
        mdb.models['Model-1'].parts['soil'].nodes[0:1024])
    mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
    mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='crack-1', part=
        mdb.models['Model-1'].parts['crack'])
    mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='soil-1', part=
        mdb.models['Model-1'].parts['soil'])
    mdb.models['Model-1'].GeostaticStep(name='geo', previous='Initial')
    mdb.models['Model-1'].SoilsStep(cetol=None, creep=OFF, end=None, initialInc=1.0
        , maxInc=1.0, minInc=1e-12, name='injection', previous='geo', timePeriod=
        1.0, utol=1000000000.0, nlgeom=ON)
    mdb.models['Model-1'].TabularAmplitude(data=((25.0, -50.0), (50.0, -75.0), (
        100.0, -100.0)), name='volumerate', smooth=SOLVER_DEFAULT, timeSpan=STEP)
    mdb.models['Model-1'].FieldOutputRequest(name='F-Output-1', createStepName='geo')
    mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
        'S', 'LE', 'U', 'RF', 'CF', 'CSTRESS', 'CDISP', 'PHILSM', 'PSILSM', 
        'VOIDR', 'SAT', 'POR'))
    mdb.models['Model-1'].HistoryOutputRequest(name='H-Output-1', createStepName='geo')
    mdb.models['Model-1'].rootAssembly.engineeringFeatures.XFEMCrack(crackDomain=
        mdb.models['Model-1'].rootAssembly.instances['soil-1'].sets['soil'], 
        crackLocation=
        mdb.models['Model-1'].rootAssembly.instances['crack-1'].sets['crack'], 
        name='Crack-1')
    mdb.models['Model-1'].Gravity(comp2=-10.0, createStepName='geo', 
        distributionType=UNIFORM, field='', name='gravity')
    mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
        distributionType=UNIFORM, fieldName='', localCsys=None, name='left', 
        region=mdb.models['Model-1'].rootAssembly.instances['soil-1'].sets['left'], 
        u1=SET, u2=UNSET, ur3=UNSET)
    mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
        distributionType=UNIFORM, fieldName='', localCsys=None, name='right', 
        region=mdb.models['Model-1'].rootAssembly.instances['soil-1'].sets['right']
        , u1=SET, u2=UNSET, ur3=UNSET)
    mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
        distributionType=UNIFORM, fieldName='', localCsys=None, name='bottom', 
        region=
        mdb.models['Model-1'].rootAssembly.instances['soil-1'].sets['bottom'], u1=
        UNSET, u2=SET, ur3=UNSET)
    mdb.models['Model-1'].ExpressionField(description='', expression='31 -  Y ', 
        localCsys=None, name='AnalyticalField-1')
    mdb.models['Model-1'].PorePressureBC(amplitude=UNSET, createStepName='geo', 
        distributionType=FIELD, fieldName='AnalyticalField-1', fixed=OFF, 
        magnitude=10000.0, name='left-pore', region=
        mdb.models['Model-1'].rootAssembly.instances['soil-1'].sets['left'])
    mdb.models['Model-1'].PorePressureBC(amplitude=UNSET, createStepName='geo', 
        distributionType=FIELD, fieldName='AnalyticalField-1', fixed=OFF, 
        magnitude=10000.0, name='right-pore', region=
        mdb.models['Model-1'].rootAssembly.instances['soil-1'].sets['right'])
    mdb.models['Model-1'].GeostaticStress(lateralCoeff1=0.6, lateralCoeff2=None, 
        name='geo', region=
        mdb.models['Model-1'].rootAssembly.instances['soil-1'].sets['soil'], 
        stressMag1=0.0, stressMag2=-310000.0, vCoord1=top_vertical_limit, vCoord2=0.0)
    mdb.models['Model-1'].VoidsRatio(distributionType=UNIFORM, name='void', region=
        mdb.models['Model-1'].rootAssembly.instances['soil-1'].sets['nall'], 
        variation=CONSTANT_RATIO, voidsRatio1=1.0)
    mdb.models['Model-1'].PorePressure(distributionType=FIELD, field=
        'AnalyticalField-1', name='pore', porePressure1=10000.0, region=
        mdb.models['Model-1'].rootAssembly.instances['soil-1'].sets['nall'], 
        variation=CONSTANT_RATIO)
    soil_elements = mdb.models['Model-1'].rootAssembly.instances['soil-1'].elements
    soil_elements_set = mdb.models['Model-1'].rootAssembly.Set(name='eall', elements=soil_elements)
    mdb.models['Model-1'].steps['injection'].control.setValues(allowPropagation=OFF
        , resetDefaultValues=OFF, timeIncrementation=(4.0, 8.0, 9.0, 16.0, 10.0, 
        4.0, 20.0, 5.0, 6.0, 3.0, 50.0))
    mdb.models['Model-1'].materials['soil'].permeability.setValues(
        inertialDragCoefficient=0.142887, specificWeight=10000.0, table=((
        2.618e-06, 0.0), ))
    mdb.models['Model-1'].predefinedFields['geo'].suppress()
    mdb.models['Model-1'].steps['geo'].setValues(maxInc=1.0, minInc=1e-05, 
        timeIncrementationMethod=AUTOMATIC, utol=0.1)
    mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
        explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
        memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, 
        multiprocessingMode=DEFAULT, name='Job-test', nodalOutputPrecision=SINGLE, 
        numCpus=1, numGPUs=0, queue=None, resultsFormat=ODB, scratch='', type=
        ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
