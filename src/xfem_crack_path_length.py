# -*- coding: mbcs -*-
from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
import csv


odb_base_path = r'C:/Users/augustus/OneDrive - jiangxubin/model/standard/Job-test-3-5.odb'
csv_base_path = r"C:/Users/augustus/OneDrive - jiangxubin/model/base/canadian/permeability"




def delta_distance(coordinate_1, coordinate_2):
	dist = sqrt((coordinate_1[0]-coordinate_2[0])**2+(coordinate_1[1]-coordinate_2[1])**2)
	return dist

def extract_frame_data(step, frame_index, target_set):
	frame = odb.steps[step].frames[frame_index]
	variable_data = frame.fieldOutputs['COORD']
	target_data = variable_data.getSubset(region=target_set)
	totoal_length = 0
	former_coordinates = [0,0]
	# csv_fw = open(r"C:/Users/augustus/OneDrive - jiangxubin/model/base/length/sparse_step_{}frame_{}.csv".format(step, frame_index), "w")
	# for index, item in enumerate(target_data.values):
	# 	if index%4==1:
	# 		csv_writer = csv.writer(csv_fw, delimiter= ',', lineterminator='\n')
	# 		csv_writer.writerow([item.nodeLabel, item.data])
	# csv_fw.close()
	for index, item in enumerate(target_data.values):
		if index%4==1:
			delta = delta_distance(item.data, former_coordinates)
			totoal_length += delta
		former_coordinates = item.data
	print("Crakc length at step{}frame{} is {}".format(step, frame_index, totoal_length))

if __name__ == "__main__":
	odb = session.openOdb(name=odb_base_path)
	steps =['Initial', 'geo', 'injection', 'injection-2']
	# xfem_node = odb.rootAssembly.nodeSets['addedNX_XFEM+001ASSEMBLY_SOIL-1_SOIL'].nodes[0]
	# xfem_node_labels = [item.label for item in xfem_node]
	for surface in odb.rootAssembly.surfaces.keys():
		frame = int(surface.split()[-1])
		step = int(surface.split()[-3])
		step_surface = odb.rootAssembly.surfaces[surface]
		node_set = step_surface.nodes[0]
		node_label_set = [node.label for node in node_set]
		target_set = odb.rootAssembly.instances['SOIL-1'].NodeSetFromNodeLabels(name='xfem_node_set_{}_{}'.format(step, frame),nodeLabels=node_label_set)
		extract_frame_data(steps[step], frame, target_set)
	odb.close()