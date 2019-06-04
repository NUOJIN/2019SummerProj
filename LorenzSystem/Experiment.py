#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 14:55:11 2019

@author: nokicheng
"""

import numpy as np

#Input the x matrix, output the dictionary matrix A
#The matrix A should look like
#     1 x1 x2 x3 x1x1 x1x2 x1x3 x2x2 x2x3 x3x3
# A =        ... ... ... ... ... ... ...
#     1 x1 x2 x3 x1x1 x1x2 x1x3 x2x2 x2x3 x3x3
def constructMatrixA(finalSol):
    result = []
    for i in range(0,len(finalSol)):
        for j in range(0,len(finalSol[i])):
            result.append(constructRow(finalSol[i][j]))
    return np.array(result)
    

#Input an array, output the corresponding dictionary matrix row
def constructRow(x):
    x = np.append(1,x)
    l = len(x)
    result = []
    for i in range(0,l):
        for j in range(i,l):
            result.append(x[i]*x[j])
    return np.array(result)

#Input matrix finalDer, output the derivative matrix V
def constructMatrixV(finalDer):
    result = []
    for i in range(0,len(finalDer)):
        for j in range(0,len(finalDer[i])):
            result.append(finalDer[i][j])
    return np.array(result)