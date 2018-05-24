import numpy as np
import matplotlib.pyplot as plt

# Make sure that caffe is on the python path:
caffe_root = '../../..'  # this file is expected to be in {caffe_root}/examples
import sys
sys.path.insert(0, caffe_root + 'python')

import caffe

# Set the right path to your model definition file, pretrained model weights,
# and the image you would like to classify.
MODEL_FILE = 'GoogleNet_cub_2011_4_deploy.prototxt'
PRETRAINED = 'GoogleNet_cub_2011_4_iter_800000.caffemodel'
IMAGE_FILE = '/data3/users/roy/iMaterials-all/test/'

caffe.set_mode_cpu()
caffe.set_device(1)
net = caffe.Classifier(MODEL_FILE, PRETRAINED,
                       mean= None,
                       channel_swap=(2,1,0),
                       raw_scale=255,
                       image_dims=(226, 226))


file = "submission.csv"
file_handler = open(file, "w+") 

file_handler.write("id\tpredicted\n")

for i in range(12800):
	input_image = caffe.io.load_image(IMAGE_FILE + str(i+1) + ".jpg") 
	prediction = net.predict([input_image])  # predict takes any number of images, and formats them for the Caffe net automatically
	#print 'prediction shape:', prediction[0].shape
	label = prediction[0].argmax()
	print 'predicted class:', label+1
	file_handler.write(str(i+1) + "\t" + str(label+1) + "\n")

file_handler.close()
