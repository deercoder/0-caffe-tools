How to create LMDB


LMDB (Lightning Memory – Mapped Database) is a key-value store database, supported by Intel distribution of Caffe*. One of the most advantage of this solution is its high-throughput. Trainings and validation datasets can be converted to the form stored in the LMDB.

##General scenario and parameters description Intel distribution of Caffe provides script supporting users with creation of LMDB.

General steps:

Prepare training and validation data. Each type of files should be stored separately.
If necessary, perform pre-processing of the training/validation data (e.g., for the images resize height/width).
Create LMDB, using the Intel distribution of Caffe script. It is located in: /examples/imagenet/create_imagenet.sh. Before run, please verify following parameters of the script:
TRAIN_DATA_ROOTand VAL_DATA_ROOT variables point to the path of the training and validation data
GLOG_logtostderr variables are set with following parameters:
resize_height – the height of the image will be resized according to this
resize_width – the width of the image will be resized according to this value
shuffle – if set, during creating LMDB database, entries will be mixed (the order of the entries will be random)
encoded – if true the LMDB will be compressed
$TRAIN_DATA_ROOT/$VAL_DATA_ROOT – previously set path to the downloaded training and validation data
$DATA/train.txt or $DATA/val.txt – text file indicates a classification of the images used to training or validation.
$EXAMPLE/ilsvrc12_train_lmdb or $EXAMPLE/ilsvrc12_val_lmdb – the path to the location where LMDB will be saved
For every new GLOG_logtostderr variable instance, a new LMDB is created, according to the set parameters.
Use the created LMDB in the Intel distribution of Caffe.
##Example execution:

For this guide purposes, examples illustrate this point by importing training and validation data from the ImageNet.

Download ImageNet training and validation data.
Navigate to the imagenet directory, e.g., cd path/to/caffe/examples/imagenet
Edit the create_imagenet.sh script, which should contain the following:
TRAIN_DATA_ROOT=/data/imagenet/train/
VAL_DATA_ROOT=/data/imagenet/val/
RESIZE=true
if $RESIZE; then
 RESIZE_HEIGHT=256
 RESIZE_WIDTH=256
else	
 RESIZE_HEIGHT=0
 RESIZE_WIDTH=0
fi
GLOG_logtostderr=1 $TOOLS/convert_imageset \
   --resize_height=$RESIZE_HEIGHT \
   --resize_width=$RESIZE_WIDTH \
   --shuffle \ 
   -encoded=true \
   $TRAIN_DATA_ROOT \
   $DATA/train.txt \
   $EXAMPLE/ilsvrc12_train_lmdb

echo "Creating val lmdb..."
Run the script, e.g: ./examples/imagenet/create_imagenet.sh
Results of the script run above:

Creating val lmdb...
I1124 10:58:44.212462 193703 convert_imageset.cpp:123] Shuffling data
I1124 10:58:44.219236 193703 convert_imageset.cpp:126] A total of 50000 images.
I1124 10:58:44.219633 193703 db_lmdb.cpp:72] Opened lmdb examples/imagenet/ilsvrc12_val_lmdb
I1124 10:58:51.641278 193703 convert_imageset.cpp:184] Processed 1000 files.
I1124 10:58:58.952800 193703 convert_imageset.cpp:184] Processed 2000 files.
I1124 10:59:05.942912 193703 convert_imageset.cpp:184] Processed 3000 files.
I1124 10:59:13.198263 193703 convert_imageset.cpp:184] Processed 4000 files.
I1124 10:59:20.982733 193703 convert_imageset.cpp:184] Processed 5000 files.

   			             [...]

I1124 11:04:31.749557 193703 convert_imageset.cpp:184] Processed 48000 files.
I1124 11:04:39.371922 193703 convert_imageset.cpp:184] Processed 49000 files.
I1124 11:04:46.304036 193703 convert_imageset.cpp:184] Processed 50000 files.
Done.
The ilsvrc12_val_lmdb directory should be created by the script, in the path according to the set EXAMPLE variable.
Update the .prototxt file of the particular model using in the Intel distribution of Caffe, e.g.,
data_param {
   source: "examples/imagenet/ilsvrc12_train_lmdb"
   batch_size: 256
   backend: LMDB
 }

