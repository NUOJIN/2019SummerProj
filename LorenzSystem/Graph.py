#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 19:50:08 2019

@author: nokicheng
"""
import matplotlib.pyplot as plt


def graph(finalSol,t,h,time,K):
    #The shape of matrix finalSol should be (5,K*m,3)
    #First Burst
    plt.subplot(121)
    plt.plot(t,finalSol[:,0],'r',t,finalSol[:,1],'b',t,finalSol[:,2],'g')
    plt.title('Before Chopped')
    plt.grid(True)
    
    #Plot the chopped data then
    t = time
    dic = ['r.','y.','b.','g.','c.','m.','k.','c.','gold.','pink.','tomato.','salmon.']
    #First Burst
    plt.subplot(122)
    for i in range(0,K):
        plt.plot(t[i],h[i,:,0],dic[i],t[i],h[i,:,1],dic[i],t[i],h[i,:,2],dic[i])
    plt.title('After Chopped')
    plt.grid(True)
    
    plt.subplots_adjust(top=0.92, bottom=0.18, left=1.10, right=2.45, hspace=0.35, wspace=0.45)
    #plt.show()
    
def graphM(C,D):
    #graph the image of two matrices
    fig = plt.figure()
    ax0 = fig.add_subplot(121)
    im0 = ax0.imshow(C)
    ax0.set_title('The Calculated Matrix C')
    fig.colorbar(im0)
    ax1 = fig.add_subplot(122)
    im1 = ax1.imshow(D)
    ax1.set_title('The Actual Matrix C')
    fig.colorbar(im1)