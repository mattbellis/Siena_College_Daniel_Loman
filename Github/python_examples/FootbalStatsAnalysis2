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

import matplotlib.dates as mdates


start=3

var0='TEAM'
passvar='SACK'      #COMP, PCT, YDS, YDS/A, LONG, TD, INT, SACK, YDSL, RATE, YDS/G
rushvar='YDS'      #ATT, YDS, YDS/A, LONG, TD, YDS/G, FUM, FUML
defpassvar='YDS/A'   #COMP, PCT, YDS, YDS/A, LONG, TD, INT, SACK, YDSL, RATE, YDS/G
defrushvar='TD'   #ATT, YDS, YDS/A, LONG, TD, YDS/G, FUM, FUML
advancedvar='TOTAL QBR'         #PASS EPA, RUN EPA, SACK EPA, PEN EPA, TOTAL EPA, ACT PLAYS, QB PAR, QB PAA, TOTAL QBR

years=['2010']#,'2009','2008','2007', '2005'] #,'2006'] #,'2005','2004','2003','2002']      #2002-2012

passingstat=matrix([[0.0]*len(years)]*32)
rushingstat=matrix([[0.0]*len(years)]*32)
defpassingstat=matrix([[0.0]*len(years)]*32)
defrushingstat=matrix([[0.0]*len(years)]*32)
advancedstat=matrix([[0.0]*len(years)]*32)

winpercent=matrix([[0.0]*len(years)]*32)

N=1000

CorrCoef=matrix([[0.0]*5]*len(years))
global CorrCoef1




################################################################################

# Use this for the scatter plots.
fig_passscatter = figure(figsize=(8,8))

