# simulations.py

""""
This module runs multiple Monte Carlo simulations to calculate the energy progression 
over time and determine the stability of a given material.

The module performs the following tasks:
- Runs several Monte Carlo simulations for a specified material, number of sodium ions 
  (Na+), simulation steps, and temperature.
- Calculates and records the energy history for each simulation.
- Averages the energy results and computes the stability of the material.
- Plots the energy progression for each simulation.

By analyzing the energy behavior, this module helps assess the stability and behavior 
of materials such as MgO and FeO during ion insertion.

Author: Luisa Chavarria, Ai (ChatGPT)
Date: March 2025
"""

import numpy as np
import matplotlib.pyplot as plt
from lattice import create_lattice
from monte_carlo_simulation import monte_carlo_step


def run_multiple_simulations(num_simulations, N_na, steps, T, material):
    """
    Run multiple Monte Carlo simulations, calculate the average and standard deviation 
    of the energy, and plot the energy progression over time.

    Parameters:
    -----------
    num_simulations : int
        The number of Monte Carlo simulations to run.

    N_na : int
        The number of Na+ ions to insert during each simulation step.

    steps : int
        The number of steps to run in each simulation.

    T : float
        The temperature of the system (in Kelvin), which influences the Boltzmann factor 
        in the acceptance of moves.

    material : str
        The material being simulated, such as 'MgO' or 'FeO'

    
    Returns:
    --------
    energies : list
        A list containing the final energy of each simulation after the specified number 
        of steps.

    Notes:
    ------
    - Each simulation runs independently, and the energy history is plotted to visualize 
      the progression of energy over time.
    - The function does not return the detailed energy history but stores the final energy 
      value for each simulation.
    - This function relies on the `monte_carlo_step` function to perform each Monte Carlo 
      move and calculate energy changes.

    """
    
    energies = []
    for _ in range(num_simulations):
        lattice = create_lattice(material)
        total_energy = 0
        energy_history = []
        
        for _ in range(steps):
            lattice, total_energy = monte_carlo_step(lattice, N_na, T, material, total_energy)
            energy_history.append(total_energy)

        energies.append(total_energy)
        # Plot energy over time
        plt.plot(energy_history, label=f"{material}")
    return energies
