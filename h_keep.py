#!/usr/bin/python

import os
import re

#select interface
def wtnick():

    iname=os.popen("cat /proc/net/dev")
    p=iname.read()
    list=open("nicname.txt","w")
    list.write(p)
    list.close()
    list=open("nicname.txt","r")
    np=0
    global niclist
    niclist=[]
    print("-network interface names select:\n ")
    for i in list.readlines():
        x=re.search("(\w+):",i)
        if(x):
            print(" +%s select %s"%(x.group(1),np))
            niclist.insert(np,x.group(1))
            np+=1
    list.close()
    global nic
    nic=int(raw_input("\n>>> "))


wtnick()
