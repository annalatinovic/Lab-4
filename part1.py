import numpy as np
from scipy import integrate

#Part 1
def integral(theta,theta_m):
    integral_value = 1.0/(np.sqrt(np.cos(theta)-np.cos(theta_m)))
    return integral_value

#convert to radians in the function
#a small angle would be close to 2pi
def exact_period(pendulum_len, initial_swing=0):
    initial_swing = initial_swing*(np.pi/180)
    if initial_swing != 0:
        constant = pendulum_len / (2*9.81)
        period =  np.sqrt(constant)*integrate.quad(integral, 0, float(initial_swing), args=(initial_swing,))[0]
        return 4*period
    else:
        constant = pendulum_len / (9.81)
        period = 2*np.pi*constant
        return period
        
exact_period(4,30)