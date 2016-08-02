#!/bin/bash

machine=$1
port=$2
tomail=$3
status=$4
echo -e "Please make sure $machine is in good status, Machine status: $status.\n" \
		"http://10.62.34.99:8010/labsmith/ \n" > /home/joe/labsmith_backup/releasetoownerfile
mail -s "You have released $machine now" $tomail < /home/joe/labsmith_backup/releasetoownerfile


