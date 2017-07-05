#!/bin/bash

fro=$1
machine=$2
port=$3
to=$4
echo -e $fro" want to use "$machine $port"." \
		"Please release it if that is Okay. Thanks!\n" \
		"http://10.62.34.100/labsmith/ \n" > /home/joe/labsmith_backup/wantfile
mail -s "$fro want to use $machine $port" $to < /home/joe/labsmith_backup/wantfile


