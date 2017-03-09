#!/usr/bin/env python
from os import listdir
from os.path import isfile, join
from shutil import copyfile


UEC_PATH = "../UECFOOD100"
IMG_FOLDER = "./Images"

for i in range(1, 2):
	path = UEC_PATH + "/" + str(i) 
	#onlyfiles = [f for f in listdir(path) if isfile(join(mypath, f))]
	#imgfiles = [f for f in onlyfiles if f.endswith(".jpg") OR f.endswith(".JPG")]
	bb_file = path + "/" + "bb_info.txt"
	f = open(bb_file, "r")
	a = f.readlines()
	print a
	j = 0
	for line in a:
		print "***********"
		if j != 0:
			lists = line.split(" ")	
			filename = lists[0] + ".txt"
			copyfile(path + "/" + lists[0] + ".jpg", IMG_FOLDER + "/" + lists[0] + ".jpg")
			print filename
			ant = open(filename, "w")
			ant.write(str(i-1) + " " + lists[1] + " " + lists[2] + " " + lists[3] + " "+ lists[4])
			ant.close()
		j = j + 1
	f.close()

