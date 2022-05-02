#!/bin/bash

#Jinwei Zhou
#Jinwzhou
#114177591

if [ $# -ne 3 ]
then
    echo "USAGE: p1.sh <extension> <src_dir> <dst_dir>"
    exit 0

fi


if [ ! -d $2 ]
then
    echo "<src_dir> not found"
    exit 0
fi

if [ -d $3 ]
then
    pathname=$(realpath $3)
    cd "$2"
    find . -type f -name "*$1" -exec cp --parents {} "$pathname"/ ';'
    find . -type f -name "*$1" -exec rm {}  ';'
    cd

else
    mkdir "$3"
fi