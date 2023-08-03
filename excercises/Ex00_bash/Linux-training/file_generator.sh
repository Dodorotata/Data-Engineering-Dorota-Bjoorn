#!/bin/bash

echo "running initalizations"
sleep 1

for i in {1..3}; do
  touch note$i.txt
done

touch note4


#---- alternative
# create note files
# for i in {1..4}; do
  # if [ $i -le 3 ]; then
  #   filename=note$i.txt
  # else
  #   filename=note$i
  # fi
  # touch $filename
# done