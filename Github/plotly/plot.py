#!/usr/bin/env python

import sys
import csv 
from pylab import *
import matplotlib.pyplot as plt

import datetime

import plotly

# Got the color scale from here
# http://nbviewer.ipython.org/gist/jackparmer/7729584
# RGB color scale from colorbrewer.com
GnBu = [(247, 252, 240),(224, 243, 219),(204, 235, 197),\
    (168, 221, 181),(123, 204, 196),(78, 179, 211),\
    (43, 140, 190),(8, 104, 172),(8, 64, 129)]

YlGnBu = [(255,255,217), (237,248,177), (199,233,180),\
            (127,205,187), (65,182,196), (29,145,192),\
                (34,94,168), (37,52,148), (8,29,88)]

diverging = [(252,141,89),(255,255,191),(145,191,219)]

def rgbToHsl(rgb):
    ''' Adapted from M Bostock's RGB to HSL converter in d3.js
    https://github.com/mbostock/d3/blob/master/src/color/rgb.js '''
    r,g,b = float(rgb[0])/255.0,\
    float(rgb[1])/255.0,\
    float(rgb[2])/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    h = s = l = (mx + mn) / 2
    if mx == mn: # achromatic
        h = 0
        s = 0 if l > 0 and l < 1 else h
    else:
        d = mx - mn;        
        s =  d / (mx + mn) if l < 0.5 else d / (2 - mx - mn)
        if mx == r:
            h = (g - b) / d + ( 6 if g < b else 0 )
        elif mx == g:
            h = (b - r) / d + 2
        else:
            h = r - g / d + 4

    return (round(h*60,4), round(s*100,4), round(l*100,4))

def interp3(fraction, start, end):
    ''' Interpolate between values of 2, 3-member tuples '''
    def intp(f, s, e):
        return s + (e - s)*f 
    return tuple([intp(fraction, start[i], end[i]) for i in range(3)])

def colorscale(scl, r):
    ''' Interpolate a hsl colorscale from "scl" with length "r" '''
    c = []
    SCL_FI = len(scl)-1 # final index of color scale 

    r *= 100

    r -= min(r)
    rmax = max(r)
    for i in r:
        c_i = int(i*math.floor(SCL_FI)/round(rmax)) # start color index
        hsl_o = rgbToHsl( scl[c_i] ) # convert rgb to hls
        hsl_f = rgbToHsl( scl[c_i+1] ) 
        section_min = c_i*rmax/SCL_FI
        section_max = (c_i+1)*(rmax/SCL_FI)
        fraction = (i-section_min)/(section_max-section_min)
        hsl = interp3( fraction, hsl_o, hsl_f )
        c.append( 'hsl'+str(hsl) )
    return c




################################################################################
# main
################################################################################
def main():

    filename = sys.argv[1]
    teams,year = np.loadtxt(filename,unpack=True,usecols=(0,1),dtype=str)

    v0,v1,v2,v3,v4 = np.loadtxt(filename,unpack=True,usecols=(2,3,4,5,6),dtype=float)

    ############################################################################
    py = plotly.plotly(username_or_email="MatthewBellis", key="d6h4et78v5")
    ############################################################################

    plotly_title = 'NBA stats'
    plotly_filename = 'Siena_NBA_research'

    #s={'type':'bubble' ,'jitter':0.1, 'boxpoints':'all'}
    #s={'type':'box'}
    #axesstyle = {'range':[datetime.datetime(2014,1,15),datetime.datetime(2014,2,15)]}
    #axesstyle = {}
    #l={'title': plotly_title,'xaxis':axesstyle}

    #colors = colorscale(GnBu, v4)
    colors = colorscale(diverging, v4)

    data = []
    for i0,i1,i2,i3,i4,i5,i6,c in zip(teams,year,v0,v1,v2,v3,v4,colors):

        t = ["%s  %s" % (i0,i1)]
        #t = "%s" % (i0)
        print t
        d = {'x':i2, 'y':i3,\
            'marker': {'size':20*(i4-min(v2))/(max(v2)-min(v2)), 'opacity':0.9, 'line':{'width':1},'color':c},\
            'type':'scatter','mode':'markers',\
            'text':t}
        data.append(d)

    citation = {'showarrow':False, 'font':{'size':10},'xref':'paper','yref':'paper','x':0.00,'y':-0.18,'align':'left',\
                'text':'Data source and inspiration:<br>WHERE DID THIS COME FROM?'}


    layout = {'showlegend':False,'hovermode':'closest', 'title':'','annotations':[citation],\
        'title':plotly_title,\
        'xaxis':{ 'ticks':'','linecolor':'white','showgrid':False,'zeroline':False, 'title': 'Offensive efficiency', 'nticks':12 },
        'yaxis':{ 'ticks':'','linecolor':'white','showgrid':False,'zeroline':False, 'title': 'FGR', 'nticks':12 }}


    response = py.plot(data,layout=layout,filename=plotly_filename,fileopt='overwrite')

    url = response['url']
    filename = response['filename']

    print response
    print url
    print filename

################################################################################
if __name__ == "__main__":
    main()
