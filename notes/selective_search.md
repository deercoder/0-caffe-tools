Selective Search
===



### **Description**

**SelectiveSearchPcode**: old code, check `demo.m`

**SelectiveSearchCodeIJCV**: new code, check `demoPascal2007.m`


### **Abstract**
Selective search is a very important process in the R-CNN's algorithm, since the first step is to generate the VOC2007_train.mat/VOC2007_test.mat, so I have to generate my own dataset's `.mat` file.

For this part, we should note that three files are very important, which are:

+ imdb/imdb_from_voc.m (list of images and classes)
+ imdb/roidb_from_voc.m (region of interest database)
+ imdb/imdb_eval_voc.m (evalutation)

**NOTE**: for fine-tuning, the generating of window file is critical, however, it still calls `imdb_from_voc`, which calls `roidb_from_voc.m`, the latter one contains some code that read the `VOC2007_train.mat` file in the folder `data/selective_search`, so if our dataset is different, it should use another instead of the pre-downloaded data files.

### **Debug**

I have encountered some problems when debugging the R-CNN's code, as follows:

1) Fine-tuning is error.

Track: I think it's caused by the previous selective_search data file, but it still contains some problem in the above three files.


2) 



### About the Selective Search Algorithm

1) The R-CNN doesn't contain the source code of selective search, We should go to [here](http://disi.unitn.it/~uijlings/MyHomepage/index.php#page=projects1) to download the source codes.

2) By default, the R-CNN's repo will download the source code, but it is a later version of selective search, that doesn't include the generating of VOC2007 dataset, I think the older one is very useful, since the demo could be used on our own dataset. Then I still use it on old codes to generate the `.mat` file. **NOTE**: using old or new doesn't affect much, since they just influence the more precise window. And the pre-downloaded [2007 trainval](http://www.huppelen.nl/SelectiveSearch/SelectiveSearchVOC2007trainval.mat) and [2007 test](http://www.huppelen.nl/SelectiveSearch/SelectiveSearchVOC2007test.mat) are all the old code's generation.

