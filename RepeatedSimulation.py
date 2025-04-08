import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import Initialisation as init
import FiniteDifference as fd


def array_reduction(array, newrows, newcolumns):
    '''
    Reduces an array to a smaller size. Useful for plotting less demanding graphs

    Parameters
    ----------
    array: np.array
        A large array of elements
    newrows: int
        The desired amount of rows in the new array
    newcolumns: int
        The desired amount of columns in the new array

    Returns
    -------
    A 3D plot of the array
    '''
    new_array = np.zeros([newrows, newcolumns])
    rows, columns = np.shape(array)
    rowrange = range(0, rows, math.floor(rows/newrows))
    colrange = range(0, columns, math.floor(columns/newcolumns))
    for i in range(newrows):
        for j in range(newcolumns):
            new_array[i, j] = array[rowrange[i], colrange[j]]
    return(new_array)
    

def rect_3d_plot(array, L, T):
    '''
    Plots a rectangular array onto a 3D graph

    Parameters
    ----------
    array: np.array
        A square array
    L: float
        The length of the membrane
    T: float
        The time period over which the system is simulated

    Returns
    -------
    A 3D plot of the array
    '''
    timesteps1, npoints = np.shape(array)

    ypoints = np.zeros(timesteps1*npoints)

    x = np.arange(0, npoints)*L/(npoints-1)
    xpoints = x
    for i in range(1, timesteps1):
        ypoints[(timesteps1*i):(timesteps1*(i+1))] = i*T/(timesteps-1)
        xpoints = np.append(xpoints, x)
    ypoints = np.flip(ypoints)

    upoints = np.concatenate(array)

    figure = plt.figure()

    ax = figure.add_subplot(projection = '3d')
    ax.scatter(xpoints,ypoints,upoints)
    ax.set_xlabel('X')
    ax.set_ylabel('t')
    ax.set_zlabel('U')
    plt.show()


def animated_3d_plot(uarray, varray, deltax, deltat, mu, timesteps, L, mod, c):
    '''
    Plots multiple 3D graphs showing the evolution of the system

    Parameters
    ----------
    uarray: np.array
        A square array representing the initial position of each point
    varray: np.array
        A square array representing the initial velocity of each point
    deltax: float
        The space interval
    deltat: float
        The small time step to simulate the system over
    mu: float
        The damping coefficient
    timesteps: int
        How many time steps to simulate the system over
    L: float
        The length of the membrane
    mod: int
        How many intervals to simulate before plotting another graph
    c: float
        The propogation velocity
    Returns
    -------
    Multiple 3D plots showing the relation between x-y-u.
    '''
    for i in range(timesteps+1):
        maxu = np.max(uarray)
        print(np.array([maxu,i]))
        if(i % mod == 0):
            reduceduarray = array_reduction(uarray, 50, 50)
            init.array_3d_plot(uarray, L, A)
        uarray, varray = fd.full_finite_difference(uarray, varray, deltax, deltat, mu, c)

