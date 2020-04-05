#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Testing Bellkor Parameter Classes
"""
import unittest

from Bellkor.Parameters.Gradients import Gradients
from Bellkor.Parameters.LearningRates import LearningRates
from Bellkor.Parameters.Regularisation import RegularisationRates
from Bellkor.Parameters.RowSettings import RowSettings


class TestAllParameterClasses(unittest.TestCase):
    """ Testing all the Classes located in the Parameters sub-directory
    """

    def setUp(self):
        self.TEST_INPUTS = dict(
            b_u=1,
            alpha_u=2,
            b_i=3,
            c_u=4,
            b_ut=5,
            c_ut=6,
            b_ibin=7,
            p=8,
            q=9,
            alpha_p=10,
        )

    def test_gradients(self):
        # Define the Gradients
        g1 = Gradients(**self.TEST_INPUTS)

        # Assertions
        self.assertEqual(g1.b_u, 1)
        self.assertEqual(g1.alpha_p, 10)

    def test_learning_rates(self):
        # Assertions
        self.assertEqual(LearningRates.alpha_p, 1e-4)
        self.assertEqual(LearningRates.q, 5e-3)

    def test_regularisation(self):
        # Assertions
        self.assertEqual(RegularisationRates.c_u, 3e-05)
        self.assertEqual(RegularisationRates.c_ut, 0.05)

    def test_row_settings(self):
        # Setup
        rs = RowSettings(
            user=1,
            movie=100,
            binval=20,
            time=123123123123,
            rating=4.5,
            time_index=1,
            **self.TEST_INPUTS
        )

        # Assertions
        self.assertEqual(rs.User, 1)

        rs.set_dev(4.123123)

        # Further Assetions
        self.assertEqual(rs.Dev, 4.123123)


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    unittest.main(testRunner=runner)
