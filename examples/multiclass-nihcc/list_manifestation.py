#!/usr/bin/env python
import glob

classes = ['No', 'Atelectasis', 'Cardiomegaly', 'Effusion',
                'Infiltration', 'Mass', 'Nodule',
                'Pneumonia', 'Pneumothorax', 'Consolidation',
                'Edema', 'Emphysema', 'Fibrosis',
                'Pleural_Thickening',  'Hernia']

for c in classes:
	files = glob.glob("./" + c + "/*.png")
	save_file = open("./" + c + ".txt", "w+")	
	for f in files:
		file_name_index = f.split('/')[-1][:-4]
		save_file.write(file_name_index + "\n")
	save_file.close()
