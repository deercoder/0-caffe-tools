#!/usr/bin/env python

import os
#import caffe
import os
import numpy as np
import skimage.io
from skimage import img_as_float # using image from opencv with skimage
from skimage.util import random_noise
from skimage import transform
from skimage.transform import AffineTransform
from skimage.filters import gaussian
from skimage.exposure import rescale_intensity
import cv2
import math
import glob


def equaHist(img):
    #Histogram Equalization
    img[:, :, 0] = cv2.equalizeHist(img[:, :, 0])
    img[:, :, 1] = cv2.equalizeHist(img[:, :, 1])
    img[:, :, 2] = cv2.equalizeHist(img[:, :, 2])
    return img

# add new interface using skimage
def sk_fliph(img):
    return np.fliplr(img)

def sk_flipv(img):
    return np.flipud(img)

# the parameter is not the sequence, so must use the specific KEY
def sk_random_noise(img, mode = 'gaussian', rate = 0.01):
    img_rn = random_noise(img, mode = "gaussian", var = 0.01)
    return img_rn

def sk_rotate(img, angle):
    img_rt = transform.rotate(img, angle)
    return img_rt

def sk_translate(img, x, y):
    img_trans = transform.warp(img, AffineTransform(translation=(-x, -y)))
    return img_trans

def sk_zoom(img, p1x, p1y, p2x, p2y):
    h = len(img)
    w = len(img[0])

    crop_p1x = max(p1x, 0)
    crop_p1y = max(p1y, 0)
    crop_p2x = min(p2x, w)
    crop_p2y = min(p2y, h)

    cropped_img = img[crop_p1y:crop_p2y, crop_p1x:crop_p2x] 
    x_pad_before = -min(0, p1x)
    x_pad_after  =  max(0, p2x-w)
    y_pad_before = -min(0, p1y)
    y_pad_after  =  max(0, p2y-h)

    padding = [(y_pad_before, y_pad_after), (x_pad_before, x_pad_after)]
    is_color = len(img.shape) == 3
    if is_color:
        padding.append((0,0)) # colour images have an extra dimension

    padded_img = np.pad(cropped_img, padding, 'constant')
    return transform.resize(padded_img, (h,w))

def sk_blur(img, sigma = 1.0):
    is_color = len(img.shape) == 3
    img_blur = rescale_intensity(gaussian(img, sigma=sigma, multichannel=is_color)) 
    return img_blur

# skimage implementation ends


# flip horonzontally or vertically
def flip(img, axis=1):
    fp = cv2.flip(img, 1)
    return fp	

# rotate in angles
def rotate(img, w, h, angle):
     rot_mat = cv2.getRotationMatrix2D((w*0.5, h*0.5), angle, 1.0)
     new_img = cv2.warpAffine(img, rot_mat, (int(math.ceil(w)), int(math.ceil(h))), flags=cv2.INTER_LANCZOS4)
     return new_img

def shear(img, w, h, shear_range):
     pts1 = np.float32([[5,5],[20,5],[5,20]])
     pt1 = 5+shear_range*np.random.uniform()-shear_range/2
     pt2 = 20+shear_range*np.random.uniform()-shear_range/2
     pts2 = np.float32([[pt1,5],[pt2,pt1],[5,pt2]])
     shear_M = cv2.getAffineTransform(pts1,pts2)
     img_sh = cv2.warpAffine(img,shear_M,(w, h))
     return img_sh

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
	is_equaHist = False
	is_shear = False
	angles = []
	
	# 7x times(org, flip, shear, eqHist, 3 angles)
	if int(count) < 500:
		is_flip = True
		angles = [90, 180, 270] # 45/135/225 is not good, leaving black background
		is_equaHist = True
		is_shear = True
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
		skimage.io.imsave(dst_sub_dir + "/" +  image_name + "_org.jpeg", image)
		print "saving ", image_name

		# flip is ture
		if is_flip == True:
			img_mirror = cv2.flip(image, 1)
			img_mirror = img_as_float(img_mirror)
			skimage.io.imsave(dst_sub_dir + "/" +  image_name + "_flip.jpeg", img_mirror)
			print "saving flipped", image_name

		if is_shear == True:
			cv_img = cv2.imread(img)
			img_shear = shear(cv_img,int(im_w), int(im_h), 5)
			cv2.imwrite(dst_sub_dir + "/" +  image_name + "_shear.jpeg", img_shear)
			print "saving shear", image_name

		if is_equaHist == True:
			cv_img = cv2.imread(img)
			img_eq = equaHist(cv_img)
			cv2.imwrite(dst_sub_dir + "/" +  image_name + "_eq.jpeg", img_eq)
			print "saving eqal hist", image_name

		# do rotation in angle
		for ag in angles:
			cv_imgs = cv2.imread(img) # here cannnot use image(from caffe.io.load_image)
			img_rot = rotate(cv_imgs, int(im_w), int(im_h), ag)
			cv2.imwrite(dst_sub_dir + "/" +  image_name + "_"+ str(ag)+".jpeg", img_rot)
			print "saving rotated", image_name + str(ag)

	f.close()

def test_sk_api():
    img_path = "a.jpeg"
    img = skimage.io.imread(img_path)
    print img
    # flip horizontal
    img_fliph = sk_fliph(img)
    skimage.io.imsave("a_fliph.jpeg", img_fliph)
    # flip vertical
    img_flipv = sk_flipv(img)
    skimage.io.imsave("a_flipv.jpeg", img_flipv)
    # random noise
    img_rdnoise = sk_random_noise(img)
    skimage.io.imsave("a_rdnoise.jpeg", img_rdnoise)
    # rotate
    img_rot = sk_rotate(img, 90)
    skimage.io.imsave("a_rotate90.jpeg", img_rot)
    # translate
    img_trans = sk_translate(img, 20, 10)
    skimage.io.imsave("a_trans_20_20.jpeg", img_trans)
    # zoom
    img_zoom = sk_zoom(img, 150, 0, 300, 150)
    skimage.io.imsave("a_zoom.jpeg", img_zoom)
    # blur
    img_blur = sk_blur(img, 1.0)
    skimage.io.imsave("a_blur.jpeg", img_blur)
   


if __name__ == "__main__":
#	main()
	test_sk_api()
