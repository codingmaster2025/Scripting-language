#!/bin/bash


path1=$(realpath $1)
path2=$(realpath $2)


if [ $# -ne 2 ]
then
	echo "input file and dictionary missing"
	exit 0
fi


if [ ! -f $path1 ]
then
	echo "<filename> is not a file"
	exit 0
fi

if [ ! -f $path2 ]
then
	echo "<filename> is not a file"
	exit 0
fi

words=$( cat $path1 | tr " " "\n" | sed -e "s/[,:.]//g" | egrep '^\b[a-zA-Z]{5}\b$' )



for word in $words
do
    if ! grep -iq $word $path2;
    then
        echo "$word"
    fi
done
