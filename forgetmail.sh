#!/bin/bash

user=$1
pwd=$2
mailto=$3

echo -e "  Hi $user, your new password is: $pwd\n \
 http://10.62.34.100/labsmith/ \n"> /home/joe/labsmith_backup/tempfile
mail -s "Your new password for Labsmith" $mailto < /home/joe/labsmith_backup/tempfile


