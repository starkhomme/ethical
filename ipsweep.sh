#!/bin/bash
for ip in `seq 1 254`:
do 
ping -c 1 $1.$ip |grep '64 bytes'|awk '{print $4}'
echo $1.$ip
done
