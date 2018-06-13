#!/usr/bin/env python
import glob
import os 
import shutil


def write_obj(f, name):
	f.write("\t<object>\n")
	f.write("\t\t<name>" + name + "</name>\n")
	f.write("\t\t<bndbox>\n")
	f.write("\t\t\t<xmax>1024</xmax>\n")
	f.write("\t\t\t<xmin>1</xmin>\n")
	f.write("\t\t\t<ymax>1024</ymax>\n")
	f.write("\t\t\t<ymin>1</ymin>\n")
	f.write("\t\t</bndbox>\n")
	f.write("\t</object>\n")

classes = ['Atelectasis', 'Cardiomegaly', 'Effusion',
                'Infiltration', 'Mass', 'Nodule',
                'Pneumonia', 'Pneumothorax', 'Consolidation',
                'Edema', 'Emphysema', 'Fibrosis',
                'Pleural_Thickening',  'Hernia']

# these two splits are the shared train/val files
trainfiles = open("train.txt", "r")
valfiles = open("val.txt", "r")

for item in trainfiles:
	f = open(item[:-1] + ".xml", "w")
	f.write("<annotation>\n")
	f.write("\t<filename>" + item[:-1] + ".png" + "</filename>\n")
	for c in classes:
		seperatefiles = open("./split_txt/" + c +".txt", "r")
		lists = seperatefiles.readlines()
		try:
			index = lists.index(item)
			write_obj(f, c)
		except:
			## not in the class
			pass
		seperatefiles.close()
	f.write("</annotation>\n")
	f.close()

for item in valfiles:
	f = open(item[:-1] + ".xml", "w")
	f.write("<annotation>\n")
	f.write("\t<filename>" + item[:-1] + ".png" + "</filename>\n")
	for c in classes:
		seperatefiles = open("./split_txt/" + c +".txt", "r")
		lists = seperatefiles.readlines()
		try:
			index = lists.index(item)
			write_obj(f, c)
		except:
			## not in the class
			pass
		seperatefiles.close()
	f.write("</annotation>\n")
	f.close()
