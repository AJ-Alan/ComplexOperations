from mpmath import * #for special math functions to be expanded in the future
import numpy as np #for numpy arrays

def complexString(a):
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


