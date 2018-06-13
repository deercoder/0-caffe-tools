#!/usr/bin/env bash
#./build/tools/caffe train --solver  models/fine-grained-cls/GoogleNet_cub_2011_solver_4.prototxt -gpu 0  2>&1 | tee im.log
./build/tools/caffe train --solver  models/finetune_googlenet/solver.prototxt --weights models/bvlc_googlenet/bvlc_googlenet.caffemodel -gpu 1 2>&1 | tee im-ft-googlenet.log
