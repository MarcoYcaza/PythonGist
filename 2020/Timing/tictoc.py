#!/usr/bin/env python3
import time 
import numpy as np

a = np.random.rand(100000)
b = np.random.rand(100000)

tic = time.time()
c = np.dot(a,b)
toc = time.time()

print("elapsed time is :"+ str(1000*(toc- tic))+"ms")

