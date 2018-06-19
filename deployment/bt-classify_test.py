import numpy as np
import matplotlib.pyplot as plt
import glob
import PIL
from PIL import Image


# Make sure that caffe is on the python path:
caffe_root = '../../../../'  # this file is expected to be in {caffe_root}/examples
import sys
sys.path.insert(0, caffe_root + 'python')

import caffe

# Set the right path to your model definition file, pretrained model weights,
# and the image you would like to classify.
MODEL_FILE = 'bt-deploy.prototxt'
PRETRAINED = 'GoogleNet_cub_2011_4_iter_780000.caffemodel'
IMAGE_FILE = '/data3/users/roy/iMaterials-all/test/'

caffe.set_mode_gpu()
caffe.set_device(1)
net = caffe.Classifier(MODEL_FILE, PRETRAINED,
                       mean= None,
                       channel_swap=(2,1,0),
                       raw_scale=255,
                       image_dims=(226, 226))


file = "submission.csv"
file_handler = open(file, "w+") 

file_handler.write("id,predicted\n")

img_lists = glob.glob(IMAGE_FILE + "*.jpg")


transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2,0,1))
transformer.set_channel_swap('data', (2,1,0))  # the reference model has channels in BGR order instead of RGB
net.blobs['data'].reshape(50,3,226,226) 


batch_ids = []

for i, f in enumerate(img_lists):
    img = Image.open(f)
    # scale all images to 256x256
    img = img.resize((226,226), PIL.Image.ANTIALIAS)
    img = np.array(img).astype(np.float32)

    transformed_image = transformer.preprocess('data', img)
    #print transformed_image.shape

    id = f.split('/')[-1][:-4]
    batch_ids.append(id)

    index = i % 50

    # put the image into i-th place in batch
    net.blobs['data'].data[index,:,:,:] = transformed_image   

    if (i+1)%50 == 0:
	# after reading all images into batch, forward once:
	probs = net.forward()
	
	# prediction results
	preds = probs['loss'].argmax(axis=1)
	print preds

	# saving all into file
	for item in range(len(preds)):
	        file_handler.write(str(batch_ids[item]) + "," + str(preds[item]+1) + "\n")	

	# clear the batch list
	batch_ids = []


file_handler.close()
