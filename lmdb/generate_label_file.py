#!/usr/bin/env python
import glob

PATH = '/data0/dataset/nihcc-train/tf-data'

src = ['normal', 'abnormal']
src_file_list = ['normal.list', 'abnormal.list']
manifestations = [
    'Atelectasis',
    'Cardiomegaly',
    'Effusion',
    'Infiltration',
    'Mass',
    'Nodule',
    'Pneumonia',
    'Pneumothorax',
    'Consolidation',
    'Edema',
    'Emphysema', 
    'Fibrosis',
    'Pleural_Thickening',
    'Hernia',
]

label_file = ['nihcc_train.txt', 'nihcc_test.txt']

def create_train_label_files():
	base_dir = PATH + "/train"
	index = 0
	f = open(label_file[0], "w+")
	for item in manifestations:
		class_dir = base_dir + "/" + item
		files = glob.glob(class_dir + "/*.png")
		for file in files:
			print file
			f.write(file + ' ' + str(index) + '\n')
		index += 1

	f.close()
	
def create_test_label_files():
	base_dir = PATH + "/test"
	index = 0
	f = open(label_file[1], "w+")
	for item in manifestations:
		class_dir = base_dir + "/" + item
		files = glob.glob(class_dir + "/*.png")
		for file in files:
			print file
			f.write(file + ' ' + str(index) + '\n')
		index += 1

	f.close()

if __name__ == "__main__":
	create_train_label_files()
	create_test_label_files()
