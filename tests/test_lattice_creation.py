#test_lattice_creation.py

""""
This module is designed to test if the create_lattice function correctly creates a 5x5x5 lattice
for MgO and FeO with alternating Mg/Fe (O) and O (1)

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
