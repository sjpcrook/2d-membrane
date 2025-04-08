import math
import numpy as np
import matplotlib.pyplot as plt
import Initialisation as init


def central_difference(uarray, v0, deltax, deltat, mu, c):
    '''
    Finds the second spacial derivative of a point utilising the points directly adjacent

    Parameters
    ----------
    uarray: np.array
	A 3 by 3 array centred at the point we wish to find the second spacial derivative of
    v0: float
        The velocity of the point we wish to find the derivative of
    deltax: float
        The space interval
    deltat: float
        The time step to find the derivative over
    mu: float
        The damping coefficient
    c: float
        The propogation velocity

    Returns
    -------
    u1, v1: np.array
        The position and velocity of the point after the time step
    '''
    dudz2 = (uarray[0,1]+uarray[1,0]+uarray[2,1]+uarray[1,2]-(4.0*uarray[1,1]))/(deltax*deltax)
    u1 = (c*c*dudz2*(deltat*deltat)) + (v0*deltat) + uarray[1,1] - (mu*v0*deltat*deltat)
    v1 = (c*c*dudz2*deltat) + v0 - (mu*v0*deltat)
    return(np.array([u1, v1]))

def full_finite_difference(u0array, v0array, deltax, deltat, mu, c):
    '''
    Finds the state of the system after a small time step

    Parameters
    ----------
    u0array: np.array
	A square array representing the amplitude at the respective xy coordinate
    v0array: float
        A square array representing the velocity at the respective xy coordinate
    deltax: float
        The space interval
    deltat: float
        The time step to simulate the system over
    mu: float
        The damping coefficient
    c: float
        The propogation velocity
    Returns
    -------
    u1array, v1array: two np.array s
        The positions and velocitys of the system after the time step
    '''
    n = np.shape(u0array)[0]
    u1array = np.zeros([n,n], dtype = float)
    v1array = np.zeros([n,n], dtype = float)
    nrange = np.arange(1, n-1)
    for i in nrange:
        for j in nrange:
            smallarray = u0array[(i-1):(i+2), (j-1):(j+2)]
            uv1 = central_difference(smallarray, v0array[i,j], deltax, deltat, mu, c)
            u1array[i,j] = uv1[0]
            v1array[i,j] = uv1[1]
    return(u1array, v1array)
           
