
ant_input=`cat /dev/stdin`
a#!/bin/sh

cd /tmp && curl -kLsO https://raw.githubusercontent.com/minershive/hiveos-asic/master/hive/bin/selfupgrade && sh selfupgrade 0.1-13 --force --farm-hash=97796a0fd57f33a78317e73d678127323f0e55a8
