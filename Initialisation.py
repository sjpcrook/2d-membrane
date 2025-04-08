import math
import numpy as np
import matplotlib.pyplot as plt
import random

def initialise(n, L, f, constants):
    '''
    Creates an n by n grid of points with their corresponding amplitude u
    
    Parameters
    ----------
    n : float
        Number of points in a given row of the grid
    
    L: float
        The length of the membrane
    
    f: function
        Function which returns the amplitude of a point (x,y)

    constants: array
        An array of constants needed to determine each amplitude
    '''
    grid = np.zeros([n,n])
    for xgrid in range(n):
        xl = xgrid*L/(n-1)
        for ygrid in range(n):
            yl = ygrid*L/(n-1)
            u = f(xl, yl, constants)
            grid[(n-1)-ygrid, xgrid] = u
    floatgrid = grid.astype(np.float)
    return(floatgrid)

def add_coord(x,y, constants):
    '''
    A function which simply adds two numbers. This is to be used as a test for other functions.
    '''
    u = x+y #NO CONSTANTS NEEDED
    return(u)



def two_dim_sine(x,y,constants):
    '''
    A function which initialises the state to a standard two dimensional wave
    '''
    L, A, n, m = constants #IMPORTANT
    u = A*np.sin(n*np.pi*x/L)*np.sin(m*np.pi*y/L)
    return(u)

def random_amplitude(x,y,constants):
    '''
    A function which generates a random amplitude for each particle on the membrane
    '''
    lower, upper = constants #IMPORTANT
    u = random.uniform(lower, upper)
    return(u)


def array_3d_plot(array, L, maximum):
    '''
    Plots an array onto a 3D graph

    Parameters
    ----------
    array: np.array
        A square array
    L: float
        The length of the membrane
    maximum: float
        Scales the size of the graph to this value
    Returns
    -------
    A 3D plot of the array
    '''
    n = np.shape(array)[0]

    ypoints = np.zeros(n*n)

    x = np.arange(0, n)*L/(n-1)
    xpoints = x
    for i in range(1, n):

        ypoints[(n*i):(n*(i+1))] = i*L/(n-1)
        xpoints = np.append(xpoints, x)
    ypoints = np.flip(ypoints)

    upoints = np.concatenate(array)

    figure = plt.figure()

    ax = figure.add_subplot(projection = '3d')

    ax.scatter(xpoints,ypoints,upoints)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('U')
    ax.axes.set_zlim3d(bottom=-maximum, top=maximum) 
    plt.show()

    
