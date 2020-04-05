#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Testing the Bellkor Algorithm
"""
import pickle
import unittest

from Bellkor.Algorithm import BellkorAlgorithm


class TestBellkorAlgorithm(unittest.TestCase):
    """ Testing the Bellkor Algorithm
    """

    # def setUp(self):
    #     with open("test_data/INIT_PARAMETERS.pickle", 'rb') as handle:
    #         self.LOAD_INIT = pickle.load(handle)

    # def test_bellkor_initialisation(self):
    #     # Initialise the Algorithm
    #     bk1 = BellkorAlgorithm(**self.LOAD_INIT)
    #
    #     self.assertEqual(bk1.START_TIME, 789609600)
    #     self.assertEqual(bk1.END_TIME, 1427842800)
    #     self.assertEqual(len(bk1.PARAMS.p), 138493)


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    unittest.main(testRunner=runner)
