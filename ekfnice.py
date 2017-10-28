#Implementação do Extended Kalman Filter

import numpy as np #NumPy is the fundamental package for scientific computing with Python
import matplotlib.pyplot as plt #Python 2D plotting library
import sympy as sy #Simbolic calcultations maybe need it
import math #use cossin and sin
#from numpy import linalg
#import numdifftools as nd #necessary to compute the jacobian matrix


#Initial Conditions - posições iniciais
#x[0] = [0,0,0] #initial position
#s[0] = [0,0,0] #pose do robot no frame do mundo
#z[k] = [0,0,0]  #ose do landmark no frame do robot
#theta[k] = #state x (coordinates of landmarks) and s (robot pose - without the theta) pose landmark frame do mundo
mu = 0 #mean
num_iter = 3 #number of iterations
size_v = (num_iter,) #size fo array
sdevia = 0.1 #standard deviation
y = np.random.normal(mu,sdevia,size=size_v) #Draw random samples from a normal (Gaussian) distribution.
#P[0] = 1.0 #estimate to error on Kalman Gain



#LEMBRAR DE MUDAR O KALMAN GAIN

#Comentei x, s e P e tenho de ter em conta que isto depois vai entrar no ekf mesmo!!!!!
#MUDEI os valores de H1 e H2 para os xhat em vez de x[j] e s[j]


#Covariances
Q = 0  #time update variance -- We consider zero because the landmarks are known a priori
R = 1e-3  #estimate of measurement update
x1 = -0.37727 # truth value (typo in example at top of p. 13 calls this z)

# allocate space for arrays
theta_c=np.zeros(size_v)      # a posteri estimate of x
sigma_c=np.zeros(size_v)         # a posteri error estimate
theta_p=np.zeros(size_v) # a priori estimate of x
sigma_p=np.zeros(size_v)    # a priori error estimate
K=np.zeros(size_v)         # gain or blending factor


theta = [[1,1,1],[2,2,2],[3,3,3]]
S = [[1,1,1],[2,2,2],[3,3,3]]
sigma = [[1,1,1],[2,2,2],[3,3,3]]
print(sigma_p)


#S = []
h = []
print(h)
#criar
for k in range(1,num_iter):		
	#H1 = xhatminus[k]
	#H2 = xhatminus[k]
	#s[k] = S

	#z[k] = Z
	
	#theta[k] = THETA

   	# time update
	#xhatminus[k] = xhat[k-1]
	#Pminus[k] = P[k-1]+Q  #Q is zero in our case -- just like in the kalman Filter


	#print(xhatminus[3]) #test print


	#h matrix --- will have tu use a for loop then i redirect to the first position in vector then i iterate ton the second vector then to the first position again
	#h = [d[k], alfa[k]]
	#Jacobian matrix
	#H = nd.Jacobian(h)
	 
	#h matrix
	h = [-S[0][0]+math.cos(S[2][2])*theta[0][0]+math.sin(S[2][2])*theta[1][1],-S[1][1]-math.sin(S[2][2])*theta[0][0]+math.cos(S[2][2])*theta[1][1],-S[2][2]+theta[2][2]]

	#H matrix - Jacobian
	#H = [[H1[0]-H2[0]/d,H1[1]-H2[1]/d],[H2[1]-H1[1]/d**2,H2[0]-H1[0]/d**2]]
	H = [[math.cos(S[2][2]),math.sin(S[2][2]),0],[-1*math.sin(S[2][2]),math.cos(S[2][2]),0],[0,0,1]] #Não é necessário identificar como k+1

	#Prediction
	
	#theta_p[k+1] = theta_p[k]
	#sigma_p[k+1] = sigma_p[k]
	
	#Update
	K[1] = sigma[1][1]*(H[1][1])*(H[1][1]*sigma[1]*H[1][1])
	theta[1] = theta[1] + K[k+1]*(y[k+1] - h[1][1]) #AQUI ESTÁ y MAS TEM DE ESTAR z
	sigma[1] = (np.identity(num_iter) - K[1]*H[1][1])*sigma[1][1]
	#K[k+1] = sigma_p[k]*np.transpose(H)*np.linalg.inv(H*sigma_p[k+1]*np.transpose(H))
	#theta_c[k+1] = theta_p[k+1] + K[k+1]*(y[k+1] - h) #AQUI ESTÁ y MAS TEM DE ESTAR z
	#sigma_c[k+1] = (np.identity(num_iter) - K[k+1]*H)*sigma_p[k]


    # measurement update
    #K[k] = Pminus[k]/( Pminus[k]+R ) #Kalman Gain without matrix H(measurement Matrix)
		
	#xhat[k] = xhatminus[k]+K[k]*(y[k]-xhatminus[k]) #Miss h instead of the ending xhatminus
	#P[k] = (1-K[k]*H)*Pminus[k] #again without matrix H
	#o H aqui dentro por inicialmente ser zero não me permite atualizar o kalman gain para um outro valor que não zero, logo
	#tenho de mudar a forma de definir o H porque senão isto vai me dar sempre zero e dessa forma não saio daqui

