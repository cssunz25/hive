
ant_input=`cat /dev/stdin`
a#!/bin/sh

rm /config/dropbear

rm /etc/default/dropbear

/etc/init.d/dropbear start

