#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Testing the Base Objects
"""
import os
import unittest

from Bellkor.Base.BaseObject import Model


class TestAllBaseObjects(unittest.TestCase):
    """ Testing all the Classes located in the Base sub-directory
    """

    def setUp(self):
        self.base_methods_and_attributes = {"PARAMS", "get_params", "load_parameters", "pickle_parameters", "predict",
                                            "train"}

    def tearDown(self):
        # Attempt to remove the pickle file and folder...
        try:
            os.remove("MODEL_PARAMS/SAVE_PICKLE.pickle")
            os.removedirs("MODEL_PARAMS")
        except IOError:
            pass

    def test_base_model_init(self):
        # Setup
        base_model = Model()

        # Assertions
        self.assertEqual(len(self.base_methods_and_attributes), 6)
        self.assertEqual(len(set(base_model.__dir__()).intersection(self.base_methods_and_attributes)), 6)

    def test_pickle_saving(self):
        # Setup
        base_model2 = Model()
        base_model2.PARAMS = dict(Test=1, Dan=2)
        base_model2.pickle_parameters(file_name="SAVE_PICKLE")

        # Assertions
        assert os.path.isfile("MODEL_PARAMS/SAVE_PICKLE.pickle")

    def test_loading_pickle(self):
        # Setup
        base_model3 = Model()
        base_model3.load_parameters(file_path="test_data/LOADING_PICKLE.pickle")

        self.assertEqual(base_model3.PARAMS, {'Test': 1})


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    unittest.main(testRunner=runner)
