#!/bin/bash
r=$1
s=$2
letter=$s
var=0

while [ $var -lt $((r-1)) ]
do
  s+=$letter
  var=$((var + 1))
done

echo $s
