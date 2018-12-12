# -*- coding: mbcs -*-
#
from abaqus import *
from abaqusConstants import *
from abaqus import session
import displayGroupOdbToolset as dgo

job_name = 'D:/thesis/mini-thesis/centrifuge/Centrifuge-2018-11-29-21-27.odb'

odb = session.openOdb(name=job_name)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='injection', frame=100)


leaf = dgo.LeafFromNodeSets(nodeSets=('addedNX_XFEM+001ASSEMBLY_SOIL-1_SOIL', 
    ))


# leaf = dgo.LeafFromNodeSets(nodeSets=('ALL NODES', 
#     ))

vp = session.viewports[session.currentViewportName]

dg = session.DisplayGroup(name='xfem_nodes', leaf=leaf)
vp.odbDisplay.setValues(visibleDisplayGroups=(dg, ))

node_dg = vp.odbDisplay.displayGroupInstances['xfem_nodes']

nodes = node_dg.nodes()
for key in list(nodes.keys()):
	print("key:{}, length:{}".format(key, len(nodes[key])))
