#test_lattice_creation.py

""""
This module contains unit tests to verify the functionality of the `create_lattice` function.
It tests the creation of 5x5x5 lattice structures for both MgO and FeO, ensuring that the 
lattices alternate correctly between cations (Mg/Fe) and anions (O).

Each lattice is expected to follow a cubic "rocksalt" structure where:
- For MgO, Mg (0) and O (1) alternate positions.
- For FeO, Fe (0) and O (1) alternate positions.

The module also includes a test for invalid material inputs, ensuring that a ValueError is raised 
for unsupported materials.

Author: Luisa Chavarria, Ai (ChatGPT)
Date: March 2025

"""


import unittest
import numpy as np
from lattice_creation import create_lattice  # Import the function to test

class TestLatticeCreation(unittest.TestCase):

    def test_create_mgo_lattice(self):
        """ Test lattice creation for MgO (should alternate between Mg and O). """
        lattice = create_lattice("MgO", 5)
        
        # Check if the shape is correct
        self.assertEqual(lattice.shape, (5, 5, 5))
        
        # Verify alternating ions: Mg=0, O=1
        for i in range(5):
            for j in range(5):
                for k in range(5):
                    if (i + j + k) % 2 == 0:
                        self.assertEqual(lattice[i, j, k], 0)  # Mg
                    else:
                        self.assertEqual(lattice[i, j, k], 1)  # O

    def test_create_feo_lattice(self):
        """ Test lattice creation for FeO (should alternate between Fe and O). """
        lattice = create_lattice("FeO", 5)
        
        # Check if the shape is correct
        self.assertEqual(lattice.shape, (5, 5, 5))
        
        # Verify alternating ions: Fe=0, O=1
        for i in range(5):
            for j in range(5):
                for k in range(5):
                    if (i + j + k) % 2 == 0:
                        self.assertEqual(lattice[i, j, k], 0)  # Fe
                    else:
                        self.assertEqual(lattice[i, j, k], 1)  # O

    def test_invalid_material(self):
        """ Test that invalid material input raises an error. """
        with self.assertRaises(ValueError):
            create_lattice("NaCl", 5)  # Invalid material should raise ValueError

if __name__ == '__main__':
    unittest.main()
