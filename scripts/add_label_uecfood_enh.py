#!/usr/bin/python

#fileHandler = open('train.txt')
fileHandler = open('train.txt')
fileNewHandler = open('new_train.txt', 'w')

fileList = fileHandler.readlines()
prefix_path = "/home/ycao/cliu2/foodcam.mobi/"

for i in range(0, len(fileList)):
	for j in range(0, 100):
		type = "UECFOOD100/" + str(j+1) + "/" # should add '/' to close it, and label is j but actual is j+1
		if fileList[i].find(type) != -1:
			new_str = fileList[i]
			length = len(fileList[i])
			new_str = new_str[0:length-1] + " " # add blank after file name
			new_str = prefix_path + new_str + str(j) # add label
			new_str = new_str + "\n"
			fileNewHandler.write(new_str)
			print new_str

fileHandler.close()
fileNewHandler.close()
