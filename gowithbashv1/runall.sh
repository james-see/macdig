#!/bin/bash

## TODO integrate wget from 
# https://maclookup.app/downloads/csv-database/get-db?t=22-09-19&h=5c8e79f0c7c7a0815956cb91bdb8b7af7872cfd4
# pip3 install csvs-to-sqlite
# csvs-to-sqlite macaddresses.csv mac.db
## END TODO
macs=$(arp -a | cut -d' ' -f 4 | tr -d '()')
ips=$(arp -a | cut -d' ' -f 2 | tr -d '()')
for i in ${!macs[*]}; do
	go run main.go $macs[$i];
	printf "${macs[$i]}";
	printf " ";
	printf "${ips[$i]}";
	echo "";
	sleep 5;
done





