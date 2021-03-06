# defines some helper functions for the RBM class

import numpy as np
from pandas import DataFrame
from random import random, shuffle, getrandbits
from hinton_demo import *

def matRound(mat,nDigits):
    "Element-wise rounding of matrix to nDigits. For making outputs prettier."
    newMat = np.zeros(mat.shape)
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            newMat[i,j] = round(mat[i,j],nDigits)
    return newMat


def symmetrize(a):
    "symmetrizes a U or L triangular square matrix. i.e. either the upper or lower triangle of the square matrix is all zeros, and the other triangle contains the data"
    return a + a.T - np.diag([a[i,i] for i in range(len(a))])


def triangularize(a):
    "turns a square symmetric matrix into an upper triangular matrix"
    for i in range(len(a)):
        for j in range(i):
            a[i,j] = 0
    return a

def logistic(a):
    'The logistic function a.k.a. sigmoid.'
    return (1+2.71818**(-1*a))**(-1)

vlogistic = np.vectorize(logistic)

def draw(p, off=0, on=1):
    'non-uniform binary probability distribution'
    threshold = random()
    if threshold > p:
        s = off
    else:
        s = on
    return s

vdraw = np.vectorize(draw)
