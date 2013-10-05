import requests
from bs4 import BeautifulSoup
import re
import numpy
from numpy import linalg, matrix, array
import HTMLParser
from HTMLParser import HTMLParser

import numpy as np


start=2



r1=requests.get('http://www.nfl.com/stats/categorystats?archive=true&conference=null&role=TM&offensiveStatisticCategory=TEAM_PASSING&defensiveStatisticCategory=null&season=2012&seasonType=REG&tabSeq=2&qualified=false&Submit=Go')
#r2.requests.get('http://www.nfl.com/stats/categorystats?archive=true&conference=null&role=TM&offensiveStatisticCategory=RUSHING&defensiveStatisticCategory=null&season=2012&seasonType=REG&tabSeq=2&qualified=false&Submit=Go')

data1=r1.content
#data2=r2.content

soup1=BeautifulSoup(data1)
#soup2=BeautifulSoup(data2)

tables1=soup1.find_all('table')
#tables2=soup2.find_all('table')

a1 = ["" for x in range(1000)]
global count
count=0

class MyHTMLParser(HTMLParser):
    
    def handle_data(self,data):
        global count
        print data
        a1[count]=data
        count = count + 1
       
        
parser=MyHTMLParser()
parser.feed(str(tables1))
b=parser.handle_data(str(tables1))


dataarray=["" for x in range(start,count-1)]
for i in range(count-start-1):
    dataarray[i]=a[i+start]


ncolumns = 14
nvalues = len(dataarray)

index = np.arange(0,nvalues,ncolumns)
print index

dataarray = array(dataarray)
dataarray = dataarray[dataarray!='\xc2\xa0']
print dataarray


print dataarray[index]
print dataarray[index+1]
print dataarray[index+2]









