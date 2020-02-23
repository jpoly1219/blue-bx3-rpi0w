#! /usr/bin/bash

while true
do
    PROCESSNAME=`ps -f | grep "python3 testing.py"`
    echo $PROCESSNAME
done