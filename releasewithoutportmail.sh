#!/bin/bash

machine=$1
tomail=$2
echo -e "You can reserve "$machine" now.\n" \
		"http://10.62.34.100/labsmith/ \n" > /home/joe/labsmith_backup/releasewithoutportfile
mail -s "You can reserve $machine now" $tomail < /home/joe/labsmith_backup/releasewithoutportfile


