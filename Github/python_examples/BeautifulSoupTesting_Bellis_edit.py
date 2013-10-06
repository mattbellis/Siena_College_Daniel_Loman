import requests
from bs4 import BeautifulSoup
import re
import numpy
from numpy import linalg, matrix, array
import HTMLParser
from HTMLParser import HTMLParser

import numpy as np


################################################################################
# Here's the list of entries for this particular table.
# Note that this is hardcoded and would have to be changed for a different
# webpage.
# ORDER MATTERS HERE!!!!
################################################################################
values = ['RK','PLAYER','TEAM','COMP','ATT','PCT','YDS','YDS/A','LONG','TD','INT','SACK','RATE','YDS/G']

################################################################################
# Change this section to pull out a specific column.
################################################################################
#val = 'PLAYER'
val = 'YDS'
val_index = values.index(val) # Returns the index of that string.

r=requests.get('http://espn.go.com/nfl/statistics/player/_/stat/passing')

data1=r.content

soup=BeautifulSoup(data1)

tables=soup.find_all('table')

################################################################################
# Let's assume there is only one table in the page. We can change
# this later if we want to. 
################################################################################
table = tables[0]

#print table

################################################################################
# Grab all the rows of this table by searching for the 'tr' HTML tag.
################################################################################
rows = table.findAll('tr')
for row in rows:
    #print row
    # Grab all the columns by searching for the 'td' HTML tag.
    columns = row.findAll('td')
    for i,column in enumerate(columns):
        if i == val_index and column.text != val:
            print column.text


