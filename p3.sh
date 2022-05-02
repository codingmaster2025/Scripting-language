#!/bin/bash

#Jinwei Zhou
#Jinwzhou
#114177591

if [ $# -eq 0 ]
then
	echo "score directory missing"
	exit 0
fi


if [ $# -ne 1 ]
then
	echo "USAGE: p3.sh<dirname>"
	exit 0
fi

if [ ! -d $1 ]
then
	echo "<dirname> is not a directory"
	exit 0
fi


path=$(realpath $1)



for entry in "$path"/*
do

    if [ -f "$entry" ]
    then


        ID=$(tail -n +2 $entry | sed -e 's/,/\n/g' | head -n +1)
        #start from second line, then /n list, get the first value
        scores=$(tail -n +2 $entry | sed -e 's/,/\n/g' | tail -n +2) #tail -n +2 skips the first line (total file size)
        # tail - last part of the file ///output  the  last  K lines, instead of the last 10; or use -n +K to output lines starting with the Kth)
        total=0
        for score in $scores
        do
            total=$((total+score))
        done
        total=$((total*2))
        echo -n "$ID:"
	    if [ $total -ge 93 ]
	    then
	    	echo "A"
	    elif [ $total -ge 80 ]
	    then
	    	echo "B"
	    elif [ $total -ge 65 ]
	    then
	    	echo "C"
	    elif [ $total -ge 51 ]
	    then
	    	echo "D"
	    else
	    	echo "F"
	    fi

    fi

done