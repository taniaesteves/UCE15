#!/bin/bash

modelDir="/home/atlas/AtlasInnovation/UCE15/Code/Model"
geojsonsDir="/home/atlas/geojsons"

while :
do
	echo "Executing script dbToDashboard.py"
	echo -e "\nSinais de Transito\n" | python3 $modelDir/dbToDashboard.py > /home/atlas/logs_daemon.txt
	sleep 2m
done
