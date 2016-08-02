#!/bin/bash

machine=$1
port=$2
tomail=$3
echo -e "You have reserved $machine successfully!\n\n" \
        "Please be reminded: \n" \
        "- Release array immediately when you are not using it! \n" \
		"- Release array in normal mode, and undo any hardware or connection changes. \n" \
		"- Use Maintenance log to record changes. \n" > /home/joe/labsmith_backup/reservefile
mail -s "You have reserved $machine successfully!" $tomail < /home/joe/labsmith_backup/reservefile





