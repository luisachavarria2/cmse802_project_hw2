# 4_MonteCarlo_module

""""
Module that implements the Monte Carlo simulation using the Metropolis-Hastings algorithm.

This module simulates the insertion of sodium ions (Na+) into a lattice structure. 
The energy change caused by inserting Na+ ions is computed, and the configuration is 
accepted or rejected based on the Metropolis-Hastings criterion, which involves 
using the Boltzmann factor to determine the probability of accepting an energy-increasing move.

Author: Luisa Chavarria, Ai (ChatGPT)
Date: March 2025

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
    Perform a single Monte Carlo step to insert sodium ions into the lattice and update the total energy.
    
    This function uses the Metropolis-Hastings algorithm to insert N_na sodium ions (Na+) 
    into the lattice. The energy change for each insertion is computed, and the ion insertion 
    is accepted or rejected based on the Boltzmann factor. The lattice and the total energy 
    of the system are updated accordingly.

    Parameters:
    -----------
    lattice : numpy.ndarray
        A 3D NumPy array representing the current lattice configuration, where cations 
        (Mg or Fe) are represented by 0, anions by 1, and Na+ ions (inserted during the simulation) 
        by 2.

    N_na : int
        The number of Na+ ions to insert in the current Monte Carlo step.

    T : float
        The temperature of the system (in Kelvin), used to calculate the Boltzmann factor.

    material : str
        The type of material being simulated. It can be 'MgO' or 'FeO', which determines the 
        target ion (Mg or Fe) for the energy calculations.

    total_energy : float
        The total energy of the system before the Monte Carlo step. This value is updated 
        after each ion insertion.

    Returns:
    --------
    tuple
        A tuple containing:
        - lattice : numpy.ndarray
            The updated lattice after the ion insertions.
        - total_energy : float
            The updated total energy of the system.

    Notes:
    ------
    - The function assumes that the lattice is a cubic grid with cations (Mg or Fe) at positions 
      marked by 0 and anions (O) marked by 1.
    - The energy change for each Na+ insertion is computed using the `energy_change` function from 
      the `energy_calculation_2` module.
    - The ion insertion is accepted if the energy change is negative, or if the Boltzmann probability 
      criterion is met for positive energy changes.

    Author: Luisa Chavarria, Ai (ChatGPT)
    Date: March 2025



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

