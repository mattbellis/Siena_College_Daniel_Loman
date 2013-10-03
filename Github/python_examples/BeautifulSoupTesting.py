import requests
from bs4 import BeautifulSoup
import re
import numpy
from numpy import linalg, matrix, array
import HTMLParser
from HTMLParser import HTMLParser


start=3



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











