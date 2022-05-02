#!/bin/bash



if [ $# -ne 1 ]
then
	echo "input directory is missing"
	exit 0
fi

if [ ! -d $1 ]
then
	echo "the directory does not exist"
	exit 0
fi


cd $1

echo "Current date and time: $(date)"
echo "Current directory is: $(pwd)"
echo ""
echo "--- 10 most recently modified directories ---"
echo "$( ls -ltc | grep "^d" | head -n 10)"

echo ""
echo "--- 6 largest files ---"

echo "$( ls -lS | grep "^-" | head -n 6)"


for (( i=1; i<=70; i++ ));
do
    echo -n "="

done
echo ""

cd ~
