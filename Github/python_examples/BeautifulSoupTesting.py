import requests
from bs4 import BeautifulSoup
import re
import numpy as np
from numpy import linalg, matrix, array
import HTMLParser
from HTMLParser import HTMLParser


start=2

r1=requests.get('http://espn.go.com/nfl/statistics/team/_/stat/passing/year/2012')
#r2.requests.get('http://www.nfl.com/stats/categorystats?archive=true&conference=null&role=TM&offensiveStatisticCategory=RUSHING&defensiveStatisticCategory=null&season=2012&seasonType=REG&tabSeq=2&qualified=false&Submit=Go')

data1=r1.content
#data2=r2.content

soup1=BeautifulSoup(data1)
#soup2=BeautifulSoup(data2)

tables1=soup1.find_all('table')
#tables2=soup2.find_all('table')

a1 = ["" for x in range(6000)]
global count
count=0

class MyHTMLParser(HTMLParser):
    
    def handle_data(self,data):
        global count
        #print data
        a1[count]=data
        count = count + 1
       
        
parser=MyHTMLParser()
parser.feed(str(tables1))
b=parser.handle_data(str(tables1))


dataarray=["" for x in range(start,count-1)]
for i in range(count-start-1):
    dataarray[i]=a1[i+start]

dataarray=array(dataarray)


ncols=14
nvalues=len(dataarray)-ncols
for i in range(ncols):
    if(dataarray[i]=='YDS'):
        index=i

indexes=np.arange(0,nvalues,ncols)
datamatrix=matrix([[0.0]*ncols]*32)

for i in range(ncols):
    datamatrix[:,i]=dataarray[indexes+i]
    


