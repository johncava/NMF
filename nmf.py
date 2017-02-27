from __future__ import division
import numpy as np

#Matrix V that needs to be decomposed into two matrices
V = np.array([[5,4,3],
             [2,1,2],
             [9,8,7]])

#Matrix H
H = np.array([[1,2,3],[4,5,6],[7,8,9]])

#Matrix W
W = np.array([[3,2,1],[6,9,4],[8,2,1]])

for iterations in xrange(50):
    H = H*((W.T*V)/(W.T*W*H + 0.0001))
    W = W*((V*H.T)/(W*H*H.T + 0.0001))
    print(H*W)