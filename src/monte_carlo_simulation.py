# 4_MonteCarlo_module

""""
This module implements the Monte Carlo simulation using the Metropolis-Hastings Algorithm. 
Sodium ions (Na+) are inserted into the lattice, and the energy change is used to determine
whether the configuration is accepted or rejected based on the Boltzmann factor


"""

import random
import numpy as np
import math
from energy_calculation_2 import energy_change

k_e = 8.99e9  # Coulomb's constant in N·m²/C²
r_Mg = 72e-12  # Ionic radius of Mg2+ in meters
r_Fe = 78e-12  # Ionic radius of Fe2+ in meters
r_Na = 102e-12  # Ionic radius of Na+ in meters
r_O = 140e-12  # Ionic radius of O2- in meters
k_B = 1.38e-23  # Boltzmann constant in J/K

# Boltzmann constant (J/K)
k_B = 1.38e-23

def monte_carlo_step(lattice, N_na, T, material, total_energy):
    """
    Perform a Monte Carlo step, inserting N_na sodium ions into the lattice and 
    updating the total energy using the Metropolis-Hastings algorithm.
    """
    # Boltzmann constant (J/K)
    k_B = 1.38e-23


    target_ion = 'Mg' if material == 'MgO' else 'Fe'
    
    # Only select positions of Mg (0) or Fe (0) for Na insertion
    ion_positions = [(i, j, k) for i in range(len(lattice)) for j in range(len(lattice)) for k in range(len(lattice)) 
                     if lattice[i, j, k] == 0]  # Only positions of Mg or Fe (cations)
    
    if len(ion_positions) == 0:
        return lattice, total_energy

    for _ in range(N_na):
        i, j, k = random.choice(ion_positions)
        delta_E = energy_change(i, j, k, lattice, target_ion)

        # Accept the move based on the energy difference and Boltzmann factor
        if delta_E < 0:
            lattice[i, j, k] = 2  # Replace with Na
            total_energy += delta_E
        else:
            probability = np.exp(-delta_E / (k_B * T))
            if random.random() < probability:
                lattice[i, j, k] = 2
                total_energy += delta_E

 return lattice, total_energy

