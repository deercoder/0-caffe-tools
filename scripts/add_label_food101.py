#!/usr/bin/python
"""
Author: Chang Liu (chang_liu@student.uml.edu)

Description: This script is used for generating the label files for Caffe to train CNN models
	     Here we would like to use Food-101 dataset, using the ROOT/meta/train.txt to
	     generate our desired format so that Caffe can recognize it.
"""
#fileHandler = open('train.txt')
fileHandler = open('test.txt')
fileNewHandler = open('new_test.txt', 'w')

fileList = fileHandler.readlines()
prefix_path = "/data1/dataset/food-101/images/"

# fetch the label from the classes.txt, that contains folder name
labels = []
label_handler = open("classes.txt", "r+")
label_lines = label_handler.readlines()
for i in label_lines:
	labels.append(i[:-1])
print labels

# now use the train.txt to generate our label files in format
for line in fileList:
	for j in labels:
		type = j + "/" # match pattern
		index = labels.index(j)
		if line.find(type) != -1: # find the label in predefined
			new_str = prefix_path + line[:-1] + ".jpg " + str(index) + "\n"
			fileNewHandler.write(new_str)
			print new_str

fileHandler.close()
fileNewHandler.close()
