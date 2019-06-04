#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 19:04:41 2019

@author: nokicheng
"""

import numpy as np
import cvxpy as cp
import scipy.optimize as op

#for optimization problem minimize L1 norm of x with constrain Ax=y
#Input K,m,number of variables,matrix A,matrix V, Output matrix C
def opt(A,v):
    c = cp.Variable(10)
    objective = cp.Minimize(cp.norm(c,1)+cp.norm(A*c-v))
    constraints = []
    prob = cp.Problem(objective,constraints)
    prob.solve(verbose=True)
    return c.value

#Optimization version for matrix V instead of vector v
def optMatrix(A,V):
    result = []
    VT = np.transpose(V)
    for i in range(0,len(VT)):
        result.append(opt(A,VT[i]))
    return np.transpose(np.array(result))

def optM(A,V):
    C = cp.Variable((10,3))
    objective = cp.Minimize(cp.norm(C,1))
    constraints = [cp.norm(A*C-V)<=1]
    prob = cp.Problem(objective,constraints)
    prob.solve()
    return C.value