import math

def Chisq(data,data1,data2,data3,data4):

    chisq=0
    global a=float
    global b=float
    global c=float
    global d=float

    for i in range(len(data)):
        O=a*data1[i]+b*data2[i]+c*data3[i]+d*data4[i]
        E=data[i]
        chisq=chisq+(O-E)**2/E
        
