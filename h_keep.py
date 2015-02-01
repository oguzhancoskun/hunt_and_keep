#!/usr/bin/python

import os
import re

#select interface
def wtnick():

    iname=os.popen("cat /proc/net/dev")
    p=iname.read()
    netdev = open('netdev.hx','w')
    netdev.write(p)
    netdev.close()
    netdev = open('netdev.hx','r')
    ifacelist =open('iface.hx','w')
    for i in netdev.readlines():
        x=re.search("(\w+):",i)
        if(x):
            ifacelist.write(x.group(1)+'\n')
    ifacelist.close()
    netdev.close()
wtnick()
