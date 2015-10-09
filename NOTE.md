NOTE
===



github/caffe: Since I use 6k models to finetune, but it still fall dramatically since 10k interations, so that the top-1/top-5 is 2.xx% and 7.xx%, I think there is something wrong with the labels, so I relabelled from 0 to 255, and then I using the new label file to do the training based on the googlenet.caffemodel


caffe: I insist that using the old 10 ~ 265 lables to do the training, but according to observation, that it falls dramatically since 10k(before that 10k it has 34% top-1, and 68% top-5). I tried experiment to retrain based on 6k iterations(on this it's still high precision so I think it maybe a coincidence. However it still falls dramatically, which makes me beleive that the data label has a bad influence).




Review
===


1. Using bad labels(10 - 265), it looks bad from 10k iteration.

2. To eliminate the random error, I observe that when iteration is ~6k, the top-1 and top-5 are still very high(34%, 68%). But even if I restore from the 6k caffemodels, it still occurred the fall of precision. So I think it's not random and the problem may be because of the labels.

3. So in order to verify my hyposisth, I relabelled from 0 ~ 255, then I rerun the training to see its effect(in ~/github/caffe).

4. In order for a comparsion, I still keep the old label 10~265 experiment running, to see the final result. Maybe it's temporary result. However, up until 55k, it's still  very low, that convince me maybe it's vital. Anyway, I will keep running until it ends, and compare with the new experiment in 3.

The result for comparasion is to be seen according to my understanding.
