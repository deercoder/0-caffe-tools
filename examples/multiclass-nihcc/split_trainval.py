#!/usr/bin/env python
import glob
import os 
import shutil

classes = ['Atelectasis', 'Cardiomegaly', 'Effusion',
                'Infiltration', 'Mass', 'Nodule',
                'Pneumonia', 'Pneumothorax', 'Consolidation',
                'Edema', 'Emphysema', 'Fibrosis',
                'Pleural_Thickening',  'Hernia']

total_f = open("total.txt", "r+")
train_f = open("train.txt", "w+")
val_f = open("val.txt", "w+")
i = 0

for item in total_f:
	if i % 5 == 0:
		val_f.write(item[:-5] + "\n")
	else:
		train_f.write(item[:-5] + "\n")
		
	i = i + 1

train_f.close()
val_f.close()
