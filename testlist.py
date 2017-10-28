import numpy as np #NumPy is the fundamental package for scientific computing with Python
import matplotlib.pyplot as plt #Python 2D plotting library
import sympy as sy #Simbolic calcultations maybe need it
#import numdifftools as nd #necessary to compute the jacobian matrix
import math

k=1
H1 = [0,0]
H2 = [3,0]

d = np.sqrt((H1[0]-H2[0])**2+(H1[1]-H2[1])**2)
alfa = np.arctan((H1[1]-H2[1])/(H1[0]-H2[0]))

#h matrix --- will have tu use a for loop then i redirect to the first position in vector then i iterate ton the second vector then to the first position again
h = [d, alfa]

print (h)
a = math.cos(3.14159265358979)
print (a)