import math

def StandDev(data):

    N=len(data)
    sumX=0
    sumX2=0
    x=0
    x2=0
    for i in range(N):
        x=data[i]
        x2=data[i]**2
        sumX=sumX+x
        sumX2=sumX2+x2

    return math.sqrt((sumX2-sumX**2/N)/(N-1))


def mean(data):

    N=len(data)
    sumX=0

    for i in range(N):
        sumX=sumX+data[i]


    return sumX/N


def z_score(datapoint, mean, SD):
    
    z_score=(datapoint-mean)/SD

    return z_score
