#!/bin/bash

machine=$1
port=$2
tomail=$3
echo -e "You can reserve "$machine $port" now.\n" \
		"http://10.62.34.100/labsmith/ \n" > /home/joe/labsmith_backup/releasefile
mail -s "You can reserve $machine $port now" $tomail < /home/joe/labsmith_backup/releasefile


