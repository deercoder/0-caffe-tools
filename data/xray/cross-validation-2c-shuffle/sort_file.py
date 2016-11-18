#!/usr/bin/env python
import os

train_file = ['train1.txt', 'train2.txt', 'train3.txt', 'train4.txt', 'train5.txt']
test_file = ['test1.txt', 'test2.txt', 'test3.txt', 'test4.txt', 'test5.txt']

for item in train_file:
	os.system('sort -R ' + item + ' > tmp.txt ')
	os.system('sort -R tmp.txt  > tmp2.txt ')
	os.system('sort -R tmp2.txt >' + item)

for item in test_file:
	os.system('sort -R ' + item + ' > tmp.txt ')
	os.system('sort -R tmp.txt  > tmp2.txt ')
	os.system('sort -R tmp2.txt >' + item)
