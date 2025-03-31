# lattice.py
""""
Module for the creation of the MgO and FeO lattice structure in 3D. 


MgO and FeO have a cubic structure or also named rocksalt similar to NaCl. 
It is one of the simplest crystal structures and can be a model for cation substitution. 

Each Mg2+ or Fe2+ ion have an octahedral coordination. This means that they are surrounded by 6 oxygen (O2-) ions

Author: Luisa Chavarria, Ai (ChatGPT)
Date: March 2025


"""
import numpy as np

def create_lattice(material="MgO", L=5):
    """
    Generate a 3D lattice for MgO or FeO with alternating cations (Mg/Fe) and anions (O).
    
    The lattice structure follows the rocksalt arrangement, where the cations and anions alternate in a cubic arrangement. 
    The size of the lattice is defined by the parameter L, creating an L x L x L grid.

    Parameters:
    -----------
    material : str, optional
        The material to create the lattice for. It can be 'MgO' or 'FeO'. Default is 'MgO'.
    L : int, optional
        The size of the lattice (L x L x L). Default is 5.

    Returns:
    --------
    numpy.ndarray
        A 3D NumPy array representing the lattice, where 0 corresponds to the cation (Mg or Fe)
        and 1 corresponds to the anion (O).

    Notes:
    ------
    - The lattice alternates between cations and anions based on the sum of the indices.
    - MgO is modeled with Mg2+ cations and O2- anions.
    - FeO is modeled with Fe2+ cations and O2- anions.
    """


    lattice = np.zeros((L, L, L), dtype=int)  # 0 for Mg/Fe, 1 for O

    if material == "MgO":
        for i in range(L):
            for j in range(L):
                for k in range(L):
                    if (i + j + k) % 2 == 0:
                        lattice[i, j, k] = 0  # Mg
                    else:
                        lattice[i, j, k] = 1  # O
    elif material == "FeO":
        for i in range(L):
            for j in range(L):
                for k in range(L):
                    if (i + j + k) % 2 == 0:
                        lattice[i, j, k] = 0  # Fe
                    else:
                        lattice[i, j, k] = 1  # O
    return lattice
