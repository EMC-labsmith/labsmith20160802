#!/bin/bash

fro=$1
machine=$2
to=$3
echo -e $fro" want to use "$machine"." \
		"Please release it if that is Okay. Thanks!\n" \
		"http://10.62.34.100\n" > /home/joe/labsmith_backup/wantfile
mail -s "$fro want to use $machine" $to < /home/joe/labsmith_backup/wantfile


