#!/usr/bin/env bash
#./build/tools/caffe train --solver  models/fine-grained-cls/GoogleNet_cub_2011_solver_4.prototxt -gpu 0  2>&1 | tee im.log
./build/tools/caffe train --solver  models/fine-grained-cls/GoogleNet_cub_2011_solver_4.prototxt --snapshot GoogleNet_cub_2011_4_iter_10000.solverstate -gpu 0  2>&1 | tee im.log
