import math
import numpy as np
import random
import matplotlib.pyplot as plt
import Initialisation as init
import FiniteDifference as fd
import RepeatedSimulation as rs
import EnergyConservation as ec


def test_two_dim_sine():
    '''
    A function which returns a standard initial wave with velocity 0.
    '''
    L = 10 #Feel Free to Edit - The length of the square membrane - float
    A = 1 #FFtE - The initial maximum amplitude of the system - float
    n = 1 #FFtE - Wave number for x axis - integer
    m = 1 #FFtE - Wave number for y axis - integer
    npoints = 101 #FFtE - Number of particles along one axis of membrane, npoint^2 total points in membrane - Integer
    constants = np.array([L, A, n, m])
    complexarray = init.initialise(npoints, L, init.two_dim_sine, constants) #FFtE third and fourth entry - Generates a random state. You can choose an appropriate function to do so using Initialsation.py
    init.array_3d_plot(complexarray, L, A) 

def simple_amplitude_test():
    '''
    A function which compares the maximum amplitude of the simulation to an analytical solution
    '''
    L = 10 #Feel Free to Edit - The length of the square membrane - float
    A = 1 #FFtE - The initial maximum amplitude of the system - float
    n = 2 #FFtE - Wave number for x axis - integer
    m = 5 #FFtE - Wave number for y axis - integer
    c = 10 #FFtE - Propogation velocity of the membrane - float
    omega = c*math.pi*math.sqrt((n**2)+(m**2))/L #Angular Frequency of the system
    constants = np.array([L,A,n,m])
    npoints = 101 #FFtE - Number of particles along one axis of membrane, npoint^2 total points in membrane - Integer
    xhighpoint = int((npoints-1)/(2*n)) #Finds where along the x axis the first anti node is
    yhighpoint = int((npoints-1)/(2*m)) #Finds where along the y axis the first anti node is
    uarray = init.initialise(npoints, L, init.two_dim_sine, constants) #FFtE third and fourth entry - Generates a random state. You can choose an appropriate function to do so using Initialsation.py
    varray = np.zeros([npoints,npoints], dtype=float)
    timesteps = 1410 #FFtE - How many timesteps to iterate the system over - integer
    amparray = np.zeros([timesteps+1])
    deltat = 0.001 #FFtE - Time difference between timesteps - float
    deltax = L/(npoints-1) #Spacial difference between adjacent particles
    timearray = np.arange(timesteps+1)*deltat
    for i in range(timesteps):
        amparray[i] = uarray[xhighpoint, yhighpoint]
        uarray, varray = fd.full_finite_difference(uarray, varray, deltax, deltat, 0, c)
    amparray[-1] = np.max(uarray)
    actualamparray = (A*np.cos(omega*timearray))
    fig = plt.figure()
    plt.plot(timearray, amparray, color = 'red') #Plot of simulation
    plt.plot(timearray, actualamparray, color = 'blue') #Plot of analytical solution
    fig.supxlabel("Time (s)")
    fig.supylabel("Maximum Amplitude (m)")
    plt.show()
    fig = plt.figure()
    difference = amparray-actualamparray
    plt.plot(timearray, difference) #Plot of difference between systems
    fig.supxlabel("Time (s)")
    fig.supylabel("Difference in Maximum Amplitude (m)")
    plt.show()
    
 

def energy_conservation_test():
    '''
    A function which produces a graph which shows whether energy is conserved in a system or not
    '''
    random.seed(435)
    L = 10 #Feel Free to Edit - The length of the square membrane - float
    A = 1 #FFtE - The initial maximum amplitude of the system - float
    n = 2 #FFtE - Wave number for x axis - integer
    m = 5 #FFtE - Wave number for y axis - integer
    c = 10 #FFtE - Propogation velocity of the membrane - float
    omega = c*math.pi*math.sqrt((n**2)+(m**2))/L
    constants = np.array([L,A,n,m])
    lower = -1 #FFtE - Lower bound to randomly generate states
    upper = 1 #FFtE - Upper bound to randomly generate states
    bounds = np.array([lower, upper])
    npoints = 51 #FFtE - Number of particles along one axis of membrane, npoint^2 total points in membrane - Integer
    uarray = init.initialise(npoints, L, init.two_dim_sine, constants) #FFtE third and fourth entry - Generates a random state. You can choose an appropriate function to do so using Initialsation.py
    varray = np.zeros([npoints,npoints], dtype=float)
    deltax = (npoints-1)/L
    deltat = 0.004 #FFtE - Time difference between timesteps - float
    mu = 5 #FFtE - Damping coefficent - float
    timesteps = 10000 #FFtE - Timesteps to iterate over - integer
    mass = 1 #FFtE - Mass of individual particles on membrane - float
    ec.multiple_energy(uarray, varray, deltax, deltat, mu, timesteps, L, c, mass)


def first_and_last_test():
    '''
    A function which shows the plot of the first and last state of the simulation
    '''
    random.seed(435)
    L = 10 #Feel Free to Edit - The length of the square membrane - float
    A = 1 #FFtE - The initial maximum amplitude of the system - float
    n = 3 #FFtE - Wave number for x axis - integer
    m = 4 #FFtE - Wave number for y axis - integer
    c = 10 #FFtE - Propogation velocity of the membrane - float
    omega = c*math.pi*math.sqrt((n**2)+(m**2))/L #Angular Frequency of the system
    constants = np.array([L,A,n,m])
    lower = -1
    upper = 1
    bounds = np.array([lower, upper])
    npoints = 51 #FFtE - Number of particles along one axis of membrane, npoint^2 total points in membrane - Integer
    uarray = init.initialise(npoints, L, init.two_dim_sine, constants)
    maximum = np.max(uarray)
    reduced = rs.array_reduction(uarray, 41, 41)
    init.array_3d_plot(reduced, L, maximum)
    varray = np.zeros([npoints,npoints], dtype=float)
    timesteps = 1000 #FFtE - How many timesteps to iterate the system over - integer
    amparray = np.zeros([timesteps+1])
    deltat = 0.004 #FFtE - Time difference between timesteps - float
    deltax = L/(npoints-1) #Spacial difference between adjacent particles
    timearray = np.arange(timesteps+1)*deltat
    for i in range(timesteps):
        print(i)
        uarray, varray = fd.full_finite_difference(uarray, varray, deltax, deltat, 0, c)
    reduced2 = rs.array_reduction(uarray, 41, 41)
    init.array_3d_plot(reduced2, L, maximum)
