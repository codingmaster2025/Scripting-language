#!/bin/bash

#Jinwei Zhou
#Jinwzhou
#114177591


if [ $# -ne 2 ]
then
    echo "data file or output file not found"
    exit 0
fi

if [ ! -f $1 ]
then
    echo "<filename> not found"
    exit 0
fi

if [ ! -f $2 ]
then
    echo "">"$2"

fi

declare -a list

while read Line
do
    index=1
	for i in $(echo $Line | tr ";:," "\n")
	do
		list[$index]=$((list[index]+ i ))
        index=$((index+1))
    done

done < $1

echo "">"$2"

for (( i=1; i<=${#list[@]}; i++ ));

do
   echo "Col $i: ${list[$i]}" >>$2


done

unset list
