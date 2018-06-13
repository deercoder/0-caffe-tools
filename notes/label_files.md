Label Files
===

## NOTE

These folder are copied from official caffe repo, if you want to use it for pre-training or fine-tuning, just copy these files back to caffe and run the corresponding script.


## How it works?

1. Under the **data** folder, there stored the label files like `train.txt`, `test.txt`, `val.txt`, they're essential for our pre-training or fine-tuning.

	During pre-training, what we use is mainly the `train.txt`, there **MUST** be file name with its lable from 0 ~ 999 for each line, like the below:

		n01440764/n01440764_10074.JPEG 0

	For  each list there is similar structure, similarly, in `val.txt` or `test.txt` they're also organized in this structure.

2. Under the  **example** folder, there stored some scripts that are used for creating resized images, computing the mean value and other functions, they're almost the same as original imagenet or other database sets, but we need to change the path in these scripts. And we also need to adjust to our own dataset settings. In original dataset, imagenet, ilsvr12, finetune_flickr, there're all different functions of the scripts.

3. Under the **models** folders, there stored many model definitions in `.prototxt` which are used for define our CNN network, they're the details for each layer's parameter like learning rate, data type, iteration times,  we should also note the **PATH** in those text files because it use the `.binaryproto` for training or fine-tuning.

4. Pre-training is different from fine-tuning, they have different class kinds and dataset. Here, in pre-training use 1000 classes, but the fine-tuning only contains 20 classes, so during fine-tuning, we need to adjust the last layor in order to get the right classification number to fit for our 20-class category.

More details should be refered and enriched later, refer to more details here[1],[2]...

[1]:  http://caffe.berkeleyvision.org/gathered/examples/imagenet.html
[2]: http://caffe.berkeleyvision.org/gathered/examples/finetune_flickr_style.html

