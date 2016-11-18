#!/usr/bin/env python
import random
import sys
import os
import shutil

PATH = '/data1/dataset/xray/xray_images/'
n = 4248
all_set = [453, 4248]

src = ['normal', 'abnormal']
src_file_list = ['normal.list', 'abnormal.list']
label_file = ['x1.txt', 'x2.txt', 'x3.txt', 'x4.txt', 'x5.txt']
label_tag = [0, 1]

# create a folder that contains the images for training and testing
# generate the label text files
def create_dataset(src, src_file_list):

	# generate the folder that contains for different labels 	
	for list_src in src:
		absolute_path = './' + list_src
		if not os.path.exists(absolute_path):
			os.mkdir(absolute_path)

	# open the file that contains the lists
	for file in src_file_list:
		file_handler = open(file, "r+")
		index = src_file_list.index(file)
		tag = label_tag[index]

		x1_handler = open(label_file[0], "a+")
		x2_handler = open(label_file[1], "a+")
		x3_handler = open(label_file[2], "a+")
		x4_handler = open(label_file[3], "a+")
		x5_handler = open(label_file[4], "a+")

		test = file_handler.readlines()
		print test
		
		a = random.sample(range(n), n)
		a = [x % all_set[index] for x in a ]
		print a
		count = 0

		# use the filelist to generate, we are sure that file exist in this folder
		# so no judge for existance of the file
		for item in a:
			tmp = test[item]
			file_name = PATH + tmp[1:-2]
				
			if count % 5 == 0:
				x1_handler.write(file_name + ' ' + str(tag) + '\n')
			elif count % 5 == 1:
				x2_handler.write(file_name + ' ' + str(tag) + '\n')
			elif count % 5 == 2:
				x3_handler.write(file_name + ' ' + str(tag) + '\n')
			elif count % 5 == 3:
				x4_handler.write(file_name + ' ' + str(tag) + '\n')
			elif count % 5 == 4:
				x5_handler.write(file_name + ' ' + str(tag) + '\n')
			count += 1

		file_handler.close()
		x1_handler.close()
		x2_handler.close()
		x3_handler.close()
		x4_handler.close()
		x5_handler.close()

if __name__ == "__main__":
	create_dataset(src, src_file_list)	
