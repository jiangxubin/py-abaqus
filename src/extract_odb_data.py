# -*- coding: mbcs -*-
from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
import csv


odb_base_path = r'C:/Users/augustus/OneDrive - jiangxubin/model/excavation'
csv_base_path = r"C:/Users/augustus/OneDrive - jiangxubin/model/base"

def extract_frame_data(frame, target_set):
	frame = odb.steps['injection'].frames[frame]
	# print(frame.frameValue)
	variable_data = frame.fieldOutputs['PORPRES']
	target_data = variable_data.getSubset(region=target_set)
	label = [item.elementLabel for item in target_data.values]
	value = [item.data for item in target_data.values]
	print(label)
	print(value)
	return label, value, frame.frameValue 
	# session.viewports['Viewport: 1'].setValues(displayedObject=ob)
	# session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(variableLabel='PFOPENXFEMCOMP1', outputPosition=WHOLE_ELEMENT, )
	# session.viewports[session.currentViewportName].odbDisplay.setFrame(step='injection', frame=frame)
	


if __name__ == "__main__":
	for i in range(1,7):
		odb_path = r'C:/Users/augustus/OneDrive - jiangxubin/model/excavation/Job-test-excavation-{}-1.odb'.format(i)
		csv_fw = open(r"C:/Users/augustus/OneDrive - jiangxubin/model/base/porpresa-{}.csv".format(i), "w")
		csv_writer = csv.writer(csv_fw, delimiter= ',', lineterminator='\n')
		odb = session.openOdb(name=odb_path)
		element_labels = (16, 47, 78, 109, 140, 171, 202, 233, 264, 295)
		target_set = odb.rootAssembly.instances['SOIL-1'].ElementSetFromElementLabels(name="target_set", elementLabels=(element_labels))
		# label, value = extract_frame_data(94, target_set)
		for index in list(range(1, 101)):
			try:
				label, data, i_t = extract_frame_data(index, target_set)
				max_data = max(data)
				csv_writer.writerow([i_t, max_data])
			except IndexError:
				break
		csv_fw.close()
		odb.close()

