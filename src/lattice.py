# Lattice_module.py
""""
Module for the creation of the MgO and FeO lattice structure in 3D. 


MgO and FeO have a cubic structure or also named rocksalt similar to NaCl. 
It is one of the simplest crystal structures and can be a model for cation substitution. 

Each Mg2+ or Fe2+ ion have an octahedral coordination. This means that they are surrounded by 6 O2- ions

Author: Luisa Chavarria
Date: March 2025


"""
import numpy as np

def create_lattice(material="MgO", L=5):
    """
    Create a 3D lattice for MgO or FeO with alternating ions.
    MgO and FeO have a rocksalt structure with alternating cations (Mg/Fe) and anions (O).
    
    Material can be 'MgO' or 'FeO'.
    L is the lattice size (L x L x L).
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
