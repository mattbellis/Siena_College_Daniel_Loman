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

import matplotlib.dates as mdates

################################################################################
# Example of a function
################################################################################
def corr_coef(x):

    cc = len(x)

    return cc


################################################################################

start=3

var0='TEAM'
passvar='RATE'      #COMP, PCT, YDS, YDS/A, LONG, TD, INT, SACK, YDSL, RATE, YDS/G
rushvar='YDS/A'      #ATT, YDS, YDS/A, LONG, TD, YDS/G, FUM, FUML

years=['2012','2011','2010','2009','2008','2007','2006','2005','2004','2002']      #2002-2012

passingstat=matrix([[0.0]*len(years)]*32)
rushingstat=matrix([[0.0]*len(years)]*32)
winpercent=matrix([[0.0]*len(years)]*32)

CorrCoef=matrix([[0.0]*2]*len(years))

# Use this for the scatter plots.
fig_passscatter = figure(figsize=(8,8))

for year in range(len(years)):

    #####################################################
    #            ####PASSING STATISTICS####             #
    #####################################################
    
    r=requests.get('http://espn.go.com/nfl/statistics/team/_/stat/passing/year/'+years[year])

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
    parser.feed(str(tables))
    b=parser.handle_data(str(tables))


    dataarray=["" for x in range(start,count-1)]
    for i in range(count-start-1):
        dataarray[i]=a[i+start]

    dataarray=array(dataarray)


    ncols=14
    nrows=32

    nvalues=len(dataarray)-ncols
    for i in range(ncols):
        if(dataarray[i]=='TEAM'):
            index0=i
        if(dataarray[i]==passvar):
            index1=i

    indexes=np.arange(0,nvalues,ncols)
    datamatrix=matrix([["      "]*2]*(nrows))
    datamatrix1=matrix([["      "]*2]*(nrows))

    c=np.delete(dataarray[indexes+index0],0,None)
    d=np.delete(dataarray[indexes+index1],0,None)

    for i in range(len(c)):
        datamatrix[i,0]=c[i]
        datamatrix[i,1]=d[i]

    count1=0
    for a in sorted(datamatrix[:,0]):
        for i in range(32):
            if(a==datamatrix[i,0]):
                datamatrix1[count1,:]=datamatrix[i,:]
                count1=count1+1
            

    passingstat[:,year]=datamatrix1[:,1]




    #####################################################   
    #            ####RUSHING STATISTICS####             #
    #####################################################


    r=requests.get('http://espn.go.com/nfl/statistics/team/_/stat/rushing/year/'+years[year])

    data=r.content

    soup=BeautifulSoup(data)

    tables=soup.find_all('table')

    a = ["" for x in range(6000)]

    count=0

    class MyHTMLParser(HTMLParser):

        def handle_data(self,data):
            global count
            #print data
            a[count]=data
            count = count + 1
       
        
    parser=MyHTMLParser()
    parser.feed(str(tables))
    b=parser.handle_data(str(tables))


    dataarray=["" for x in range(start,count-1)]
    for i in range(count-start-1):
        dataarray[i]=a[i+start]

    dataarray=array(dataarray)


    ncols=10
    nrows=32

    nvalues=len(dataarray)-ncols
    for i in range(ncols):
        if(dataarray[i]=='TEAM'):
            index0=i
        if(dataarray[i]==rushvar):
            index1=i

    indexes=np.arange(0,nvalues,ncols)
    datamatrix=matrix([["      "]*2]*(nrows))
    datamatrix1=matrix([["      "]*2]*(nrows))

    c=np.delete(dataarray[indexes+index0],0,None)
    d=np.delete(dataarray[indexes+index1],0,None)

    for i in range(len(c)):
        datamatrix[i,0]=c[i]
        datamatrix[i,1]=d[i]

    count1=0
    for a in sorted(datamatrix[:,0]):
        for i in range(32):
            if(a==datamatrix[i,0]):
                datamatrix1[count1,:]=datamatrix[i,:]
                count1=count1+1
            

    rushingstat[:,year]=datamatrix1[:,1]



    #####################################################   
    #               ####WIN PERCENTAGE####              #
    #####################################################



    r=requests.get('http://espn.go.com/nfl/standings/_/year/'+years[year])

    data=r.content

    soup=BeautifulSoup(data)

    tables=soup.find_all('table')

    a = ["" for x in range(6000)]

    count=0

    class MyHTMLParser(HTMLParser):

        def handle_data(self,data):
            global count
            #print data
            a[count]=data
            count = count + 1
       
        
    parser=MyHTMLParser()
    parser.feed(str(tables))
    b=parser.handle_data(str(tables))


    dataarray=["" for x in range(start,count-1)]
    for i in range(count-start-1):
        dataarray[i]=a[i+start]

    dataarray=array(dataarray)

    dataarray = dataarray[dataarray!='\n']
    dataarray = dataarray[dataarray!='American Football Conference']
    dataarray = dataarray[dataarray!='x - ']
    dataarray = dataarray[dataarray!='y - ']
    dataarray = dataarray[dataarray!='z - ']
    dataarray = dataarray[dataarray!='* - ']


    ncols=13
    nrows=32

    nvalues=len(dataarray)-ncols
    for i in range(ncols):
        if(dataarray[i]=='NFC EAST'):
            index0=i
        if(dataarray[i]=='PCT'):
            index1=i

    indexes=np.arange(0,nvalues,ncols)
    indexes1=np.arange(0,40,5)

    datamatrix=matrix([["      "]*2]*(nrows))
    datamatrix1=matrix([["      "]*2]*(nrows))

    c=dataarray[indexes+index0]
    c=np.delete(c,indexes1,None)

    d=dataarray[indexes+index1]
    d=np.delete(d,indexes1,None)


    for i in range(len(c)):
        datamatrix[i,0]=c[i]
        datamatrix[i,1]=d[i]

    count1=0
    for a in sorted(datamatrix[:,0]):
        for i in range(32):
            if(a==datamatrix[i,0]):
                datamatrix1[count1,:]=datamatrix[i,:]
                count1=count1+1


    winpercent[:,year]=datamatrix1[:,1]

    # Plot the individual years for passing
    fig_passscatter.add_subplot(4,4,year+1)
    print winpercent
    plot(winpercent[:,year],passingstat[:,year],'ko',markersize=5)





