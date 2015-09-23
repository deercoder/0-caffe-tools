#!/usr/bin/env bash
./build/tools/caffe train --solver models/finetune_googlenet_food/solver.prototxt -weights models/bvlc_googlenet/bvlc_googlenet.caffemodel -gpu 0 2>&1 | tee food.log
