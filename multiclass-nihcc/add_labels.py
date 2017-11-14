#!/usr/bin/env python
import glob
import os 
import shutil

classes = ['Atelectasis', 'Cardiomegaly', 'Effusion',
                'Infiltration', 'Mass', 'Nodule',
                'Pneumonia', 'Pneumothorax', 'Consolidation',
                'Edema', 'Emphysema', 'Fibrosis',
                'Pleural_Thickening',  'Hernia']

# these two splits are the shared train/val files

for c in classes:
	# these two files are for each class, it has XXX_train, XXX_val.txt file
	train_label = open(c + "_train.txt", "w")
	val_label = open(c + "_val.txt", "w")
	
	trainfiles = open("train.txt", "r")
	valfiles = open("val.txt", "r")

	# now that we construct each XXX_train, XXX_val.txt file
	# first look up the file in each category
	seperatefiles = open("./split_txt/" + c +".txt", "r")
	lists = seperatefiles.readlines()
	#print lists
	print c
	for t in trainfiles:
		try:
			index = lists.index(t)
			index = 1
			#print index
		except:
			index = -1
		train_label.write(t[:-1] + " " + str(index) + "\n")
	train_label.close()
		
	for t in valfiles:
		try:
			index = lists.index(t)
			index = 1
		except:
			index = -1
		#print index
		val_label.write(t[:-1] + " " + str(index) + "\n")
	val_label.close()
	seperatefiles.close()

trainfiles.close()
valfiles.close()
