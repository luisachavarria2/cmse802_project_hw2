# mcs_module.py

""""
This module runs multiple Monte Carlo simulatons and calculates the 
energy progression for each simulation. 
It also averages the results to determine the stability of each material 

"""
import numpy as np
import matplotlib.pyplot as plt
from lattice import create_lattice
from monte_carlo_simulation import monte_carlo_step


def run_multiple_simulations(num_simulations, N_na, steps, T, material):
    """
    Run multiple Monte Carlo simulations and calculate the average and standard deviation of the energy.
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