plt.figure()
plt.plot(y,'k+',label='noisy measurements')
plt.plot(theta_c,'b-',label='a posteri estimate')
plt.axhline(x1,color='g',label='truth value')
plt.legend()
plt.title('Estimate vs. iteration step', fontweight='bold')
plt.xlabel('Iteration')
plt.ylabel('Voltage')

plt.figure()
valid_iter = range(1,num_iter) # Pminus not valid at step 0
plt.plot(valid_iter,Pminus[valid_iter],label='a priori error estimate')
plt.title('Estimated $\it{\mathbf{a \ priori}}$ error vs. iteration step', fontweight='bold')
plt.xlabel('Iteration')
plt.ylabel('$(Voltage)^2$')
plt.setp(plt.gca(),'ylim',[0,.01])
plt.show()


#plt.figure()
#plt.plot(y,'k+',label='noisy measurements')
#plt.plot(xhat,'b-',label='a posteri estimate')
#plt.axhline(x1,color='g',label='truth value')
#plt.legend()
#plt.title('Estimate vs. iteration step', fontweight='bold')
#plt.xlabel('Iteration')
#plt.ylabel('Voltage')

#plt.figure()
#valid_iter = range(1,num_iter) # Pminus not valid at step 0
#plt.plot(valid_iter,Pminus[valid_iter],label='a priori error estimate')
#plt.title('Estimated $\it{\mathbf{a \ priori}}$ error vs. iteration step', fontweight='bold')
#plt.xlabel('Iteration')
#plt.ylabel('$(Voltage)^2$')
#plt.setp(plt.gca(),'ylim',[0,.01])
#plt.show()



# Factorial function
#    if n <= 0:
#        return 1
#    else:
#        return n * factorial(n - 1)

#Taylor series function
#def taylor(function, x0, n, x = sy.Symbol('x')):
#    i = 0
#    p = 0
#    while i <= n:
#        p = p + (function.diff(x, i).subs(x, x0))/(factorial(i))*(x - x0)**i
#        i += 1
#    return p
    #sy.Simbol associate the variable x to letter 'x'
    #diff difference between to consecutive iterations
    #subs replace the previous variable for the next one


#for k in range(1,num_iter):
    # time update
#    xhatminus[k] = xhat[k-1]  #Gonna interfere with measurement model and only with that
#    Pminus[k] = P[k-1]+Q  #Q is zero in our case -- just like in the kalman Filter

    # measurement update
#    K[k] = Pminus[k]/( Pminus[k]+R ) #Kalman Gain without matrix H(measurement Matrix)
#    xhat[k] = xhatminus[k]+K[k]*(z[k]-xhatminus[k]) #Miss H instead of the ending xhatminus
#    P[k] = (1-K[k])*Pminus[k] #again without matrix H