#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:17:37 2019

@author: nokicheng
"""

import numpy as np
import Graph
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import Optimization

def Lorenz96(t,x,N,F,m=0):
  # compute state derivatives
  if m == 0:
      d = np.zeros(N)
  else:
      d = np.zeros((N,m))
  # first the 3 edge cases: i=1,2,N
  d[0] = (x[1] - x[N-2]) * x[N-1] - x[0]
  d[1] = (x[2] - x[N-1]) * x[0]- x[1]
  d[N-1] = (x[0] - x[N-3]) * x[N-2] - x[N-1]
  # then the general case
  for i in range(2, N-1):
      d[i] = (x[i+1] - x[i-2]) * x[i-1] - x[i]
  # add the forcing term
  d = d + F
  # return the state derivatives
  return d

def SolveEq(N,y0,m,period,F):
    #time points
    t = np.linspace(0,period,m)
    #solve ODE
    sol = solve_ivp(lambda t,y:Lorenz96(t,y,N,F),[0,period],y0,t_eval=t)
    #sol = odeint(Lorenz96, y0, t, args=(N,F))
    return (sol,t)

def InitialGenerator(N):
    return np.random.uniform(-1,1,N)

#generate stochastic bursts
def burst(N,m,period,F):
    y0 = InitialGenerator(N)
    (sol,t) = SolveEq(N,y0,m,period,F)
    sol = sol.y
    #sol = sol + np.random.normal(0,0.01,sol.shape)
    return (np.transpose(sol),t)

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

def constructIdealMatrixV(finalSol,t,N,F,m):
    result = Lorenz96(t,np.transpose(finalSol[0]),N,F,m)
    l = len(finalSol)
    for i in range(1,l):
        result = np.concatenate((result,Lorenz96(t,np.transpose(finalSol[i]),N,F,m)),axis = 1)
    return np.transpose(result)

def checkSparcity(M,threhold):
    count = 0
    r,c = M.shape
    for i in range(0,r):
        for j in range(0,c):
            if abs(M[i][j]) >= threhold:
                count += 1
    return count

def p(i,j,N):#only work for i<=j
    N = N-1
    if i < 0:
        i += N + 1
    elif i > N:
        i = i - N - 1
    if j < 0:
        j += N + 1
    elif j > N:
        j = j - N - 1
    if i > j:
        i,j = j,i
    #return int(N*(i)+0.5*(i-i*i)+j)
    return int((N)*i+0.5*(i-i*i)+j+N+2)

def actualMatrixC(N,F):
    result = []
    NN = int((N+2)*(N+1)/2)
    for i in range(0,N):
        x = np.zeros(NN)
        x[0] = F
        x[p(i-1,i+1,N)] = 1
        x[p(i-2,i-1,N)] = -1
        x[i+1] = -1
        result.append(x)
    return np.transpose(np.array(result))
            
def experiment(K,N):
    mulBurst = []
    for i in range(0,K):
        mulBurst.append(burst(N,m,period,F)[0])
    mulBurst = np.array(mulBurst)
    
    A = constructMatrixA(mulBurst)
    V = constructIdealMatrixV(mulBurst,t,N,F,m)
    
    C1 = Optimization.optMatrix(A,V)
    C2 = actualMatrixC(N,F)
    return (np.linalg.norm(C1-C2)/np.linalg.norm(C2))

def experiment2(K,N,m):
    count = 0  
    xs = []
    for i in range(0,20):
        x = experiment(K,N)
        xs.append(x)
        if x < 0.05:
            count += 1
    return (m*K/NN, count/20)
if __name__ == "__main__":
    #Set global parameters
    N = 50
    NN = int((N+2)*(N+1)/2)
    m = 5
    dt = 2
    period = m*dt
    F = 8
    
    y,t = burst(N,m,period,F)
    
    #Assign the value of K
    #K*m < NN = 703
    X = []
    Y = []
    for K in [9,10,11,12]:
        xx, yy = experiment2(K,N,m)
        X.append(xx)
        Y.append(yy)
    
    m = 10
    H = []
    I = []
    for K in [7,8,9,10]:
        xx, yy = experiment2(K,N,m)
        H.append(xx)
        I.append(yy)
    
    HH = [X,H]
    II = [Y,I]
    cv = ['m=5', 'm=10']
    c = ['r','b']
    
    for i in [0,1]:
        plt.scatter(HH[i],II[i],c=c[i],label=cv[i])
    plt.legend()
    plt.xlabel("K*m/N")
    plt.ylabel("Successful Recovery Probability")
    