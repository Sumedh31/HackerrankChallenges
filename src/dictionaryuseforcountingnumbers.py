'''
Created on 23-Oct-2017

@author: Sumedh.Tambe
'''
from collections import Counter
listofnumbers=(1,2,1,3,4,1,2,4,5,4)
dic=Counter(listofnumbers)
# dictionary={}
# for numbers in listofnumbers:
#     if numbers in dictionary.keys():
#         
#         dictionary[numbers]=dictionary[numbers]+1
#         
#     else:
#         
#         dictionary[numbers]=1
#     #dictionary[numbers]=numbers
print(dic)