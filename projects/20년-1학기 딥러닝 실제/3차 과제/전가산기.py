import numpy as np

def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

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
 
#전가산기
def FullAdder(a, b, c):
    tmp1 = XOR(a, b)
    result_sum = XOR(tmp1, c)

    tmp2 = AND(a, b)
    tmp3 = AND(tmp1, c)
    result_carry = OR(tmp2, tmp3)
    print(a, b, c, result_sum, result_carry)

print('\nFullAdder')  
FullAdder(0, 0, 0)
FullAdder(0, 0, 1)
FullAdder(0, 1, 0)
FullAdder(0, 1, 1)
FullAdder(1, 0, 0)
FullAdder(1, 0, 1)
FullAdder(1, 1, 0)
FullAdder(1, 1, 1)

print('\n NAND')     
print(0, 0, NAND(0, 0))
print(1, 0, NAND(1, 0))
print(0, 1, NAND(0, 1))
print(1, 1, NAND(1, 1))

print('\nAND')      
print(0, 0, AND(0, 0))
print(1, 0, AND(1, 0))
print(0, 1, AND(0, 1))
print(1, 1, AND(1, 1))

print('\nOR')  
print(0, 0, OR(0, 0))
print(1, 0, OR(1, 0))
print(0, 1, OR(0, 1))
print(1, 1, OR(1, 1))

print('\nXOR')  
print(0, 0, XOR(0, 0))
print(1, 0, XOR(1, 0))
print(0, 1, XOR(0, 1))
print(1, 1, XOR(1, 1))

    
    
    
    
    
