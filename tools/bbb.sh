#!/usr/bin/env bash
i=0
while [ $i -le 256 ] 
do
	echo "\""$((i))"\"",
	i=$((i+1))
done
