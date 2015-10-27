#!/usr/bin/env python
"""
* This program is used for cutting the raw images using the bounding-box label
which is a 4-dimension tuple (x_left, x_up, x_right, x_down)

* Author: Chang Liu
"""
import Image

src_path = '/home/ycao/cli/C0005768-8F_110512154251915.JPG'
src = Image.open(src_path)
frame = src.crop((0, 0, 800, 1000))
frame.save(src_path[:-4]+"_crop.jpg")