for year in range(len(years)):

    normalPassWin=matrix([[0.0]*2]*32)
    normalRushWin=matrix([[0.0]*2]*32)
    

    ### Datasets ###

    ave=matrix([[0.0]*3]*1)

    for i in range(32):
        ave[0,0]=ave[0,0]+passingstat[i,year]
        ave[0,1]=ave[0,1]+rushingstat[i,year]
        ave[0,2]=ave[0,2]+winpercent[i,year]

    ave=ave/32
    normalPassWin[:,0]=passingstat[:,year]-ave[0,0]
    normalPassWin[:,1]=winpercent[:,year]-ave[0,2]
    normalRushWin[:,0]=rushingstat[:,year]-ave[0,1]
    normalRushWin[:,1]=winpercent[:,year]-ave[0,2]

    CovPassWin=normalPassWin.T*normalPassWin
    CovRushWin=normalRushWin.T*normalRushWin

    CorrPassWin=matrix([[0.0]*len(CovPassWin)]*len(CovPassWin.T))
    CorrRushWin=matrix([[0.0]*len(CovRushWin)]*len(CovRushWin.T))



    for i in range(len(CovPassWin)):
        for j in range(len(CovPassWin.T)):
            CorrPassWin[i,j]=CovPassWin.T[i,j]/math.sqrt((CovPassWin.T[i,i]*CovPassWin.T[j,j]))

    CorrCoef[year,0]=CorrPassWin[0,1]

    for i in range(len(CovRushWin)):
        for j in range(len(CovRushWin.T)):
            CorrRushWin[i,j]=CovRushWin.T[i,j]/math.sqrt((CovRushWin.T[i,i]*CovRushWin.T[j,j]))
    
    CorrCoef[year,1]=CorrRushWin[0,1]

years2=array([0.0]*len(years)).astype('int')
for i in range(len(years)):
    years2[i]=float(years[i])


cc = corr_coef(years2)
print "cc: %d" % (cc)



fig = figure()
plot(years2,CorrCoef[:,0],'ko')
xlabel('year')
ylabel('Correlation Coefficient')
title('Correlation between pass '+ passvar +' and win percent')
fmt_xdata = mdates.DateFormatter('%Y')
fig.autofmt_xdate()
ylim(-1.0,1.0)
xlim(min(years2)-1,max(years2)+1)

figure()

plot(years2,CorrCoef[:,1],'ko')
xlabel('year')
ylabel('Correlation Coefficient')
title('Correlation between rush '+ rushvar + ' and win percent')
ylim(-1.0,1.0)
xlim(min(years2)-1,max(years2)+1)

show()
