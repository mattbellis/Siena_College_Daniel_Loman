import requests
from bs4 import BeautifulSoup
import re
import numpy as np
from numpy import linalg, matrix, array
import HTMLParser
from HTMLParser import HTMLParser
import math
import pylab
from pylab import *

r=requests.get('http://hoopdata.com/teamff.aspx')

data=r.content
soup=BeautifulSoup(data)
table=soup.find_all('table')

table1=table[6]

rows=table1.findAll('tr')

values=['Name', 'OffEff', 'DefEff', 'Diff', 'Own', 'Opp', 'Diff', 'Own', 'Opp', 'Diff',  'Own', 'Opp', 'Diff',  'Own', 'Opp', 'Diff']

TeamIndex=0
OEIndex=1
eFGIndex=4
FTRIndex=7
TORIndex=10
ORRIndex=13

teams=matrix([['    ']*1]*30)
teamStats=np.array([[0.0]*5]*30)

FTP=np.array([[0.0]*2]*30)

count=0

text_file=open('/Users/DanLo1108/Documents/AdvancedLab/Data Files/teams.txt','w')

for row in rows:
    if(count<31):
        columns=row.findAll('td')
        for i, column in enumerate(columns):
            if(count>0):
                if(i==TeamIndex):
                    teams[count-1,0]=column.text
                    text_file.write(column.text)
                    text_file.write('\n')
                if(i==OEIndex):
                    teamStats[count-1,0]=column.text
                if(i==eFGIndex):
                    teamStats[count-1,1]=column.text
                if(i==FTRIndex):
                    teamStats[count-1,2]=column.text
                if(i==TORIndex):
                    teamStats[count-1,3]=column.text
                if(i==ORRIndex):
                    teamStats[count-1,4]=column.text
        count=count+1

text_file.close()


r=requests.get('http://hoopdata.com/teamoffstats.aspx')

data=r.content
soup=BeautifulSoup(data)
table=soup.find_all('table')

table1=table[3]


rows=table1.findAll('tr')

count=0
for row in rows:
    if(count<31):
        columns=row.findAll('td')
        for i, column in enumerate(columns):
            if(count>0):
                if(i==2):
                    FTP[count-1,0]=column.text
                if(i==7):
                    FTP[count-1,1]=column.text
                    

        count=count+1
        
teamStats1=np.array([[0.0]*5]*30)

b=sorted(teamStats, key=lambda teamStats_entry: teamStats_entry[0])
a=sorted(FTP, key=lambda FTP_entry: FTP_entry[0])

FTParray=matrix([[0.0]*1]*30)


for i in range(30):
    j=29-i
    FTParray[i]=a[j][1]
    teamStats1[i,0]=b[j][0]
    teamStats1[i,1]=b[j][1]
    teamStats1[i,2]=b[j][2]
    teamStats1[i,3]=b[j][3]
    teamStats1[i,4]=b[j][4]

np.savetxt('/Users/DanLo1108/Documents/AdvancedLab/Data Files/FTP.txt',FTParray, delimiter='\t')
np.savetxt('/Users/DanLo1108/Documents/AdvancedLab/Data Files/teamStats.txt', teamStats1, delimiter="\t")
#np.savetxt('/Users/DanLo1108/Documents/AdvancedLab/Data Files/teams.txt', teams)
