#!/usr/bin/env python
"""
* This program is used for cutting the raw images using the bounding-box label
which is a 4-dimension tuple (x_left, x_up, x_right, x_down)

* Author: Chang Liu
"""
import Image
import os

src_folder = '/home/ycao/cliu2/caffe/data/test/UECFOOD256/'

dst_folder = '/home/ycao/cliu2/caffe/data/test/cropped_UEC/'

# try build the dst folder to store the cropped images with bounding-box
if not os.path.exists(dst_folder):
	os.makedirs(dst_folder)

# crop the images as the training dataset
for i in range(1, 256+1):

	# read file from bb_info.txt under the folders(bounding-box)
	bb_info = src_folder + str(i) + "/bb_info.txt"
	file_bb_handler = open(bb_info)
	
	# create new sub folders to store the cropped images
	sub_folder = dst_folder + str(i)
	if not os.path.exists(sub_folder):
		os.makedirs(sub_folder)
	
	# for each item in bb_info, get the file name and bb_box
	for line in file_bb_handler:
		# get item in the bb_info
		name, xleft, xup, xright, xdown = line.split()
		file_name = src_folder + str(i) + "/" + str(name) + ".jpg"
		
		# for non-exist item, print error
		if not os.path.exists(file_name):
			print "Not exist this file", file_name
		# otherwise, crop and save it
		else:
			src = Image.open(file_name)
			left = int(xleft)
			up = int(xup)
			right = int(xright)
			down = int(xdown)
			frame = src.crop((left, up, right, down))
			frame.save(sub_folder+"/"+str(name)+"_crop.jpg")
			src.close()
		print name, xleft, xup, xright, xdown
	file_bb_handler.close()
