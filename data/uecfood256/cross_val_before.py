#!/usr/bin/env python
src = ["val0.txt", "val1.txt", "val2.txt", "val3.txt", "val4.txt"]
train_dst = ["uec_train_cv_1.txt", "uec_train_cv_2.txt","uec_train_cv_3.txt","uec_train_cv_4.txt","uec_train_cv_5.txt"]
test_dst = ["uec_test_cv_1.txt","uec_test_cv_2.txt","uec_test_cv_3.txt","uec_test_cv_4.txt","uec_test_cv_5.txt"]

src_handler = []
train_handler = []
test_handler = []

PATH = "/data3/users/cliu2/caffe/data/test/"

# open files for writing
for i in src:
	tmp = open(i, "r+")
	src_handler.append(tmp)

for i in range(0, 5):
	tmp = open(train_dst[i], "a+")
	train_handler.append(tmp)
	tmp = open(test_dst[i], "a+")
	test_handler.append(tmp)


# write files(ther is a bug here, whyy????
for i in range(0, 5):
	print "aaaa", i
	src_handler[i].seek(0)
	for file in src_handler[i]:
		test_handler[i].write(PATH+file)
	for j in range(0,5):
		if j != i:
			src_handler[j].seek(0)
			for file in src_handler[j]:
				train_handler[i].write(PATH+file)

# close files
for i in src_handler:
	i.close()	

for i in range(0, 5):
	train_handler[i].close()
	test_handler[i].close()