for year in range(len(years)):

    #####################################################
    #               ####WIN PERCENTAGE####              #
    #####################################################
    
    r=requests.get('http://www.pro-football-reference.com/years/'+years[year])

    data=r.content

    soup=BeautifulSoup(data)

    tables=soup.find_all('table')

    a = ["" for x in range(6000)]

    global count
    count=0

    class MyHTMLParser(HTMLParser):

        def handle_data(self,data):
            global count
            #print data
            a[count]=data
            count = count + 1
       
        
    parser=MyHTMLParser()
    parser.feed(str(tables[0]))
    b=parser.handle_data(str(tables[0]))



    
    dataarray=["" for x in range(1096)]
    for i in range(1096):
        dataarray[i]=a[i]

 
    count1=0
    for i in range(len(dataarray)-1):
        if (dataarray[count1]=='\n'):
            del(dataarray[count1])
        
        else:
            count1=count1+1

    dataarray=array(dataarray)

    dataarray = dataarray[dataarray!=' AFC East']
    dataarray = dataarray[dataarray!=' AFC North']        
    dataarray = dataarray[dataarray!=' AFC South']
    dataarray = dataarray[dataarray!=' AFC West']
    dataarray = dataarray[dataarray!=' NFC East']
    dataarray = dataarray[dataarray!=' NFC North']
    dataarray = dataarray[dataarray!=' NFC South']
    dataarray = dataarray[dataarray!=' NFC West']

    ncols=13
    nrows=32

    nvalues=len(dataarray)-ncols
    for i in range(ncols):
        if(dataarray[i]=='Tm'):
            index0=i
        if(dataarray[i]=='W-L%'):
            index1=i

    indexes=np.arange(0,nvalues,ncols)
    datamatrix=matrix([["      "]*2]*(nrows))
    datamatrix1=matrix([["      "]*2]*(nrows))

    c=np.delete(dataarray[indexes+index0],0,None)
    d=np.delete(dataarray[indexes+index1],0,None)

    for i in range(len(c)):
        if(i<16):
            datamatrix[i,0]=c[i]
            datamatrix[i,1]=float(d[i])
        if(i>16):
            datamatrix[i-1,0]=c[i]
            datamatrix[i-1,1]=float(d[i])

    count2=0
    for a in sorted(datamatrix[:,0]):
        for i in range(32):
            if(a==datamatrix[i,0]):
                datamatrix1[count2,:]=datamatrix[i,:]
                if(count2<31):
                    count2=count2+1
            
    for i in range(len(datamatrix1)):
        winpercent[i,year]=float(datamatrix1[i,1])
        


    #####################################################
    #         ####PASSING/RUSHING YARDS####             #
    #####################################################


    a = ["" for x in range(6000)]

    global count
    count=0


    class MyHTMLParser(HTMLParser):

        def handle_data(self,data):
            global count
            #print data
            a[count]=data
            count = count + 1
       
        
    parser=MyHTMLParser()
    parser.feed(str(tables[8]))
    b=parser.handle_data(str(tables[8]))




    dataarray=["" for x in range(1800)]
    for i in range(1800):
        dataarray[i]=a[i]

 
    count1=0
    for i in range(len(dataarray)-1):
        if (dataarray[count1]=='\n'):
            del(dataarray[count1])
        else:
            count1=count1+1


    for i in range(4):
        del(dataarray[0])

    dataarray=array(dataarray)

    ncols=26
    nrows=32

    nvalues=len(dataarray)-ncols

    index0=1
    index1=13
    index2=19

    indexes=np.arange(0,nvalues,ncols)
    datamatrix=matrix([["            "]*2]*(nrows))
    datamatrix1=matrix([["            "]*2]*(nrows))

    c=np.delete(dataarray[indexes+index0],0,None)
    d=np.delete(dataarray[indexes+index1],0,None)

    for i in range(len(c)):
        datamatrix[i,0]=c[i]
        datamatrix[i,1]=float(d[i])
        

    count2=0
    for a in sorted(datamatrix[:,0]):
        for i in range(32):
            if(a==datamatrix[i,0]):
                datamatrix1[count2,:]=datamatrix[i,:]
                if(count2<31):
                    count2=count2+1
            
    for i in range(len(datamatrix1)):
        passingstat[i,year]=float(datamatrix1[i,1])



    indexes=np.arange(0,nvalues,ncols)
    datamatrix=matrix([["      "]*2]*(nrows))
    datamatrix1=matrix([["      "]*2]*(nrows))

    c=np.delete(dataarray[indexes+index0],0,None)
    d=np.delete(dataarray[indexes+index2],0,None)

    for i in range(len(c)):
        datamatrix[i,0]=c[i]
        datamatrix[i,1]=float(d[i])


    count2=0
    for a in sorted(datamatrix[:,0]):
        for i in range(32):
            if(a==datamatrix[i,0]):
                datamatrix1[count2,:]=datamatrix[i,:]
                if(count2<31):
                    count2=count2+1
            
    for i in range(len(datamatrix1)):
        rushingstat[i,year]=float(datamatrix1[i,1])    




    #####################################################
    #                  ####DEFENSE####                  #
    #####################################################

    


    r=requests.get('http://www.pro-football-reference.com/years/'+years[year]+'/opp.htm')

    data=r.content

    soup=BeautifulSoup(data)

    tables=soup.find_all('table')

    a = ["" for x in range(6000)]

    global count
    count=0


    a = ["" for x in range(6000)]

    global count
    count=0


    class MyHTMLParser(HTMLParser):

        def handle_data(self,data):
            global count
            #print data
            a[count]=data
            count = count + 1
       
        
    parser=MyHTMLParser()
    parser.feed(str(tables[0]))
    b=parser.handle_data(str(tables[0]))




    dataarray=["" for x in range(1800)]
    for i in range(1800):
        dataarray[i]=a[i]

 
    count1=0
    for i in range(len(dataarray)-1):
        if (dataarray[count1]=='\n'):
            del(dataarray[count1])
        else:
            count1=count1+1


    for i in range(4):
        del(dataarray[0])

    dataarray=array(dataarray)

    dataarray = dataarray[dataarray!='Sc%']
    dataarray = dataarray[dataarray!='TO%']

    ncols=24
    nrows=32

    nvalues=len(dataarray)-ncols

    index0=1
    index1=13
    index2=19

    indexes=np.arange(0,nvalues,ncols)
    datamatrix=matrix([["            "]*2]*(nrows))
    datamatrix1=matrix([["            "]*2]*(nrows))

    c=np.delete(dataarray[indexes+index0],0,None)
    d=np.delete(dataarray[indexes+index1],0,None)

    for i in range(32):
        datamatrix[i,0]=c[i]
        datamatrix[i,1]=float(d[i])
        

    count2=0
    for a in sorted(datamatrix[:,0]):
        for i in range(32):
            if(a==datamatrix[i,0]):
                datamatrix1[count2,:]=datamatrix[i,:]
                if(count2<31):
                    count2=count2+1
            
    for i in range(len(datamatrix1)):
        defpassingstat[i,year]=float(datamatrix1[i,1])



    indexes=np.arange(0,nvalues,ncols)
    datamatrix=matrix([["      "]*2]*(nrows))
    datamatrix1=matrix([["      "]*2]*(nrows))

    c=np.delete(dataarray[indexes+index0],0,None)
    d=np.delete(dataarray[indexes+index2],0,None)

    for i in range(32):
        datamatrix[i,0]=c[i]
        datamatrix[i,1]=float(d[i])


    count2=0
    for a in sorted(datamatrix[:,0]):
        for i in range(32):
            if(a==datamatrix[i,0]):
                datamatrix1[count2,:]=datamatrix[i,:]
                if(count2<31):
                    count2=count2+1
            
    for i in range(len(datamatrix1)):
        defrushingstat[i,year]=float(datamatrix1[i,1])


        
