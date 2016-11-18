#!/usr/bin/env python
import os

src_file = ['x1.txt', 'x2.txt', 'x3.txt', 'x4.txt', 'x5.txt']
train_file = ['train1.txt', 'train2.txt', 'train3.txt', 'train4.txt', 'train5.txt']
test_file = ['test1.txt', 'test2.txt', 'test3.txt', 'test4.txt', 'test5.txt']


for i in range(5):
	train_handler = open(train_file[i], "a+")
	test_handler = open(test_file[i], "a+")
	for j in range(5):
		handler = open(src_file[j], "r+")
		if i != j:
			for item in handler:
				train_handler.write(item)
		elif i == j:
			for item in handler:
				test_handler.write(item)			
		handler.close()
	train_handler.close()
	test_handler.close()
