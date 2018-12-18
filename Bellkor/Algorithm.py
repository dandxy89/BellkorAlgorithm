#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" BellKor.Algorithm

BellKor Algorithm

"""
import datetime
import logging
import math
import random
import time
from typing import Tuple, Type

import numpy as np
import pandas as pd

from Bellkor.Base.BaseObject import Model
from Bellkor.Parameters.Gradients import Gradients
from Bellkor.Parameters.LearningRates import LearningRates
from Bellkor.Parameters.Parameters import Parameters
from Bellkor.Parameters.Regularisation import RegularisationRates
from Bellkor.Parameters.RowSettings import RowSettings
from Bellkor.Utils.Decorators import timeit, timeit_debug, test_method
from Bellkor.Utils.Exceptions import ModelValidationException, ModelIterationException

module_logger = logging.getLogger("BellKor.BellkorAlgorithm")
random.seed(612018)


class BellkorAlgorithm(Model):
    """ Implementation of the Original Bellkor Algorithm as presented here:

            Link: https://netflixprize.com/assets/GrandPrize2009_BPC_BellKor.pdf

    """
    PARAMS = Parameters

    START_TIME = None
    END_TIME = None

    LEARNING_RATES = LearningRates
    REGULARISATION = RegularisationRates

    GLOBAL_MEAN = None

    USERS = None
    ITEMS = None

    TIME_RANGE = None
    TIME_DIFF = None

    # Optimisation Values
    COST = 0
    TOTAL_ERROR = 0
    NUM = 0

    def __repr__(self):
        return "< Bellkor Algorithm >"

    @timeit
    def __init__(self, n_items: int, n_users: int, global_mean: int = None,
                 time_setting: dict = dict(Start=None, End=None), matrix_size: int = 20):
        """ Initialisation of the Bellkor Algorithm.

            :param n_items:         Number of Items
            :param n_users:         Number of Users
            :param global_mean:     Global Averaged Mean Rating
            :param time_data:       Time Dictionary containing the Start and End
            :param matrix_size:     Matrix Width

        """
        super().__init__()
        logger = logging.getLogger("BellKor.BellkorAlgorithm.__init__")
        logger.debug("Initialisation of the Bellkor Algorithm started.")

        # Create the Arrays of Users and Item Lists
        self.USERS = np.arange(n_users)
        self.ITEMS = np.arange(n_items)

        # Update the Global Mean Parameter
        if global_mean is not None:
            self.GLOBAL_MEAN = global_mean
            logger.debug("Global Mean stored.")

        # Set the Time parameters
        if time_setting["Start"] is not None and time_setting["End"] is not None:
            self.START_TIME = int(time_setting["Start"])
            self.END_TIME = int(time_setting["End"])
            self.TIME_DIFF = self.END_TIME - self.START_TIME
            dt_rng = list(map(lambda x: int(time.mktime(x.timetuple())),
                              pd.date_range(start=datetime.datetime.fromtimestamp(self.START_TIME),
                                            end=datetime.datetime.fromtimestamp(self.END_TIME),
                                            freq="D").tolist()))
            self.TIME_RANGE = np.arange(len(dt_rng))
            self.TIME_MAP = dict(zip(dt_rng, np.arange(self.TIME_RANGE.shape[0])))
            logger.debug("Time Parameters stored.")

        # Define the User Parameters
        for user in self.USERS:
            # For each User add their Parameters
            self.PARAMS.b_u[user] = 0
            self.PARAMS.alpha_u[user] = 0
            self.PARAMS.c_u[user] = 1
            self.PARAMS.p[user] = np.random.rand(matrix_size) * 1e-2
            self.PARAMS.alpha_p[user] = np.random.rand(matrix_size) * 1e-2

        # Create the Time bases User parameters
        self.PARAMS.b_ut = np.zeros(shape=(self.USERS.shape[0], self.TIME_RANGE.shape[0]))
        self.PARAMS.c_ut = self.PARAMS.b_ut.copy()
        logger.debug("User Parameters stored.")

        # Define the Items Parameters
        for item in self.ITEMS:
            self.PARAMS.b_i[item] = 0
            self.PARAMS.q[item] = np.random.rand(matrix_size) * 1e-2

        # Create the Time based params for each Item
        self.PARAMS.b_ibin = np.tile(np.arange(30), reps=(self.ITEMS.shape[0], 1)) / 100
        logger.debug("Item Parameters stored.")

        # Validate the Algorithm has been instantated correctly
        self._validation()
        logger.debug("Initisation of the Bellkor Algorithm ended.")

    @timeit_debug
    def _validation(self):
        """ Ensure the Model has been Initialised Correctly

            :return:                True if Validation Passes

        """
        if self.START_TIME is None or self.END_TIME is None:
            raise ModelValidationException(msg="No time constants are known.")

        if self.TIME_DIFF is None:
            raise ModelValidationException(msg="Time difference hasn't been calculated.")

        if self.GLOBAL_MEAN is None:
            raise ModelValidationException(msg="Global Mean is not known.")

        if self.USERS is None or self.ITEMS is None:
            raise ModelValidationException(msg="Users or Items directory have not been initialised correctly.")

        if self.COST != 0 or self.TOTAL_ERROR != 0 or self.NUM != 0:
            self.COST, self.TOTAL_ERROR, self.NUM = 0, 0, 0

    @timeit_debug
    @test_method(enable=False, model="Algorithm", test="override_rates")
    def override_rates(self, lr: LearningRates = None, reg: RegularisationRates = None):
        """ Call this function before running the Bellkor Algorithm

            :param lr:              Learning Rate Settings
            :param reg:             Regularisation Rate Settings
            :return:                None

        """
        logger = logging.getLogger("BellKor.BellkorAlgorithm.override_rates")

        if lr is not None:
            logger.info("Updating the Learning Rates")
            self.LEARNING_RATES = lr

        if reg is not None:
            logger.info("Updating the Regularisation Rates")
            self.REGULARISATION = reg

    @timeit
    @test_method(enable=False, model="Algorithm", test="predict")
    def predict(self, x: np.ndarray, average_times: dict) -> np.ndarray:
        """ Predict the re-adjusted Rating in X.

            Info:

                x: is an Array with the columns in the order shown below.

            Columns:

                [Index, TimePeriod, User, Item, BaseRating]

            :param x:               Input Data
            :param average_times:   Dictionary of User -> Avg Time
            :return:                Model Predictions

        """
        logger = logging.getLogger("BellKor.BellkorAlgorithm.predict")

        # Early return if no data exists
        if x.shape[0] == 0:
            logger.error("Input data contained no rows.")
            return np.array([])

        # Collect the Results
        collected_results, t1 = [], time.time()

        for each_index in x[:, 0]:
            # Get the Row Settings
            rs = self.get_row_settings(inputs=x[int(each_index), :])

            # Run the Bellkor Algorithm
            prediction, updated_rs = self.run_bellkor(rs=rs, average_times=average_times)
            logger.debug("Prediction made: {} - Dev {}".format(prediction, updated_rs.Dev))

            # Collect Result
            collected_results.append([each_index, prediction])

        logger.info("Prediction Time took: {}s".format(time.time() - t1))
        # Return Results
        return np.array(collected_results)

    @timeit
    @test_method(enable=False, model="Algorithm", test="train")
    def train(self, x: np.ndarray, average_times: dict,
              sample_size: int = 1000, iterations: int = 10) -> Tuple[float, float]:
        """ Fit the Bellkor Algorithm with Stochastic Gradient Descent.

            Info:

                x: is an Array with the columns in the order shown below.

            Columns:

                [Index, TimePeriod, User, Item, BaseRating]

            :param x:               Input Data
            :param average_times:   Dictionary of User -> Avg Time
            :param sample_size:     Sample Size per Epoch
            :param iterations:      Number of Iterations
            :return:                None

        """
        logger = logging.getLogger("BellKor.BellkorAlgorithm.train")

        # Check that the number of Iterations is greater or less than 1
        if iterations <= 0:
            raise ModelIterationException(msg="Incorrect amount of Iterations passed to method.")
        else:
            self.NUM = 0

        # Iterate through each Epoch
        for epoch in np.arange(start=0, stop=iterations):
            logger.info("Running Epoch: {}".format(epoch + 1))
            t1 = time.time()

            # Sample from the Training Set Index
            for each_index in np.random.choice(x[:, 0], sample_size):
                logger.debug("Sampling Index: {} during Epoch: {}".format(int(each_index), epoch))

                # Get the given Row
                rs = self.get_row_settings(inputs=x[int(each_index), :])

                # Run the Bellkor Algorithm
                prediction, updated_rs = self.run_bellkor(rs=rs, average_times=average_times)
                logger.debug("Prediction made: {} - Dev {}".format(prediction, updated_rs.Dev))
                self.NUM += 1

                # Compute the Cost
                error = self.compute_cost(rating=rs.Rating, prediction=prediction, rs=updated_rs)
                logger.debug("Error: {}".format(error))

                # Update the parameters by Gradient Descent
                self.gradient_decent(error=error, rs=updated_rs)

            logger.info("Epoch: {} took: {}s".format(epoch, time.time() - t1))

        # Return Results
        return self.COST / self.NUM, self.TOTAL_ERROR / self.NUM

    @timeit_debug
    @test_method(enable=False, model="Algorithm", test="run_bellkor")
    def run_bellkor(self, rs: RowSettings, average_times: dict) -> Tuple[float, RowSettings]:
        """ Bellkor Algorithm

            :param rs:              Row and Parameters
            :param average_times:   Dictionary of User -> Avg Time
            :return:                Prediction

        """
        logger = logging.getLogger("BellKor.BellkorAlgorithm.run_bellkor")

        # Find the difference from the Average Review data
        delta = (rs.Time - average_times[rs.User])

        # Find the Sign
        sign = -1 if delta < 0 else 1

        # Rescale
        delta = abs(delta) / self.TIME_DIFF

        # Find the 'deviation'
        dev = sign * math.pow(delta, 0.4)
        rs.set_dev(dev=dev)

        # Find P
        P = rs.p + rs.alpha_p * dev

        # Calculate the Model Prediction
        output = self.GLOBAL_MEAN + rs.b_u + (rs.alpha_u * dev) + rs.b_ut + \
                 (rs.b_i + rs.b_ibin) * (rs.c_u + rs.c_ut) + np.dot(rs.q.T, P)

        logger.debug("Model Prediction: {}".format(output))
        return output, rs

    @timeit_debug
    @test_method(enable=False, model="Algorithm", test="compute_cost")
    def compute_cost(self, rating: float, prediction: float, rs: RowSettings) -> float:
        """ Compute the Error and Cost for a given rating and prediction

            :param rating:          Actual Rating
            :param prediction:      Model's Predicted Rating
            :param rs:              Row values
            :return:                Cost, Error

        """
        # Calculate the Error
        error = rating - prediction

        # Calculate the Cost
        self.COST += error ** 2

        # Include the Regularisation Terms too
        self.COST += (self.REGULARISATION.b_u * (rs.b_u ** 2) +
                      self.REGULARISATION.alpha_u * (rs.alpha_u ** 2) +
                      self.REGULARISATION.b_ut * (rs.b_ut ** 2) +
                      self.REGULARISATION.b_i * (rs.b_i ** 2) +
                      self.REGULARISATION.b_ibin * (rs.b_ibin ** 2) +
                      self.REGULARISATION.c_u * (rs.c_u - 1) ** 2 +
                      self.REGULARISATION.c_ut * (rs.c_ut ** 2) +
                      self.REGULARISATION.p * (rs.p ** 2) +
                      self.REGULARISATION.q * (rs.q ** 2) +
                      self.REGULARISATION.alpha_p * (rs.alpha_p ** 2))

        return error

    @timeit_debug
    def gradient_decent(self, error, rs: RowSettings):
        """ Update the Parameters using Gradient Decent

            :param error:       Computed Error
            :param rs:          Row values

        """
        logger = logging.getLogger("BellKor.BellkorAlgorithm.gradient_decent")

        # Compute the Gradients
        grads = self.get_gradients(rs=rs, error=error)

        self.PARAMS.b_u[rs.User] -= self.LEARNING_RATES.b_u * grads.b_u
        self.PARAMS.alpha_u[rs.User] -= self.LEARNING_RATES.alpha_u * grads.alpha_u
        self.PARAMS.b_i[rs.Movie] -= self.LEARNING_RATES.b_i * grads.b_i
        self.PARAMS.c_u[rs.User] -= self.LEARNING_RATES.c_u * grads.c_u
        self.PARAMS.b_ut[rs.User, rs.time_index] -= self.LEARNING_RATES.b_ut * grads.b_ut
        self.PARAMS.c_ut[rs.User, rs.time_index] -= self.LEARNING_RATES.c_ut * grads.c_ut
        self.PARAMS.b_ibin[rs.Movie, rs.BinVal] -= self.LEARNING_RATES.b_ibin * grads.b_ibin
        self.PARAMS.p[rs.User] -= self.LEARNING_RATES.p * grads.p
        self.PARAMS.q[rs.Movie] -= self.LEARNING_RATES.q * grads.q
        self.PARAMS.alpha_p[rs.User] -= self.LEARNING_RATES.alpha_p * grads.alpha_p

        logger.debug("Gradient Descent: U: {}, M: {}".format(rs.User, rs.Movie))

    @timeit_debug
    @test_method(enable=False, model="Algorithm", test="get_params")
    def get_params(self) -> Type[Parameters]:
        """ Get the Model Parameters

            :return:                Get the Internal Model parameters

        """
        return self.PARAMS

    @timeit_debug
    @test_method(enable=False, model="Algorithm", test="get_row_settings")
    def get_row_settings(self, inputs):
        """ Get the Row Settings

                [Index, TimePeriod, User, Item, BaseRating]

            :param inputs:          Array Row
            :return:                RowSettings

        """
        logger = logging.getLogger("BellKor.BellkorAlgorithm.get_row_settings")

        # Row Values
        user = int(inputs[2])
        movie = int(inputs[3])
        time_val = inputs[1]
        binval = int((time_val - self.START_TIME) / (self.TIME_DIFF / 30))

        # Get datetime Index
        time_index = int(time.mktime(datetime.datetime.fromtimestamp(time_val).date().timetuple()))
        time_index = int(self.TIME_MAP[time_index])

        # Collate the Row Settings
        rs = RowSettings(user=user,
                         movie=movie,
                         rating=inputs[4],
                         binval=binval,
                         time=time_val,
                         time_index=time_index,
                         b_u=self.PARAMS.b_u[user],
                         alpha_u=self.PARAMS.alpha_u[user],
                         b_i=self.PARAMS.b_i[movie],
                         c_u=self.PARAMS.c_u[user],
                         b_ut=self.PARAMS.b_ut[user, time_index],
                         c_ut=self.PARAMS.c_ut[user, time_index],
                         b_ibin=self.PARAMS.b_ibin[movie - 1, binval],
                         p=self.PARAMS.p[user],
                         q=self.PARAMS.q[movie],
                         alpha_p=self.PARAMS.alpha_p[user])

        logger.debug("Row Setting: {}".format(rs))
        return rs

    @timeit_debug
    @test_method(enable=False, model="Algorithm", test="get_gradients")
    def get_gradients(self, rs, error) -> Gradients:
        """ Compute the Gradients

            :param rs:              Row Settings
            :param error:           Compute Error
            :return:                Calculated Gradients

        """
        logger = logging.getLogger("BellKor.BellkorAlgorithm.get_gradients")

        # Calculate all the Gradients for each Parameter
        gradients = Gradients(b_u=-2 * error + 2 * self.REGULARISATION.b_u * rs.b_u,
                              alpha_u=2 * error * (-rs.Dev + 2 * self.REGULARISATION.alpha_u * rs.alpha_u),
                              b_ut=2 * error * (-1 + self.REGULARISATION.b_ut * rs.b_ut),
                              b_i=2 * error * (-rs.c_u - rs.c_ut + 2 * self.REGULARISATION.b_i * rs.b_i),
                              b_ibin=2 * error * (-rs.c_u - rs.c_ut + 2 * self.REGULARISATION.b_ibin * rs.b_ibin),
                              c_u=2 * error * (-rs.b_i - rs.b_ibin + 2 * self.REGULARISATION.c_u * (rs.c_u - 1)),
                              c_ut=2 * error * (-rs.b_i - rs.b_ibin + 2 * self.REGULARISATION.c_ut * rs.c_ut),
                              p=2 * error * (rs.q + 2 * self.REGULARISATION.p * rs.p),
                              q=2 * error * (rs.p + rs.alpha_p * rs.Dev + 2 * self.REGULARISATION.q * rs.q),
                              alpha_p=2 * error * (rs.q * rs.Dev + self.REGULARISATION.alpha_p * rs.alpha_p))

        logger.debug("Error: {} -  Gradients: {}".format(error, gradients))
        return gradients
