#!/usr/bin/env bash
# This file is used for generating labels for caffe training on UEC-100 category dataset

# first, empty the label file
echo > train.txt
echo > test.txt

# divide by 4:1 training/testing ratio
cat val0.txt > train.txt
cat val1.txt >> train.txt 
cat val2.txt >> train.txt 
cat val3.txt >> train.txt 
cat val4.txt > test.txt

# now this file only contain file name, we need absolute path, and its label
