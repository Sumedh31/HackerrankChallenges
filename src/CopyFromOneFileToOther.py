'''
Created on 11-Oct-2017

@author: Sumedh.Tambe
'''
inputfile=open("D:\Input.txt")
inputdata=inputfile.read()
inputfile.close()

outputfile=open("D:\Output.txt","a")
outputfile.truncate()
#outputfile.write(inputdata)
outputfile.close()
