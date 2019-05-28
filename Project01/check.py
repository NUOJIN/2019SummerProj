#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 13:44:23 2019

@author: nokicheng
"""

import numpy as np

#input an array with length 3 and parameters 
#output the theoretical value of the derivatice of x1
def checkX1(x,p):
    return p[0]*x[1]-p[0]*x[0]

def checkX2(x,p):
    return p[1]*x[0]-x[0]*x[2]-x[1]

def checkX3(x,p):
    return x[0]*x[1]-p[2]*x[2]

def checkAll(x,p):
    x = np.transpose(x)
    return np.transpose([checkX1(x,p),checkX2(x,p),checkX3(x,p)])