'''
Created on 27-Oct-2017

@author: Sumedh.Tambe
'''
from pip._vendor.distlib.compat import raw_input
from collections import Counter

Number_OfShoes_Available=int(raw_input())
if(0<Number_OfShoes_Available<10**3):
    List_OF_Size=list(map(int,raw_input().split()))
    dic=Counter(List_OF_Size)
Number_Of_Customers=int(raw_input())

def getRaghusIncome(Number_Of_Customers,dic):
    RaghusMoney=0
    if(0<Number_Of_Customers<=10**3):
        for customers in range(Number_Of_Customers):
            list1=list(map(int,raw_input().split()))
            if list1[0] in dic.keys():
                if not dic[list1[0]]==0:
                    RaghusMoney=RaghusMoney+list1[1]
                    dic[list1[0]]=dic[list1[0]]-1
        return RaghusMoney
    
print(getRaghusIncome(Number_Of_Customers,dic))

                
                