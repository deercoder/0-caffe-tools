#!/usr/bin/env python
import glob
import os 
import shutil

classes = ['Atelectasis', 'Cardiomegaly', 'Effusion',
                'Infiltration', 'Mass', 'Nodule',
                'Pneumonia', 'Pneumothorax', 'Consolidation',
                'Edema', 'Emphysema', 'Fibrosis',
                'Pleural_Thickening',  'Hernia']

for c in classes:
	files = glob.glob("./" + c + "/*.png")
	for f in files:
		filename = f.split('/')[-1]
		try:
			shutil.move(f, "./images/"+filename)
		except Exception:
    			continue
