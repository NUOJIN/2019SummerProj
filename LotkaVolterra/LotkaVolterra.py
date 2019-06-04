#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 20:21:58 2019

@author: nokicheng
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def model(y,t,r,alpha,N):
    x = y
    dydt = np.matmul(np.diag(r),np.diag(x)).dot(np.ones(N)-alpha.dot(x))
    return dydt

def SolveEq(r,alpha,N,y0,m,period):
    #time points
    t = np.linspace(0,period,m)

    #solve ODE
    sol = odeint(model,y0,t,args=(r,alpha,N))
    return (sol,t)

def InitialGenerator(N):
    return np.random.uniform(-1,1,N)

if __name__ == '__main__':
    r = np.array([1,0.72,1.53,1.27])
    alpha = np.array([[1,1.09,1.52,0],[0,1,0.44,1.36],[2.33,0,1,0.47],[1.21,0.51,0.35,1]])
    N = 4
    
    y0 = InitialGenerator(N)
    print(y0)
    (sol,t) = SolveEq(r,alpha,N,y0,5000,10000)
    
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    xdata = sol[:,0]
    ydata = sol[:,1]
    zdata = sol[:,2]
    cdata = sol[:,3]
    cmhot = plt.get_cmap('nipy_spectral')
    gra = ax.scatter3D(xdata,ydata,zdata,c=cdata,cmap=cmhot,marker='.')
    fig.colorbar(gra,fraction=0.046, pad=0.06)
    