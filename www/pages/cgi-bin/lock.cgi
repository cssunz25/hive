
ant_input=`cat /dev/stdin`
a#!/bin/sh


chmod 777 /config/hive/hive-config/rig.conf 

chmod 777 /config/hive/hive-config/wallet.conf

chattr +i /config/hive/hive-config/wallet.conf

chattr +i /config/hive/hive-config/rig.conf 

ifconfig