#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 13:06:40 2019

@author: nokicheng
"""

import numpy as np
from scipy.integrate import odeint
import check
from random import randint
import Experiment
import Optimization
import Graph

#function that returns dy/dt
def model(y,t,sigma,rho,beta):
    x1,x2,x3 = y
    dydt = [-sigma*x1+sigma*x2,rho*x1-x1*x3-x2,x1*x2-beta*x3]
    return dydt

def SolveEq(sigma,rho,beta,y0,m):
    #time points
    t = np.linspace(0,100,m)

    #solve ODE
    sol = odeint(model,y0,t,args=(sigma,rho,beta))
    print(sol)
    return (sol,t)

def InitialGenerator(p):
    #p is the precision
    return [randint(-p,p)/p,randint(-p,p)/p,randint(-p,p)/p]

def getGradient(X,m):
    #Input matrix X and return xs' derivative
    #The precision of derivetive depends on the value of m
    result = []
    for i in range(0,len(X)-1):
        row = []
        for j in range(0,len(X[1]-1)):
            row.append((X[i+1,j]-X[i,j])/(1/m))
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
  
def burst(sigma,rho,beta,K,m):
    #create K bursts and m samples with given sigma,rho,beta
    finalSol = []
    finalDer = []
    for i in range(0,K):
        #Obtain the solution by precision = 100
        sol = SolveEq(sigma,rho,beta,InitialGenerator(100),m+1)
        der = getGradient(sol,m)
        sol = sol[:-1,:]
        finalSol.append(sol)
        finalDer.append(der)
    
    finalSol = np.array(finalSol)
    finalDer = np.array(finalDer)
    return (finalSol,finalDer)

def chopUp(u,l,K,m,t):
    #Input a matrix u with shape 5 by K*m by 6 as well as its corresponding time
    #Output a matrix with shape K by 5 by m by 6 as well as corresponding time
    #The chop starts from position l, l < K*m and l >= 0
    result = []
    time = []
    h = np.concatenate((u,u),axis=1)
    ti = np.concatenate((t,t),axis=0)
    for i in range(0,K):
        result.append(h[:,l+i*m:l+i*m+m,:])
        time.append(ti[l+i*m:l+i*m+m])
    result = np.array(result)
    time = np.array(time)
    return (result,time)

if __name__ == "__main__":
    #Assign the parameter sigma, rho, and beta
    sigma = 10
    rho = 28
    beta = 8/3
    
    #Assign the value of number of burst K, sample size m, chop up starting point l
    K = 5
    m = 5
    l = 14
    
    (finalSol,finalDer,t) = burst(sigma,rho,beta,2,K*m)
    #Obtain vectors u_j with j from 0 to 5*K*m and graph different burst seperately
    u = np.concatenate((finalSol,finalDer),axis=2)
    #graph1(finalSol,t)
    
    #Chop up the data into K pieces with input start point l and graph different bursts seperately
    (h,time) = chopUp(u,l,K,m,t)
    #graph2(h,time,K)
  
    #Produce matrix A, V
    A = Experiment.constructMatrixA(finalSol)
    V = Experiment.constructMatrixV(finalDer)
    
    #Use L1 optimization to obtain matrix C1
    #C1 = Optimization.optMatrix(A,V)
    #C2 is the actual matrix C obtained from parameters and Lorenz system directly
    C2 = np.transpose(np.array([np.array([0,-sigma,sigma,0,0,0,0,0,0,0]),np.array([0,rho,-1,0,0,0,-1,0,0,0]),np.array([0,0,0,-beta,0,1,0,0,0,0])]))
    
    #Graph the matrices C1 and C2
    #Graph.graphM(C1,C2)
    Graph.graph(finalSol,t,h,time,K)
  