#!/bin/bash

modelDir="/home/atlas/AtlasInnovation/UCE15/Code/Model"
geojsonsDir="/home/atlas/geojsons"
dashboardDir="/home/atlas/AtlasInnovation/UCE15/Code/Dashboard"

while :
do
	rm $geojsonsDir/*
	echo "Executing script dbToDashboard.py"
	echo -e "\nSinais de Transito\n" | python3 $modelDir/dbToDashboard.py > /home/atlas/logs_daemon.txt
	rm $dashboardDir/data/*
	cp $geojsonsDir/* $dashboardDir/data/
	sleep 30
done
