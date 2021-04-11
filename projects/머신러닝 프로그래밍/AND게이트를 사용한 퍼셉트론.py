import numpy as np

def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2 - theta
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1
    
print('\nAND')      
print(0, 0, AND(0, 0))
print(1, 0, AND(1, 0))
print(0, 1, AND(0, 1))
print(1, 1, AND(1, 1))

def NAND(x1, x2):
    w1, w2, theta = -0.5, -0.5, -0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1
    
def OR(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.2
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

def XOR(x1, x2):
    return AND(OR(x1, x2), NAND(x1, x2))

print('\nXOR')  
print(0, 0, XOR(0, 0))
print(1, 0, XOR(1, 0))
print(0, 1, XOR(0, 1))
print(1, 1, XOR(1, 1))