'''
Created on 04-Aug-2017

@author: Sumedh.Tambe
'''
from pip._vendor.distlib.compat import raw_input
import sys

How_many_inputs= int(raw_input())
number=0
d={}

#print(d['Krishna'][0])
if ((How_many_inputs<=10) & (How_many_inputs >=2)):
    while(number<=How_many_inputs):
    
        record=raw_input()
        recordlist=record.split()
        if(number<How_many_inputs):
            if ((0<=float(recordlist[1])<=100) & (0<=float(recordlist[2])<=100) & (0<=float(recordlist[3])<=100)):
                d[recordlist[0]]=[float(recordlist[1]),float(recordlist[2]),float(recordlist[3])]
            else:
                print("Wrong marks given")
        
        else:
            if recordlist[0] in d.keys():
                #print(recordlist[0])
                Average=float((d[recordlist[0]][0]+d[recordlist[0]][1]+d[recordlist[0]][2])/3)
                Average=format(Average,'.2f')
               
                sys.stdout.write(str(Average))
        number=number+1
    #print(d[recordlist[0]][1])
    