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

#function that returns dy/dt
def model(y,t,sigma,rho,beta):
    x1,x2,x3 = y
    dydt = [-sigma*x1+sigma*x2,rho*x1-x1*x3-x2,x1*x2-beta*x3]
    return dydt

def SolveEq(sigma,rho,beta,y0,m):
    #time points
    t = np.linspace(0,1,m)

    #solve ODE
    sol = odeint(model,y0,t,args=(sigma,rho,beta))
    return sol

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
    
def graphM(C,D):
    #graph the image of two matrices
    fig, (ax0,ax1) = plt.subplots(1,2)
    im1 = ax0.imshow(C)
    ax0.set_title('The Calculated Matrix C')
    fig.colorbar(im1,ax=ax0)
    im2 = ax1.imshow(D)
    ax1.set_title('The Actual Matrix C')
    fig.colorbar(im2,ax=ax1)
    plt.show()
    
if __name__ == "__main__":
    #Assign the parameter sigma, rho, and beta
    sigma = 1
    rho = 2
    beta = 3
    
    #Assign the value of number of burst K and sample size m
    K = 5
    m = 15
    
    #Check the calculated derivatice with theoretical derivative
    (finalSol,finalDer) = burst(sigma,rho,beta,K,m)
    #checkDer(finalDer,finalSol,[sigma,rho,beta])
    
    #Produce matrix A, V
    A = Experiment.constructMatrixA(finalSol)
    V = Experiment.constructMatrixV(finalDer)
    
    #Use L1 optimization to obtain matrix C1
    C1 = Optimization.optMatrix(A,V)
    #C2 is the actual matrix C obtained from parameters and Lorenz system directly
    C2 = np.transpose(np.array([np.array([0,-sigma,sigma,0,0,0,0,0,0,0]),np.array([0,rho,-1,0,0,0,-1,0,0,0]),np.array([0,0,0,-beta,0,1,0,0,0,0])]))
    graphM(C1,C2)
    
    #The ideal matrix C should be like
    #      0 -s s 0 0 0 0 0 0 0
    # CT = 0 r -1 0 0 0 -1 0 0 0
    #      0 0 0 -b 0 1 0 0 0 0