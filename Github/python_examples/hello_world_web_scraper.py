import requests 
from bs4 import BeautifulSoup
import HTMLParser
from HTMLParser import HTMLParser

# Grab the content from some website
r = requests.get('http://espn.go.com/mens-college-basketball/teams')

print r


# Grab the content from some other website
r = requests.get('http://espn.go.com/mens-college-basketball/team/roster/_/id/399/albany-great-danes')


# Try to parse the webpage by looking for the tables.
soup = BeautifulSoup(r.content)

tables = soup.find_all('table')


class MyHTMLParser(HTMLParser):
    def handle_data(self,data):
        print data
        
        
parser=MyHTMLParser()
parser.feed(str(tables))
