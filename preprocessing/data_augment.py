#!/usr/bin/env python

import os
import caffe
import os
import numpy as np
import skimage.io
import cv2
import math
import glob


def equaHist(img):
    #Histogram Equalization
    img[:, :, 0] = cv2.equalizeHist(img[:, :, 0])
    img[:, :, 1] = cv2.equalizeHist(img[:, :, 1])
    img[:, :, 2] = cv2.equalizeHist(img[:, :, 2])
    return img

# flip horonzontally or vertically
def flip(img, axis=1):
    fp = cv2.flip(img, 1)
    return fp	

# rotate in angles
def rotate(img, w, h, angle):
     rot_mat = cv2.getRotationMatrix2D((w*0.5, h*0.5), angle, 1.0)
     new_img = cv2.warpAffine(img, rot_mat, (int(math.ceil(w)), int(math.ceil(h))), flags=cv2.INTER_LANCZOS4)
     return new_img

def main():
    #parse the text file 
    f = open("train_label_count.txt", "r+")
    rlines = f.readlines()

    # BASE_DIR
    base_dir = "/data0/dataset/iMaterials/train_all/"
    dst_dir = "/data0/dataset/iMaterials/aug_train_all/"
    for item in rlines:
	label, count, _ = item.split(" ") 
	is_flip = False
	angles = []
	
	# 9x times(org, flip, 7 angles)
	if int(count) < 500:
		is_flip = True
		angles = [45, 90, 135, 180, 225, 270, 315]	
	# 5x times(org, flip, 3 angles)
	elif int(count) in range(500, 1000):
		is_flip = True
		angles = [90, 180, 270]
	# 3x times(org, flip, 1 angles)
	elif int(count) in range(1000, 2000):
		is_flip = True
		angles = [180]
	# 2x times(org, flip
	elif int(count) in range(2000, 3000):
		is_flip = True
	else:
		print ">3000" 

	### Now processing
	sub_dir = base_dir + str(label)
	dst_sub_dir = dst_dir + str(label)
	if not os.path.exists(dst_sub_dir):
		os.mkdir(dst_sub_dir)
	imgs = glob.glob(sub_dir + "/*.jpeg")
	for img in imgs:
		# save original image
		image_name = img.split("/")[-1][:-5]
		image = caffe.io.load_image(img, color=True)
		im_w = image.shape[1]
		im_h = image.shape[0]
		cv2.imwrite(dst_sub_dir + "/" +  image_name + "_org.jpeg", image)
		print "saving ", image_name

		# flip is ture
		if is_flip == True:
			img_mirror = cv2.flip(image, 1)
			cv2.imwrite(dst_sub_dir + "/" +  image_name + "_flip.jpeg", img_mirror)
			print "saving flipped", image_name

		# do rotation in angle
		for ag in angles:
			img_rot = rotate(image, im_w, im_h, ag)
			cv2.imwrite(dst_sub_dir + "/" +  image_name + "_"+ str(ag)+".jpeg", img_rot)
			print "saving rotated", image_name + str(ag)

	f.close()

if __name__ == "__main__":
	main()
