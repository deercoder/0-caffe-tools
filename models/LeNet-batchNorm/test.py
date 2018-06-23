import numpy as np
import matplotlib.pyplot as plt
import glob
import PIL
from PIL import Image


# Make sure that caffe is on the python path:
caffe_root = '../../'  # this file is expected to be in {caffe_root}/examples
import sys
sys.path.insert(0, caffe_root + 'python')

import caffe

# Set the right path to your model definition file, pretrained model weights,
# and the image you would like to classify.
MODEL_FILE = 'deploy.prototxt'
PRETRAINED = 'lenet_iter_10000.caffemodel'

caffe.set_mode_gpu()
caffe.set_device(1)

net = caffe.Net(MODEL_FILE, PRETRAINED, caffe.TEST)

transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2,0,1))  # move image channels to outermost dimension
transformer.set_raw_scale('data', 255)      # rescale from [0, 1] to [0, 255]

img = caffe.io.load_image("image_5.png", color=False)
img = caffe.io.resize(img, (28, 28))
transformed_image = transformer.preprocess('data', img)
net.blobs['data'].data[0] = transformed_image
probs = net.forward()
label = probs['loss'].argmax(axis=1)
print label
