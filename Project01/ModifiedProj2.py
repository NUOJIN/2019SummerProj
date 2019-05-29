#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 13:06:40 2019

@author: nokicheng
"""

import numpy as np
from scipy.integrate import odeint
import check
import matplotlib.pyplot as plt
from random import randint
import Experiment
import Optimization
import Graph

#function that returns dy/dt
def model(y,t,sigma,rho,beta):
    x1,x2,x3 = y
    dydt = [-sigma*x1+sigma*x2,rho*x1-x1*x3-x2,x1*x2-beta*x3]
    return dydt

def SolveEq(sigma,rho,beta,y0,m,period):
    #time points
    t = np.linspace(0,period,m)

    #solve ODE
    sol = odeint(model,y0,t,args=(sigma,rho,beta))
    return (sol,t)

def InitialGenerator(p):
    #p is the precision
    return [randint(-p,p)/p,randint(-p,p)/p,randint(-p,p)/p]

def getGradient(X,m,period):
    #Input matrix X and return xs' derivative
    #The precision of derivetive depends on the value of m
    result = []
    for i in range(0,len(X)-1):
        row = []
        for j in range(0,3):
            row.append((X[i+1,j]-X[i,j])/(period/m))
        result.append(np.array(row))
    return np.array(result)

def checkDer(finalDer,finalSol,p):
    #To compare calculated derivative and theoretical derivative
    print('The calculated derivative matrix is:')
    print(finalDer)
    print('The theoretical derivative matrix is:')
    theoretical = check.checkAll(finalSol,p)
    print(theoretical)
    print('The error matrix is:')
    print((finalDer-theoretical)/theoretical)

def burst(sigma,rho,beta,m,period):
    #create K bursts and m samples with given sigma,rho,beta
    #Obtain the solution by precision = 100
    (sol,t) = SolveEq(sigma,rho,beta,InitialGenerator(100),m+1,period)
    der = getGradient(sol,m,period)
    sol = sol[:-1,:]
    return (np.array(sol),np.array(der),t[:-1])

def chopUp(u,l,m,t):
    #Input a matrix u with shape 5 by K*m by 6 as well as its corresponding time
    #Output a matrix with shape K by 5 by m by 6 as well as corresponding time
    #The chop starts from position l, l < K*m and l >= 0
    result = []
    time = []
    h = np.concatenate((u,u),axis=0)
    ti = np.concatenate((t,t),axis=0)
    for i in range(0,K):
        result.append(h[l+i*m:l+i*m+m,:])
        time.append(ti[l+i*m:l+i*m+m])
    result = np.array(result)
    time = np.array(time)
    return (result,time)
    
if __name__ == "__main__":
    #Assign the parameter sigma, rho, and beta
    sigma = 10
    rho = 28
    beta = 8/3
    
    #Assign the value of number of burst K and sample size m
    K = 8
    m = 5
    l = 8
    
    #Assign period
    period = 20
    
    #Check the calculated derivatice with theoretical derivative
    (finalSol,finalDer,t) = burst(sigma,rho,beta,K*m,period)
    (h,time) = chopUp(finalSol,l,m,t)
    #Graph.graph(finalSol,t,h,time,K)
    #checkDer(finalDer,finalSol,[sigma,rho,beta])
    
    #Produce matrix A, V
    A = Experiment.constructMatrixA([finalSol])
    V = finalDer
    
    #Use L1 optimization to obtain matrix C1
    C1 = Optimization.optMatrix(A,V)
    #C2 is the actual matrix C obtained from parameters and Lorenz system directly
    C2 = np.transpose(np.array([np.array([0,-sigma,sigma,0,0,0,0,0,0,0]),np.array([0,rho,-1,0,0,0,-1,0,0,0]),np.array([0,0,0,-beta,0,1,0,0,0,0])]))
    Graph.graphM(C1,C2)

    
    #The ideal matrix C should be like
    #      0 -s s 0 0 0 0 0 0 0
    # CT = 0 r -1 0 0 0 -1 0 0 0
    #      0 0 0 -b 0 1 0 0 0 0