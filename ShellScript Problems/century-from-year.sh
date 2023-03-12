#!/bin/bash
year=$1

if [ $((year%100)) -eq 0 ]
then
  echo $((year / 100))
else
  echo $((year / 100 + 1))
fi
