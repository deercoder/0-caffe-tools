#!/usr/bin/python

fileHandler = open('train.txt')
fileNewHandler = open('new_train.txt', 'w')

fileList = fileHandler.readlines()

type = [ 'n07639069', 'n07663899', 'n07697537', 'n07698672', 'n07730207', 'n07739125', 'n07747607', 'n07753592', 'n07873807' ] 

label = ['0', '1', '2', '3', '4', '5', '6','7', '8']

for i in range(0, len(fileList)):
	for j in range(0, 9):
		if fileList[i].find(type[j]) != -1:
			new_str = fileList[i]
			length = len(fileList[i])
			new_str = new_str[0:length-1] + " "
			new_str = new_str + label[j] 	
			new_str = new_str + "\n"
			fileNewHandler.write(new_str)
			print new_str

fileHandler.close()
fileNewHandler.close()
