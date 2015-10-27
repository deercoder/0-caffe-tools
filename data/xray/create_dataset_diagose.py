#!/usr/bin/env python
import sys
import os
import shutil

PATH = '/home/ycao/cli/xray_images/'

#src = ['LI', 'GH','CA', 'MI', 'AI', 'OT']
#src_file_list = ['LI.list', 'GH.list', 'CA.list', 'MI.list', 'AI.list', 'OT.list']
#label_file = ['xray_diagnose_train.txt', 'xray_diagnose_test.txt']
#label_tag = [0, 1, 2, 3, 4, 5]

## Now we don't use MI and GH since it has so small dataset of images.
src = ['LI', 'CA', 'AI', 'OT']
src_file_list = ['LI.list', 'CA.list', 'AI.list', 'OT.list']
label_file = ['xray_diagnose_train.txt', 'xray_diagnose_test.txt']
label_tag = [0, 1, 2, 3]

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

		train_handler = open(label_file[0], "a+")
		test_handler = open(label_file[1], "a+")

		count = 0

		# use the filelist to generate, we are sure that file exist in this folder
		# so no judge for existance of the file
		for line in file_handler:
			file_name = PATH + line[1:-2]
		 	shutil.copy(file_name, './' + str(src[index]))
	
			if count % 5 == 0:
				test_handler.write(file_name + ' ' + str(tag) + '\n')
			else:
				train_handler.write(file_name + ' ' + str(tag) + '\n')
			count += 1
				
		file_handler.close()
		test_handler.close()
		train_handler.close()

if __name__ == "__main__":
	create_dataset(src, src_file_list)	
