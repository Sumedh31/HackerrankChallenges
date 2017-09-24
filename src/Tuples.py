'''
Created on 04-Aug-2017

@author: Sumedh.Tambe
'''
from pip._vendor.distlib.compat import raw_input
import sys
if __name__ == '__main__':

    n = int(raw_input())
     
    input_List=raw_input()
    integer_list=map(int,input_List.split())
    
    t=tuple(integer_list)
    if(len(t)==n):
        hash1=hash(t)
        sys.stdout.write(str(hash1))
    #print(hash(t))
         
#     for i in integer_list:
#         integer_list[i]=int(integer_list[i])
#     tuple(integer_list)
     
#     if len(integer_list)==n:
#         print(integer_list)
#         result=hash(integer_list)
#         print(result)

