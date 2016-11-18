#!/usr/bin/env python
from sklearn.metrics import classification_report
import numpy as np
import sys
import caffe
import os

caffe_root = './'  # this file should be run from {caffe_root}/examples (otherwise change this line)
sys.path.insert(0, caffe_root + 'python')


if os.path.isfile('/home/cliu/github/caffe/models/finetune-xray-alexnet-shuffle/finetune_alexNet_xray_iter_100000.caffemodel'):
    print 'CaffeNet found.'
else:
    print 'Not found!'

caffe.set_device(3)
caffe.set_mode_gpu()

model_def = caffe_root + 'models/finetune-xray-alexnet-shuffle/deploy.prototxt'
model_weights = '/home/cliu/github/caffe/models/finetune-xray-alexnet-shuffle/finetune_alexNet_xray_iter_100000.caffemodel'

net = caffe.Net(model_def,      # defines the structure of the model
                model_weights,  # contains the trained weights
                caffe.TEST)     # use test mode (e.g., don't perform dropout)


# load the mean ImageNet image (as distributed with Caffe) for subtraction
mu = np.load(caffe_root + 'python/caffe/imagenet/ilsvrc_2012_mean.npy')
mu = mu.mean(1).mean(1)  # average over pixels to obtain the mean (BGR) pixel values
print 'mean-subtracted values:', zip('BGR', mu)

# create transformer for the input called 'data'
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})

transformer.set_transpose('data', (2,0,1))  # move image channels to outermost dimension
transformer.set_mean('data', mu)            # subtract the dataset-mean value in each channel
transformer.set_raw_scale('data', 255)      # rescale from [0, 1] to [0, 255]
transformer.set_channel_swap('data', (2,1,0))  # swap channels from RGB to BGR


# set the size of the input (we can skip this if we're happy
#  with the default; we can also change it later, e.g., for different batch sizes)
net.blobs['data'].reshape(50,        # batch size
                          3,         # 3-channel (BGR) images
                          227, 227)  # image size is 227x227

predict_array = []
groundtruth_array = []
#test_file = open('/home/cliu/github/caffe-tools/data/xray/xray_diagnose_test.txt', "r+")
test_file = open('/home/cliu/github/caffe-tools/data/xray/xray_diagnose_train.txt', "r+")

for item in test_file.readlines():
	img_name =  item.split(' ')
	true_label = img_name[1][:-1]
	groundtruth_array.append(int(true_label))
	image = caffe.io.load_image(img_name[0])
	transformed_image = transformer.preprocess('data', image)

	# copy the image data into the memory allocated for the net
	net.blobs['data'].data[...] = transformed_image

	### perform classification
	output = net.forward()
	output_prob = output['prob'][0]  # the output probability vector for the first image in the batch
	predict_array.append(int(output_prob.argmax()))

	print 'predicted class is:', output_prob.argmax()


target_names = ['class 0', 'class 1', 'class 2', 'class 3']
print predict_array, groundtruth_array
print(classification_report(groundtruth_array, predict_array, target_names=target_names))
test_file.close()
