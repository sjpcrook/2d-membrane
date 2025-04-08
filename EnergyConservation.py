import math
import numpy as np
import matplotlib.pyplot as plt
import Initialisation as init
import FiniteDifference as fd
import RepeatedSimulation as rs

def energyofsystem(uarray, varray, c, mass, deltax):
    '''
    Finds the total energy of a system at a given time interval, assuming the mass at each point is 1kg

    Parameters
    ----------
    uarray: np.array
        A square array representing the position of a given point on the membrane
    varray: np.array
        A square array representing the velocity of a given point on the membrane
    c: float
        The propogation velocity
    mass: float
        The mass of each particle on the membrane
    deltax: float
        The distance between adjacent particles

    Returns
    -------
    energy: float
        The total energy of the system
    '''
    vsquared = varray*varray
    pointlength = np.shape(uarray)[0]
    kinetic = 0.5*mass*np.sum(vsquared)
    ubyx = np.zeros([pointlength, pointlength])
    ubyy = np.zeros([pointlength, pointlength])
    for x in range(pointlength-2):
        for y in range(pointlength-2):
            ubyx[x+1, y+1] = (uarray[x+2, y+1]-uarray[x, y+1])/(2*deltax)
            ubyy[x+1, y+1] = (uarray[x+1, y+2]-uarray[x+1, y])/(2*deltax)
    potential = 0.5*mass*(pointlength/(pointlength-1))*np.sum((ubyx*ubyx)+(ubyy*ubyy))*c*c
    energy = kinetic + potential
    print(kinetic)
    print(potential)
    return(energy)

def multiple_energy(uarray, varray, deltax, deltat, mu, timesteps, L, c, mass):
    '''
    Finds the total energy of a system throughout the simulation

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
        A positive number representing the damping coefficient
    timesteps: int
        How many time steps to simulate the system over
    L: float
        The length of the membrane
    c: float
        The propogation velocity
    mass: float
        The mass of each particle on the membrane

    Returns
    -------
    A graph showing how the total energy changes over time
    '''
    energy = np.zeros(timesteps+1)
    energy[0] = energyofsystem(uarray,varray, c, mass, deltax)
    for i in range(timesteps): 
        print(i)
        uarray, varray = fd.full_finite_difference(uarray, varray, deltax, deltat, mu, c)
        energy[i+1] = energyofsystem(uarray,varray, c, mass, deltax)
    xarray = np.arange(timesteps+1)*deltat
    plt.plot(xarray, energy)
    plt.xlabel("Time (s)")
    plt.ylabel("Energy (J)")
    plt.ylim([0, max(energy)*1.2])
    plt.title("Conservation of Energy in the System")
    plt.show()


