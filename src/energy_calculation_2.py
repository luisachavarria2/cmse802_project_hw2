import numpy as np

def energy_change(i, j, k, lattice, target_ion="Mg"):
    """
    Calculate the Coulombic energy change when inserting Na+ at position (i, j, k).
    This function calculates the total energy due to Na+ interacting with its 
    nearest neighbors and the target ion (Mg or Fe).
    """

    # Constants (convert radii from picometers to meters)
    k_e = 8.99e9  # Coulomb's constant in N·m²/C²
    r_Mg = 72e-12  # Ionic radius of Mg2+ in meters  (72e-12)
    r_Fe = 78e-12  # Ionic radius of Fe2+ in meters  (78e-12)
    r_Na = 102e-12  # Ionic radius of Na+ in meters  (102e-12)
    r_O = 140e-12  # Ionic radius of O2- in meters  (140e-12)
    
    Q_Na = 1  # Charge of Na+
    Q_O = -2  # Charge of O2-
    
    # Select target ion parameters
    if target_ion == 'Mg':
        Q_target = 2  # Mg2+ charge
        r_target = r_Mg
    elif target_ion == 'Fe':
        Q_target = 2  # Fe2+ charge
        r_target = r_Fe
    else:
        raise ValueError(f"Unsupported target ion: {target_ion}")

    # Calculate the lattice size (assuming a cubic lattice)
    L = len(lattice)

    # Nearest neighbors in 3D (6 neighbors for a cubic lattice)
    neighbors = [(i + 1, j, k), (i - 1, j, k),
                (i, j + 1, k), (i, j - 1, k),
                (i, j, k + 1), (i, j, k - 1)]
    
    # Apply periodic boundary conditions to the neighbors
    neighbors = [(ni % L, nj % L, nk % L) for ni, nj, nk in neighbors]

    # Energy calculation between Na+ and O2- neighbors
    E_Na_O_total = 0
    for ox, oy, oz in neighbors:
        r_Na_O = np.sqrt((ox - i)**2 + (oy - j)**2 + (oz - k)**2)  # 3D distance
        E_Na_O = k_e * Q_Na * Q_O / r_Na_O  # Coulombic energy between Na and O
        E_Na_O_total += E_Na_O

    # Find the target ion position (Mg or Fe)
    target_position = None
    for x in range(L):
        for y in range(L):
            for z in range(L):
                if lattice[x, y, z] == target_ion:
                    target_position = (x, y, z)
                    break
            if target_position:
                break
        if target_position:
            break

    # Calculate the energy between Na+ and the target ion if found
    if target_position:
        tx, ty, tz = target_position
        r_Na_target = np.sqrt((tx - i)**2 + (ty - j)**2 + (tz - k)**2)  # Distance between Na+ and target ion
        E_Na_target = k_e * Q_Na * Q_target / r_Na_target  # Coulombic energy between Na and target ion
    else:
        E_Na_target = 0  # No target ion found

    # Return the total energy change
    delta_E = E_Na_O_total + E_Na_target
    return delta_E
