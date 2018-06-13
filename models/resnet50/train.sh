#!/usr/bin/env bash
./build/tools/caffe train --solver  models/resnet50/solver.prototxt -gpu 2 2>&1 | tee im-resnet50.log
