#!/bin/bash
for dir in /data0/dataset/nihcc/*;
do
    dir_name=$(basename $dir)
    echo $dir_name
    cd $dir
    nums=$(ls |wc -l)
    echo $nums
    test_nums=$((nums/5))
    echo $test_nums
    train_nums=$((nums-test_nums))
    echo $train_nums
    mkdir /data0/dataset/nihcc-train/tf-data/train/$dir_name
    mkdir /data0/dataset/nihcc-train/tf-data/test/$dir_name
    i=0
    for f in *;
    do 
       if [ $i -lt $train_nums ]
       then
           cp $f /data0/dataset/nihcc-train/tf-data/train/$dir_name
       else 
           cp $f /data0/dataset/nihcc-train/tf-data/test/$dir_name
       fi 
       let i++;
    done
done
