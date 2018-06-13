#!/usr/bin/env bash
./build/tools/caffe train --solver  models/VGG_CNN_S/solver.prototxt --weights models/VGG_CNN_S/VGG_CNN_S.caffemodel -gpu 0 2>&1 | tee im-ft-vgg.log
