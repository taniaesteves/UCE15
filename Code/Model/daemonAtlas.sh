#!/bin/bash

modelDir="/home/atlas/AtlasInnovation/UCE15/Code/Model"
dataDir="/home/atlas/data"
dashboardDir="/home/atlas/AtlasInnovation/UCE15/Code/Dashboard"

getCurrentTime() {	
	now=$(date +"%T")
}

while :
do
	
	getCurrentTime
	echo "$now: Awake"	
	
	getCurrentTime
	echo "$now: > Removing all from $dataDir"
	rm $dataDir/*
	
	getCurrentTime
	echo  "$now: > Executing atlas_dbToDashboard"
	echo -e "\nSinais de Transito\n" | python3 $modelDir/atlas_dbToDashboard.py > /home/atlas/logs_atlas_dbToDashboard.txt

	getCurrentTime
	echo  "$now: > Executing atlas_dbToCsv"
	echo -e "\nSinais de Transito\n" | python3 $modelDir/atlas_dbToCsv.py > /home/atlas/logs_atlas_dbToCsv.txt
	
	getCurrentTime
	echo  "$now: > Executing atlas_dbToJson"
	echo -e "\nSinais de Transito\n" | python3 $modelDir/atlas_dbToJson.py > /home/atlas/logs_atlas_dbToJson.txt
	
	getCurrentTime
	echo  "$now: > Executing atlas_dbToTex"
	echo -e "\nSinais de Transito\n" | python3 $modelDir/atlas_dbToTex.py > /home/atlas/logs_atlas_dbToTex.txt
	
	getCurrentTime
	echo  "$now: > Executing pdflatex"
	cd $modelDir
	pdflatex -output-directory $dataDir $dataDir/"sinais_de_transito.tex" > /home/atlas/logs_pdflatex.txt
	rm $dataDir/*.tex $dataDir/*.aux 
	mv $dataDir/sinais_de_transito.csv $dataDir/catalog.csv
	mv $dataDir/sinais_de_transito.json $dataDir/catalog.json
	mv $dataDir/sinais_de_transito.pdf $dataDir/catalog.pdf	 
	
	getCurrentTime
	echo  "$now: > Copying files to "
	rm $dashboardDir/data/*	
	
	
	cp $dataDir/* $dashboardDir/data/

	getCurrentTime
	echo "$now: > Going to sleep 15s"	
	sleep 15
done


