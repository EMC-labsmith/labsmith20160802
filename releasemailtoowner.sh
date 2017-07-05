#!/bin/bash

machine=$1
tomail=$2
status=$3
echo -e " Please make sure $machine is in good status. Current machine status:\n\n" \
        "$status\n"\ > /home/joe/labsmith_backup/releasetoownerfile
mail -s "You have released $machine" $tomail < /home/joe/labsmith_backup/releasetoownerfile


