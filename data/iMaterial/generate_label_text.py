#!/usr/bin/env python
import glob

DIR = ["train01", "val"]


for item in DIR:
	handler = open(item+".txt", "w")
	for i in range(128):
		path = item + "/" + str(i) + "/"
		filelists = glob.glob(path+"*.jpeg")
		for file in filelists:
			print file
			handler.write(file + " " + str(i) + "\n")
	handler.close()
