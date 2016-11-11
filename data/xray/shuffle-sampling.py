#!/usr/bin/env python
import random
import sys
import os
import shutil

PATH = '/data1/dataset/xray/xray_images/'
n = 2252
all_set = [1182, 560, 202, 2252]
all_name = ['CA', 'OT', 'LI', 'AI']

src_file_list = ['CA.list', 'OT.list', 'LI.list', 'AI.list']
label_file = ['xray_train.txt', 'xray_test.txt']
label_tag = [0, 1, 2, 3]


def create_dataset(src, src_file_list):
	# generate the folder that contains for different labels 	
	for list_src in src:
		absolute_path = './' + list_src
		if not os.path.exists(absolute_path):
			os.mkdir(absolute_path)
	
	for file in src_file_list:
		file_handler = open(file, "r+")
		index = src_file_list.index(file)
		tag = label_tag[index]

		train_handler = open(label_file[0], "a+")
		test_handler = open(label_file[1], "a+")

		test = file_handler.readlines() 
		print test
	
		a = random.sample(range(n), n)
		a = [x % all_set[index] for x in a ]
		print a
		
		count = 0

		for item in a:
			tmp = test[item]
			file_name = PATH + tmp[1:-2]
			
			if count % 5 == 0:
				test_handler.write(file_name + ' ' + str(tag) + '\n')
			else:
				train_handler.write(file_name + ' ' + str(tag) + '\n')
			count += 1

		file_handler.close()
		test_handler.close()
		train_handler.close()
			

if __name__ == "__main__":
	create_dataset(all_name, src_file_list)
