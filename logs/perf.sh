#!/bin/bash

PROC="pyt-ping.py"
OPT=""
if [ "$1" = "-m" ]
then
	OPT="-H"
fi

top $OPT -b -p $(ps -ef | grep "$PROC" | awk '{ print $2}' | head -n 1) | grep -i $USER

