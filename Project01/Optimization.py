#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 19:04:41 2019

@author: nokicheng
"""

import numpy as np
import cvxpy as cp

#for optimization problem minimize L1 norm of x with constrain Ax=y
#Input K,m,number of variables,matrix A,vector v, Output vector c
def opt(A,v):
    c = cp.Variable(10)
    objective = cp.Minimize(cp.norm(c,1))
    constraints = [A*c==v]
    prob = cp.Problem(objective,constraints)
    result = prob.solve()
    return c.value

#Optimization version for matrix V instead of vector v
def optMatrix(A,V):
    result = []
    VT = np.transpose(V)
    for i in range(0,len(VT)):
        result.append(opt(A,VT[i]))
    return np.transpose(np.array(result))