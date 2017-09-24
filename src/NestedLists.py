from pip._vendor.distlib.compat import raw_input
list1=[]

for i in range(int(raw_input())):
    name=raw_input()
    score=float(raw_input())    
    list1.append([name,score])
    
lowest=float("inf") 
secondlowest=float("inf")

for index, i in enumerate(range(len(list1))):
    if(format(float(list1[index][1]),'.4f')<format(float(secondlowest),'.4f')):
        if(format(float(list1[index][1]),'.4f')<format(float(lowest),'.4f')):
            lowest,secondlowest=format(float(list1[index][1]),'.4f'),format(float(lowest),'.4f')
        else:
            secondlowest=format(float(list1[index][1]),'.4f')

#print(list1[index][0] for index, i in enumerate(range(len(list1))) if(float(list1[index][1])==float(secondlowest)))
list2=[] 
for index, i in enumerate(range(len(list1))):
    if(format(float(list1[index][1]),'.4f')==format(float(secondlowest),'.4f')):
        list2.append((list1[index][0]))
        
list2=sorted(list2,key=str.lower)
    
for index,i in enumerate(range(len(list2))):
    print(list2[index]) 