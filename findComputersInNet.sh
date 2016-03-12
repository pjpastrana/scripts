#! /bin/bash

for i in 192.168.1.{1..10}
do
    if ping -c1 -w1 $i &>/dev/null
    then
        echo $i is up
    fi
done
