#!/bin/bash
macs=$(arp -a | cut -d' ' -f 4 | tr -d '()')
ips=$(arp -a | cut -d' ' -f 2 | tr -d '()')
declare -i j
j=0
for i in $macs
do	
	go run main.go $i;
	printf $i;
	printf " ";
	printf $ips[$j];
	echo "";
	sleep 5;
done



