#!/bin/bash

ans1=$(($1 % $2))
ans2=$(($1 % $3))

if [[ $ans1 -eq 0 && $ans2 -eq 0 ]]
then
  echo "true"
else
  echo "false"
fi
