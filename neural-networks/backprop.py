'''
Calculation of F(x) gradient using the backpropagation algoritm

Defining F(x) as: f_3 ° f_2 ° f_1 (x)

Declaration of functions (if needed): 

def f_1(x,W,b):
    return W*x + b
def f_2(x):
    return np.square(x)
def f_3(x):
    return np.sum(x)
def F(x):
    return f_3(f_2(f_1)))

'''
import numpy as np

#Calculating the gradient of F by hand (see backprop.MD), 
# with respect to the parameters (W and b): 

def F_grad_W(x,W,b):
    prod = W @ x + b
    return np.outer(2*prod,x)

def F_grad_b(x,W,b):
    return 2*(W @ x + b)

#Testing vectors:

x = np.array([0.1,0.2,0.3,0.4,0.5])
y = 0.5 * (np.array([1,1,1,1,1]))
z = np.array([0.5,0.5,0.1,0.1,0.1])

testing = [x,y,z]

np.random.seed(666)

#Defining W and b as: 
 
W = np.random.randint(0,2,size=(5,5)) #values are 1 or 0
b = np.random.randint(0,2,size=5) #values are 1 or 0

for _ in testing:
    gradW = F_grad_W(_,W,b)
    gradb = F_grad_b(_,W,b)
    print(f'The gradient of F with respect to W for x={_} is {gradW}')
    print(f'The gradient of F with respect to b for x={_} is {gradb}')


