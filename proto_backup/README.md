README
===


##GUIDE for dataset:

**new_train_sort.txt, new_test_sort.txt**: For UEC 256-category with v0~v2 for training, v3~v4 for testing. Label is from **0~255**.

**uec_test_256_sort.txt  uec_train_256_sort.txt**: For UEC 256-category with v0~v2 for training, v3~v4 for testing. Label is from **10~165**.

**uec_train.txt, uec_test.txt**: For UEC256-category + COCO-Food category for training and testing(UEC is same partition, coco is used by the labels from coco dataset's train and val partition). Label is from **0~265**.


##RESULT

for uec_test(coco+uec), top-1 ~ 49%, top-5 ~ 78%.


for uec_256 wrong label(10 ~ 265 label): very low, top-1 ~ 2%, top-5 ~ 7% (This wrong label may have a very bad influence! see [NOTE](https://github.com/DeercoderResearch/caffe-tools/blob/cdd62fbef47d6725a2842ac68b899525136c5fb2/NOTE.md) )


for uec_256 right label: To be seen
