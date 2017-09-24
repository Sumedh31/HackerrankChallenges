'''
Created on 12-Sep-2017

@author: Sumedh.Tambe
'''
from pip._vendor.distlib.compat import raw_input


list1=[]

for i in range(int(raw_input())):
    name=raw_input()
    score=float(raw_input())    
    list1.append([name,score])
lowest=float("inf") 
secondlowest=float("inf")
for index, i in enumerate(range(len(list1))):
    if(format(float(list1[index][1]),'.2f')<format(float(secondlowest),'.2f')):
        if(format(float(list1[index][1]),'.2f')<format(float(lowest),'.2f')):
            lowest,secondlowest=format(float(list1[index][1]),'.2f'),format(float(lowest),'.2f')
        else:
            secondlowest=format(float(list1[index][1]),'.2f')

#print(list1[index][0] for index, i in enumerate(range(len(list1))) if(float(list1[index][1])==float(secondlowest)))
 
for index, i in enumerate(range(len(list1))):
    if(format(float(list1[index][1]),'.2f')==format(float(secondlowest),'.2f')):
        list2=[]
        list2.append((list1[index][0]))
        #list2=list2.sort()
        list2.sort()
        print(list2)
         
#     
    
    
#print(list1) 