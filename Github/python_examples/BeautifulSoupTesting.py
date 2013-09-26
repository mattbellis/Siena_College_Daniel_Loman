import requests
from bs4 import BeautifulSoup
import re
import numpy
from numpy import linalg, matrix
import HTMLParser
from HTMLParser import HTMLParser

r=requests.get('http://espn.go.com/nfl/statistics/player/_/stat/passing')

data=r.content

soup=BeautifulSoup(data)
count=0

tables=soup.find_all('table')
print tables

class MyHTMLParser(HTMLParser):
    def handle_data(self,data):
        print "data: ",data
        #print len(data)
        
        
parser=MyHTMLParser()
print parser
parser.feed(str(tables))
