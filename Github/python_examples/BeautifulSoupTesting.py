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

class MyHTMLParser(HTMLParser):
    def handle_data(self,data):
        #print data
        
        
parser=MyHTMLParser()
parser.feed(str(tables))
