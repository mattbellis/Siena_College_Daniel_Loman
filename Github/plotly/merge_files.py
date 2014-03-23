import sys
import numpy as np

file0 = open(sys.argv[1])
file1 = open(sys.argv[2])

for line0,line1 in zip(file0,file1):
    print line0.strip(),line1.strip()
