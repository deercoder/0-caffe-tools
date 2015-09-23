#!/usr/bin/env bash
i=1
while [ $i -le 256 ] 
do
	echo "\""$((i+9))"\"",
	i=$((i+1))
done
