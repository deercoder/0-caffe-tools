ref to: https://github.com/BVLC/caffe/wiki/Using-a-Trained-Network:-Deploy

learn how to generate the `deploy.prototxt`.


## Code


## Error

1. I cannot get good results, or I can only get random results?

   becuase the `deploy.prototxt` is not correct, use old prototxt or not corresponding prototxt,
   make sure to generate them from the original `train_val.prototxt` file.


2. I cannot speed up the testing.

   using `caffe.io.load_image` can only one image, for batch loading, using the `net.forward()` function.
   previously I used the `net.predict`, though it can load multiple images
