from mpmath import * #for special math functions to be expanded in the future
import numpy as np #for numpy arrays/list 

def complexString(a): #function that prints a string based on the complex number list
  if a[1] == 0: #pure reals
    return str(a[0]) #only returns real numbers
  elif a[0] == 0: #pure imaginary
    return str(a[1])+'i'
  elif a[1] > 0: #imaginary part is positive
    return str(a[0])+'+'+str(a[1])+'i'
  elif a[1] < 0: #imaginary part is negative
    return str(a[0])+'-'+str(abs(a[1]))+'i'    

def addC(c1,c2): #to add 
  return c1 + c2 

def subtractC(c1,c2): #to subtract
  return c1 - c2

def quotient(c1,c2): #to divide -> c1 is numerator and c2 is denominator
  if c2[0] == 0 and c2[1] == 0:
    return "Complex infinity"
  else:
    divide = c2[0]**2 + c2[1]**2 #divisor for both real and imaginary parts
    real = (c1[0]*c2[0] + c1[1]*c2[1])/divide
    imag = (c2[0]*c1[1] - c1[0]*c2[1])/divide
    return np.array([real,imag])
  
def product(c1,c2): #to multiply
    real = c1[0]*c2[0] - c1[1]*c2[1])
    imag = c2[0]*c1[1] + c1[0]*c2[1]
    return np.array([real,imag])

