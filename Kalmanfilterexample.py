# Kalman filter example demo in Python
#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plot

# intial parameters
n_iter = 50
sz = (n_iter,) # size of array
x1 = -5 # truth value (typo in example at top of p. 13 calls this z)
z = np.random.normal(x1,0.1,size=sz) # observations (normal about x, sigma=0.1)

Q = 1e-5 # process variance

# allocate space for arrays
xhat=np.zeros(sz)      # a posteri estimate of x
P=np.zeros(sz)         # a posteri error estimate
xhatminus=np.zeros(sz) # a priori estimate of x
Pminus=np.zeros(sz)    # a priori error estimate
K=np.zeros(sz)         # gain or blending factor

R = 0.1**2 # estimate of measurement variance

# intial guesses
xhat[0] = -4.8
P[0] = 1.0

for k in range(1,n_iter):
    # time update
    xhatminus[k] = xhat[k-1]
    Pminus[k] = P[k-1]+Q


    print(xhatminus[k]) #test print

    # measurement update
    K[k] = Pminus[k]/( Pminus[k]+R )
    xhat[k] = xhatminus[k]+K[k]*(z[k]-xhatminus[k])
    P[k] = (1-K[k])*Pminus[k]

plt.figure()
plt.plot(z,'k+',label='observations')
plt.plot(xhat,'b-',label='a posteri estimate')
plt.axhline(x1,color='g',label='truth value')
plt.legend()
plt.title('Relative position vs. iteration step', fontweight='bold')
plt.xlabel('Iteration')
plt.ylabel('Relative position')

#plt.figure()
#valid_iter = range(1,n_iter) # Pminus not valid at step 0
#plt.plot(valid_iter,Pminus[valid_iter],label='a priori error estimate')
#plt.title('Estimated $\it{\mathbf{a \ priori}}$ error vs. iteration step', fontweight='bold')
#plt.xlabel('Iteration')
#plt.ylabel('$(Voltage)^2$')
#plt.setp(plt.gca(),'ylim',[0,.01])
plt.show()

#print ("O valor de x é", xhat)