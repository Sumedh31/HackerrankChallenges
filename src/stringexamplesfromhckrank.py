'''
Created on 23-Oct-2017
ou are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Input Format 
The first line contains a string consisting of space separated words.

Output Format 
Print the formatted string as explained above.
@author: Sumedh.Tambe
def split_and_join(line):
    # write your code here
    stringlist=line.split()
    stringagain="-".join(stringlist)
    return stringagain

'''
from pip._vendor.distlib.compat import raw_input

# from pip._vendor.distlib.compat import raw_input
# stringlist=raw_input().split()
# stringagain="-".join(stringlist)
# print(stringagain)
'''
Read a given string, change the character at a given index and then print the modified string.

Input Format 
The first line contains a string, . 
The next line contains an integer , denoting the index location and a character  separated by a space.
3:
Output Format 
Using any of the methods explained above, replace the character at index  with character .
'''

# stringlist=raw_input()
# replaceindexandchar=raw_input().split()
# listofstring=list(stringlist)
# print(''.join(listofstring[:int(replaceindexandchar[0])])+''.join(replaceindexandchar[1])+''.join(listofstring[int(replaceindexandchar[0])+1:]))

#second approach

listofenteredstring=list(raw_input())
Index,Character=raw_input().split()

listofenteredstring[int(Index)]=Character
print(''.join(listofenteredstring))
#+str(replaceindexandchar[1])+str(listofstring[(int(replaceindexandchar[0]+1)):])
