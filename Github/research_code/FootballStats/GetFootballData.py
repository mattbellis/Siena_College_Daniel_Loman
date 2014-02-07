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
import random

var0='TEAM'
passvar='Yds'      #Cmp, Att, Yds, TD, Int, NY/A, 1stD
rushvar='Yds'      #Att, Yds, TD, Y/A, 1stD
defpassvar='Yds'   #Cmp, Att, Yds, TD, Int, NY/A, 1stD
defrushvar='Yds'   #Att, Yds, TD, Y/A, 1stD


years=[0.0]*13  #enters desired number of years to analyze
j=0
for i in range(2000,2013):
    years[j]=str(i)
    j=j+1



datamatrix=matrix([['                       ']*2]*32)

totpassyards=matrix([[0.0]*len(years)]*32)
totrushyards=matrix([[0.0]*len(years)]*32)
totdefpassyards=matrix([[0.0]*len(years)]*32)
totdefrushyards=matrix([[0.0]*len(years)]*32)


fig_passscatter = figure(figsize=(8,8))

for year in range(len(years)):

    r1=requests.get('http://www.pro-football-reference.com/years/'+years[year])
    r2=requests.get('http://www.pro-football-reference.com/years/'+years[year]+'/opp.htm')

    data1=r1.content
    soup1=BeautifulSoup(data1)
    table1=soup1.find_all('table')

    data2=r2.content
    soup2=BeautifulSoup(data2)
    table2=soup2.find_all('table')

    if(float(years[year])<=2002):
        tab=6
    if(float(years[year])>2002):
        tab=9
    
    wintable=table1[0]
    offtable=table1[tab]
    deftable=table2[0]


    winrows=wintable.findAll('tr')
    offrows=offtable.findAll('tr')
    defrows=deftable.findAll('tr')

    #####################################################
    #               ####WIN PERCENTAGE####              #
    #####################################################
    

    values=['Tm', 'W', 'L', 'T','W-L%', 'Pts', 'PtsO','PtDef','MoV','SoS','SRS','OSRS','DSRS']

    val1='Tm'
    val2='W-L%'

    val_index1=values.index(val1)
    val_index2=values.index(val2)

    count=0

    for row in winrows:
        columns=row.findAll('td')
        for i, column1 in enumerate(columns):
            for j, column2 in enumerate(columns):
                if i==val_index1 and j== val_index2 and column1.text != val1 and column2.text != val2:
                    if(column1.text != '' and column2.text != ''):
                         datamatrix[count,0] = column1.text
                         datamatrix[count,1] = column2.text
                         count=count+1
                        
                         
    datamatrix1=matrix([["                     "]*2]*count)

    count1=0
    for a in sorted(datamatrix[:,0]):
        for i in range(len(datamatrix1)):
            if(a==datamatrix[i,0]):
                datamatrix1[count1,:]=datamatrix[i,:]
                count1=count1+1

    winpercent=matrix([[0.0]*len(years)]*len(datamatrix1))

    for i in range(len(datamatrix1)):
        winpercent[i,year]=float(datamatrix1[i,1])


    #####################################################
    #         ####PASSING/RUSHING YARDS####             #
    #####################################################

    values1=['Rk','Tm','G','Pts','Yds','Ply','Y/P','TO','FL','1stPy','1stD','Cmp','Att','Yds','TD','Int','NY/A','1stD','Att','Yds','TD','Y/A','1stD','Sc%','TO%','EXP']
    values2=['Rk','Tm','G','Pts','Yds','Ply','Y/P','1stD','Cmp','Att','Yds','TD','Int','NY/A','1stD','Att','Yds','TD','Y/A','1stD','Sc%','TO%','EXP']

    b=float(years[year])
    
    if(b>2000):
        values=values1
    if(b<=2000.0):
        values=values2


    val1='Tm'
    val2=passvar
    val3=rushvar

    val_index1=values.index(val1)
    val_index2=0
    val_index3=0

    for i in range(5,len(values)):
        if(val_index2==0):
            if(values[i]==val2):
                val_index2=i
        if(values[i]==val2 and val_index2 != i):
            val_index3=i

    count=0

    for row in offrows:
        columns=row.findAll('td')
        for i, column1 in enumerate(columns):
            for j, column2 in enumerate(columns):
                if i==val_index1 and j== val_index2 and column1.text != val1 and column2.text != val2:
                    if(column1.text != '' and column2.text != '' and column1.text != 'Avg Team' and column1.text != 'League Total' and column1.text != 'Avg Tm/G'):
                         datamatrix[count,0] = column1.text
                         datamatrix[count,1] = column2.text
                         count=count+1
                         

                         
    datamatrix1=matrix([["                    "]*2]*count)

    count1=0
    for a in sorted(datamatrix[:,0]):
        for i in range(len(datamatrix1)):
            if(a==datamatrix[i,0]):
                datamatrix1[count1,:]=datamatrix[i,:]
                count1=count1+1

    passingstat=matrix([[0.0]*1]*len(datamatrix1))

    for i in range(len(datamatrix1)):
        passingstat[i]=float(datamatrix1[i,1])

    count=0
    datamatrix=matrix([['                  ']*2]*32)
    
    for row in offrows:
        columns=row.findAll('td')
        for i, column1 in enumerate(columns):
            for j, column2 in enumerate(columns):
                if i==val_index1 and j== val_index3 and column1.text != val1 and column2.text != val3:
                    if(column1.text != '' and column2.text != '' and column1.text != 'Avg Team' and column1.text != 'League Total' and column1.text != 'Avg Tm/G'):
                         datamatrix[count,0] = column1.text
                         datamatrix[count,1] = column2.text
                         count=count+1
                         


    datamatrix1=matrix([["                  "]*2]*count)

    count1=0
    for a in sorted(datamatrix[:,0]):
        for i in range(len(datamatrix1)):
            if(a==datamatrix[i,0]):
                datamatrix1[count1,:]=datamatrix[i,:]
                count1=count1+1

    rushingstat=matrix([[0.0]*1]*len(datamatrix1))

    for i in range(len(datamatrix1)):
        rushingstat[i]=float(datamatrix1[i,1])


    #####################################################
    #                  ####DEFENSE####                  #
    #####################################################

     
    val1='Tm'
    val2=defpassvar
    val3=defrushvar

    val_index1=values.index(val1)
    val_index2=0
    val_index3=0

    for i in range(5,len(values)):
        if(val_index2==0):
            if(values[i]==val2):
                val_index2=i
        if(values[i]==val2 and val_index2 != i):
            val_index3=i

    count=0

    for row in defrows:
        columns=row.findAll('td')
        for i, column1 in enumerate(columns):
            for j, column2 in enumerate(columns):
                if i==val_index1 and j== val_index2 and column1.text != val1 and column2.text != val2:
                    if(column1.text != '' and column2.text != '' and column1.text != 'Avg Team' and column1.text != 'League Total' and column1.text != 'Avg Tm/G'):
                         datamatrix[count,0] = column1.text
                         datamatrix[count,1] = column2.text
                         count=count+1

                         
    datamatrix1=matrix([["                  "]*2]*count)

    count1=0
    for a in sorted(datamatrix[:,0]):
        for i in range(len(datamatrix1)):
            if(a==datamatrix[i,0]):
                datamatrix1[count1,:]=datamatrix[i,:]
                count1=count1+1

    defpassingstat=matrix([[0.0]*1]*len(datamatrix1))

    for i in range(len(datamatrix1)):
        defpassingstat[i]=float(datamatrix1[i,1])

    count=0
    datamatrix=matrix([['                  ']*2]*32)
    
    for row in defrows:
        columns=row.findAll('td')
        for i, column1 in enumerate(columns):
            for j, column2 in enumerate(columns):
                if i==val_index1 and j== val_index3 and column1.text != val1 and column2.text != val3:
                    if(column1.text != '' and column2.text != '' and column1.text != 'Avg Team' and column1.text != 'League Total' and column1.text != 'Avg Tm/G'):
                         datamatrix[count,0] = column1.text
                         datamatrix[count,1] = column2.text
                         count=count+1


    datamatrix1=matrix([["                  "]*2]*count)

    count1=0
    for a in sorted(datamatrix[:,0]):
        for i in range(len(datamatrix1)):
            if(a==datamatrix[i,0]):
                datamatrix1[count1,:]=datamatrix[i,:]
                count1=count1+1

    defrushingstat=matrix([[0.0]*1]*len(datamatrix1))

    for i in range(len(datamatrix1)):
        defrushingstat[i]=float(datamatrix1[i,1])

    totpassyards[:,year]=passingstat
