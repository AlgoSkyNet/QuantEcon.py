"""
Filename: test_approximation.py
Authors: Chase Coleman
Date: 07/18/2014

Tests for approximation.py file (i.e. tauchen)

"""
import sys
import os
import unittest
import numpy as np
from numpy.testing import assert_allclose
from quantecon.markov import tauchen


class TestTauchen(unittest.TestCase):

    def setUp(self):
        self.rho, self.sigma_u = np.random.rand(2)
        self.n = np.random.random_integers(3, 25)
        self.m = np.random.random_integers(4)
        self.tol = 1e-12

        mc = tauchen(self.rho, self.sigma_u, self.m, self.n)
        self.x, self.P = mc.state_values, mc.P

    def tearDown(self):
        del self.x
        del self.P

    def testShape(self):
        i, j = self.P.shape

        self.assertTrue(i == j)

    def testDim(self):
        dim_x = self.x.ndim
        dim_P = self.P.ndim

        self.assertTrue(dim_x == 1 and dim_P == 2)

    def test_transition_mat_row_sum_1(self):
        self.assertTrue(np.allclose(np.sum(self.P, axis=1), 1, atol=self.tol))

    def test_positive_probs(self):
        self.assertTrue(np.all(self.P) > -self.tol)

    def test_states_sum_0(self):
        self.assertTrue(abs(np.sum(self.x)) < self.tol)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTauchen)
    unittest.TextTestRunner(verbosity=2, stream=sys.stderr).run(suite)
