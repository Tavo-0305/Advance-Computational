'''
Calculation of F(x) gradient using the backpropagation algoritm

Defining F(x) as: f_3 ° f_2 ° f_1 ° f_2 ° f_1 (x)

So it behaves as an outcome from a 5 layer

'''
import numpy as np
#Declaration of functions
def f_1(x,W,b):
    return W*x + b
def f_2(x):
    return np.square(x)
def f_3(x):
    return np.sum(x)
def F(x):
    return f_3(f_2(f_1(f_2(f_1(x)))))

