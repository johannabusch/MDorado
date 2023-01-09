import unittest
import os
import numpy as np
import MDAnalysis
from mdorado import msd
from mdorado.data.datafilenames import (water_topology, 
                                        water_trajectory,
                                        test_unwrap,
                                        test_msd
                                            )

class TestProgram(unittest.TestCase):
    def test_unwrap(self):
        u = MDAnalysis.Universe(water_topology, water_trajectory, tpr_from_one=True)
        mol42grp = u.select_atoms("resid 42")
        mol42pos = msd.unwrap(universe=u, agrp=mol42grp, dimensionskey="xyz", cms=True)
        refunwrap = np.load(test_unwrap)
        self.assertIsNone(np.testing.assert_array_almost_equal(refunwrap, mol42pos))
    def test_msd(self):
        u = MDAnalysis.Universe(water_topology, water_trajectory)
        hgrp = u.select_atoms("name hw")
        hpos = msd.unwrap(universe=u, agrp=hgrp, dimensionskey="xyz", cms=False)
        hmsd = msd.msd(positions=hpos, dt=0.2) 
        refmsd = np.loadtxt(test_msd)
        self.assertIsNone(np.testing.assert_array_almost_equal(refmsd, hmsd))

if __name__ == '__main__':
        unittest.main()


