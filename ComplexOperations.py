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

## Basic operations

def addC(c1,c2): #to add 
  return c1 + c2 

def minusC(c1,c2): #to subtract
  return c1 - c2

def quotientC(c1,c2): #to divide -> c1 is numerator and c2 is denominator
  if c2[0] == 0 and c2[1] == 0: #cannot divide by zero
    print("Complex infinity")
  else:
    divide = c2[0]**2 + c2[1]**2 #divisor for both real and imaginary parts
    real = (c1[0]*c2[0] + c1[1]*c2[1])/divide #real part
    imag = (c2[0]*c1[1] - c1[0]*c2[1])/divide #imaginary part
    return np.array([real,imag])
  
def productC(c1,c2): #to multiply
    real = c1[0]*c2[0] - c1[1]*c2[1] #real part
    imag = c2[0]*c1[1] + c1[0]*c2[1] #imaginary part
    return np.array([real,imag])

## changing polar form to rectangular form and vice versa
def findPolar(c): #to find polar form
  radius = sqrt(c[0]**2 + c[1]**2) #radius of the complex number
  theta = arctanCC(c) #to find the angle (in radians) from the real axis 
  return np.array([radius,theta])

def findRect(c): #to find the rectangular form where c[0] == radius and c[1] == angle (in radians)
  real = c[0]*cos(c[1])
  imag = c[0]*sin(c[1])
  return np.array([real,imag])
  
def arctanCC(c): #specific arctangent formula for infinity and negative real cases when finding the argument of the complex number 
  if c[0] == 0: #for division by zero cases
    if c[1] > 0: #when the imaginary part is positive -> pi/2
      return pi/2
    elif c[1] < 0: #when the imaginary part is negative -> -pi/2
      return -pi/2
    else: #for pure zero caseso
      return 0
  elif c[0] < 0: #for negative real number cases -> pi
    return pi
  else: #for normal cases that isn't included from above
    return atan(c[1]/c[0])

## Functions related to euler's number
# complex natural log
def logC(c): #necessary for general natural log of complex numbers rather than the log of any number by complex bases 
  l = findPolar(c) #to find the polar form which is necessary for finding the natural log
  real = log(l[0]) #real part 
  imag = l[1] #imaginary part
  return np.array([real,imag])

# complex exponentiation (by e)
def expC(c): #useful when dealing with exponential values
  mult = exp(c[0]) #multiplied to both real and imaginary
  e = findRect(np.array([1,c[1]])) #to have the imaginary part as the input for the theta
  real = mult*e[0] #real part
  imag = mult*e[1] #imaginary part
  return np.array([real,imag])

## Special Functions
# complex exponentiation simplified based on my original program
def powC(c1,c2):
  if c1[0] == 0 and c1[1] == 0 and c2[0] == 0: # both forms of 0^0 and 0^i are undefined
    print("\nThe value is undefined")
  else: 
    return expC(productC(logC(findPolar(c1)),c2))

# complex logarithm simplified
def logarithmC(c1,c2):
    if c1[0] == 0 and c1[1] == 0:
        if c2[0] == 0 and c2[1] == 0:
            print("This is undefined")
        else:
            return np.array([0,0])
    elif c2[0] == 0 and c2[1] == 0:
        print("The result is complex infinity")
    elif c1[0] == 1 and c1[1] == 0:
        if c2[0] == 1 and c2[1] == 0:
            print("This is undefined")
        else:
            print("The result is complex infinity")
    elif c1[0] == c2[0] and c1[1] == c1[1]:
        return np.array([1,0])
    else:
      based = logC(c1)
      input = logC(c2)
      return quotientC(c2,c1)

## Trigonometric functions
# all derived based on their complex definitions and proven by Wolfram Alpha
def sine(a):
    real = sin(a[0])*cosh(a[1])
    imag = cos(a[0])*sinh(a[1])
    return np.array([real,imag])

def cosine(b):
    real = cos(b[0])*cosh(b[1])
    imag = -sin(b[0])*sinh(b[1])
    return np.array([real,imag])

def tangent(c):
    real = tan(c[0])/(pow(cosh(c[1]),2)+pow(tan(c[0])*sinh(c[1]),2))
    imag = tanh(c[1])/(pow(cos(c[0]),2)+pow(tanh(c[1])*sin(c[0]),2))
    return np.array([real,imag])

def secant(d):
    real = sec(d[0])*sech(d[1])/(1+pow(tan(d[0])*tanh(d[1]),2))
    imag = csc(d[0])*csch(d[1])/(1+pow(cot(d[0])*coth(d[1]),2))
    return np.array([real,imag])

def cosecant(f):
    real = csc(f[0])*sech(f[1])/(1+pow(cot(f[0])*tanh(f[1]),2))
    imag = -sec(f[0])*csch(f[1])/(1+pow(tan(f[0])*coth(f[1]),2))
    return np.array([real,imag])

def cotangent(g):
    real = tan(g[0])/(pow(cosh(g[1])*sec(g[0]),2)-1)
    imag = tanh(g[1])/(pow(sech(g[1])*cos(g[0]),2)-1)
    return np.array([real,imag])

## Inverse Trigonometric functions
#possibly the hardest complex function
def arcsine(w):
  quotientC(
    logC(
      addC(
        productC(w,np.array([0,1])),
        powC(
          minusC(
            np.array[1,0],
            productC(w,w)
          ),
          np.array([0.5,0])
        )
      )
    ),
    np.array([0,1]))


a = np.array([2,2])
b = np.array([-3,5])

