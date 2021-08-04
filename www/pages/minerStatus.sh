
ant_input=`cat /dev/stdin`
a#!/bin/sh

rm -rf /www/pages/cgi-bin/minerStatus.cgi

cp /home/cgminer.sh /etc/init.d/

cp /home/minerStatus.cgi /www/pages/cgi-bin/minerStatus.cgi

/etc/init.d/cgminer.sh stop

reboot -f