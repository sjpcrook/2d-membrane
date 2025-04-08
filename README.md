[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/uGnJXzOT)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=13923643&assignment_repo_type=AssignmentRepo)

This simulation is designed to replicate a two-dimensional standing wave. The file named Simulator.py contains functions which can be adapted as neccessary to run the simulation and obtain a desired result, such as the energy conservation or a 3D plot of the system.
You can change the variables used in creating an intial state, or generate a completely random initial state to be analysed. The system automatically applies boundary conditions which fixes the edge of the membrane however.

Initialisation.py - Generates a starting membrane at t=0 when v=0. There are some methods to do so included and a plotting feature to visualise it.

FiniteDifference.py - Iterates the membrane over one time period

RepeatedSimulation.py - Iterated the membrane over multiple time periods. Includes methods to plot the membrane at different times.

EnergyConservation.py - Checks kinetic/potential/total energy of system at each time interval