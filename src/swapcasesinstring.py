'''
Created on 20-Oct-2017

@author: Sumedh.Tambe
'''
from pip._vendor.distlib.compat import raw_input

try:
    list1=list(raw_input())
    #list1=list(stringinput)
    #print(list1)
    list2=[]
    for index, char in enumerate(range(len(list1))):    
        if(97<=ord(list1[index])<=122):        
            #strin=''.join(str(list1[index]).upper())
            list2.append(str(list1[index]).upper()) 
        elif(65<=ord(list1[index])<=90):
            #strin=''.join(str(list1[index]).lower())
            list2.append(str(list1[index]).lower()) 
        else:
            list2.append(str(list1[index]))
    print("".join(str(x) for x in list2))
except EOFError:
    print("error")