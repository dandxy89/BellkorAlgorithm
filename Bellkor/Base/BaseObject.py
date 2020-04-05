#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Base Object
"""
import logging
from abc import ABCMeta, abstractmethod

from Bellkor.Utils.Decorators import timeit

module_logger = logging.getLogger("Bellkor.Base.BaseObject")


class Model:
    """ Base Model Class
    """
    PARAMS = None

    __metaclass__ = ABCMeta

    def __init__(self, *args):
        """ Initialisation of the Class
        """
        pass

    def __repr__(self):
        """ Used in the Python debugger
        """
        return "< Base Model Class >"

    @abstractmethod
    def train(self, *args):
        """ Base Training Method
        """
        pass

    @abstractmethod
    def predict(self, *args):
        """ Get a Prediction given an Input dataset
        """
        pass

    @abstractmethod
    def get_params(self):
        """ Get the Model Parameters
        """
        pass

    @timeit
    def pickle_parameters(self, file_name: str, full_path: str = None, default_folder: str = "MODEL_PARAMS") -> str:
        """ Pickle the Params

            :param file_name:       Name of the File to store the Pickle as
            :param full_path:       Full file path not including the file name
            :param default_folder:  Default folder name when creating one
            :return:                FilePath where its stored

        """
        import os
        import pickle
        logger = logging.getLogger("BellKor.BellkorAlgorithm.pickle_parameters")

        try:
            # Define the full file path
            if full_path is not None:
                path = f"{full_path}/{file_name}.pickle"
            else:
                # Make a New Directory
                os.mkdir(default_folder)
                path = f"{os.getcwd()}/{default_folder}/{file_name}.pickle"

            # Save the Parameters as a Pickle
            with open(path, 'wb') as handle:
                pickle.dump(self.PARAMS, handle, protocol=pickle.HIGHEST_PROTOCOL)

            logger.info(f"Save the Parameters @ {path}")
            return path

        except Exception as error:
            logger.error("Failure to save parameters", error)
            return "FAILURE"

    @timeit
    def load_parameters(self, file_path) -> bool:
        """ Load the Parameters from a filePath

            :param file_path:    File path to load Model Parameters from

        """
        import pickle
        logger = logging.getLogger("BellKor.BellkorAlgorithm.load_parameters")

        try:
            with open(file_path, 'rb') as handle:
                self.PARAMS = pickle.load(handle)

            logger.info(f"Loaded the Parameters from {file_path}")
            return True

        except Exception as error:
            logger.warning("Failure to load parameters", error)
            return False
