NOTES
=====

For some very easy notes about the caffe and its usage:


1. To specify the caffe's using GPU, just add the parameter `-gpu id`. For example ,when using caffe for pre-training, here is a good example.
		
		./tools/caffe train --solver=models/my_own_dataset_caffenet/solver.prototxt -gpu 3


	this above command gives a description about using the gpu with the id=3, so that it will not affect others' work.


2. To verity some work, it is necessary to do some experiments, but it's a waste of time to run it without any understanding of the code and its mechanism. Note to work smart rather than blindness.

