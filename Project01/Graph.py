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
    plt.subplot(431)
    plt.plot(t,finalSol[0,:,0],'r',t,finalSol[0,:,1],'b',t,finalSol[0,:,2],'g')
    plt.title('First Burst')
    plt.grid(True)
    
    #Second Burst
    plt.subplot(432)
    plt.plot(t,finalSol[1,:,0],'r',t,finalSol[1,:,1],'b',t,finalSol[1,:,2],'g')
    plt.title('Second Burst')
    plt.grid(True)
    
    #Third Burst
    plt.subplot(433)
    plt.plot(t,finalSol[2,:,0],'r',t,finalSol[2,:,1],'b',t,finalSol[2,:,2],'g')
    plt.title('Third Burst')
    plt.grid(True)
    
    #Forth Burst
    plt.subplot(434)
    plt.plot(t,finalSol[3,:,0],'r',t,finalSol[3,:,1],'b',t,finalSol[3,:,2],'g')
    plt.title('Forth Burst')
    plt.grid(True)
    
    #Fifth Burst
    plt.subplot(435)
    plt.plot(t,finalSol[4,:,0],'r',t,finalSol[4,:,1],'b',t,finalSol[4,:,2],'g')
    plt.title('Fitth Burst')
    plt.grid(True)
    
    #Plot the chopped data then
    t = time
    dic = ['r.','y.','b.','g.','c.','m.','k.']
    #First Burst
    plt.subplot(437)
    for i in range(0,K):
        plt.plot(t[i],h[i,0,:,0],dic[i],t[i],h[i,0,:,1],dic[i],t[i],h[i,0,:,2],dic[i])
    plt.title('First Burst')
    plt.grid(True)
    
    #Second Burst
    plt.subplot(438)
    for i in range(0,K):
        plt.plot(t[i],h[i,1,:,0],dic[i],t[i],h[i,1,:,1],dic[i],t[i],h[i,1,:,2],dic[i])
    plt.title('Second Burst')
    plt.grid(True)
    
    #Third Burst
    plt.subplot(439)
    for i in range(0,K):
        plt.plot(t[i],h[i,2,:,0],dic[i],t[i],h[i,2,:,1],dic[i],t[i],h[i,2,:,2],dic[i])
    plt.title('Third Burst')
    plt.grid(True)
    
    #Forth Burst
    plt.subplot(4,3,10)
    for i in range(0,K):
        plt.plot(t[i],h[i,3,:,0],dic[i],t[i],h[i,3,:,1],dic[i],t[i],h[i,3,:,2],dic[i])
    plt.title('Forth Burst')
    plt.grid(True)
    
    #Fifth Burst
    plt.subplot(4,3,11)
    for i in range(0,K):
        plt.plot(t[i],h[i,4,:,0],dic[i],t[i],h[i,4,:,1],dic[i],t[i],h[i,4,:,2],dic[i])
    plt.title('Fitth Burst')
    plt.grid(True)
    
    plt.subplots_adjust(top=2.92, bottom=1.18, left=0.10, right=1.45, hspace=0.35, wspace=0.45)
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