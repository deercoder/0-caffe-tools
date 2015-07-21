README
====

This models define my configuration for food image category classification

### Dataset

Using Images from [Microsoft CoCo Dataset](http://mscoco.org/) for fine-tuing

### Method

Here I used the pret-trained models from ImageNet with 1,000 classes, which is also for training the image classification models, then using the method from [finetuning using Flickr dataset](http://caffe.berkeleyvision.org/gathered/examples/finetune_flickr_style.html), I can fine-tuned on my own dataset with my protobuf definition

### Start training

Similar to the flickr method, I changed the models definition under models/ folder, then add the training dataset, which includes the images, train.txt, test.txt(for details about these dataset, refer to [Coco-1](https://github.com/DeercoderResearch/coco-1)).

**NOTE**: My food image from coco contains 10 categories, so in *train\_val.txt* the `num_output` should be `10`.

### Attention

1. Never forget to check the protobuf definition for your own dataset

2. Never forget to sort the train.txt or test.txt, otherwise it will return bad accuracy result.
