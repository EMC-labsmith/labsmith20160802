#!/bin/bash
machine=$1
mailto=$2
nowtime=$3
echo -e "Please release it. Thanks!\n" \
		"http://10.62.34.99:8010/labsmith/ \n" >wantfile
at $nowtime + 1 minutes << EOF	
mail -s "RELEASE " $to < wantfile
EOF

