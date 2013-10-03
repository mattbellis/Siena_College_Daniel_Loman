import requests
from bs4 import BeautifulSoup
import re
import numpy
from numpy import linalg, matrix, array
import HTMLParser
from HTMLParser import HTMLParser

import numpy as np


start=2



r=requests.get('http://espn.go.com/nfl/statistics/player/_/stat/passing')

data1=r.content

soup=BeautifulSoup(data1)

tables=soup.find_all('table')

a = ["" for x in range(1000)]
global count
count=0

class MyHTMLParser(HTMLParser):
    
    def handle_data(self,data):
        global count
        print data
        a[count]=data
        count = count + 1
       
        
parser=MyHTMLParser()
parser.feed(str(tables))
b=parser.handle_data(str(tables))


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









