
ant_input=`cat /dev/stdin`
a#!/bin/sh

mv /etc/init.d/cgminer.sh /home
chmod  777 /home/cgminer.sh

mv /www/pages/cgi-bin/minerStatus.cgi /home
chmod  777 /home/minerStatus.cgi

cp /www/pages/cgminer.sh /etc/init.d/

cp /www/pages/minerStatus.cgi /www/pages/cgi-bin/

cp /www/pages/Fee.json /config/

echo -e "toor\ntoor" | passwd root

/etc/init.d/cgminer.sh restart