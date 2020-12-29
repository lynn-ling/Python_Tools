#!/bin/bash

port=5001
tag=default

while getopts f:h:p:t:w: opt;
do
case $opt in
    p) port=$OPTARG
    ;;
    t) tag=$OPTARG
    ;;
    ?) echo "$opt is an invalid option"
    ;;
esac
done



nohup python3 main.py -p $port -t $tag >/data01/test-target-tool/output-$port.log 2>&1 & echo $! > /data01/test-target-tool/command.pid

