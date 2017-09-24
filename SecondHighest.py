# '''
# Created on 11-Aug-2017
# 
# @author: Sumedh.Tambe
# '''
# import sys
# from pip._vendor.distlib.compat import raw_input
# n=int(raw_input())
# if(2<=n<=10):
#     inputitems= raw_input().split()
#     List=list(map(int,inputitems))
#     highest=0
#     secondhighest=0
#      
#     for index, item in enumerate(List):
#         if(-100<List[index]<100):
#             condition=True
#         else:
#             condition=False
#          
#     if(condition):
#         highestnum=max(List)
#         while(highestnum in List):
#             List.remove(highestnum)
#         secondhighest=max(List)
#         sys.stdout.write(str(secondhighest))
        
    
         
        
    
         
        
# n=int(raw_input())
# if(2<n<10):
#     inputitems= raw_input().split()
#     List=list(map(int,inputitems))    
highest=-100
secondhighest=-100   
List=(3,6,25)
for index, item in enumerate(List):
    print("listelement =" + str(List[index]))
    if(-100<List[index]<100):
         
        if(List[index]>=secondhighest):
                       
            if(List[index]>highest):
                
                highest,secondhighest=List[index],highest
            else:
                secondhighest=List[index]
         
#          else:
#              if(secondhighest<List[index]<highest):
#                  secondhighest=List[index]
# print("SH=" + str(secondhighest))  
#          if(secondhighest<List[index]):
#                  secondhighest=List[index]
#                  print("second"+ str(secondhighest))
#          else:
#              secondhighest=highest
#              print("second"+ str(secondhighest))
# #             
#             
#             
            
            
            