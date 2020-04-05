#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Bellkor.Parameters.RowSettings
"""
from Bellkor.Base.Generic import Generic


class RowSettings(Generic):
    """ Row Settings
    """

    User = None
    Movie = None
    Rating = None
    BinVal = None
    Time = None
    Dev = None
    time_index = None

    def __init__(
        self,
        user: int,
        movie: int,
        binval: int,
        time: int,
        rating: float,
        b_u,
        alpha_u,
        b_i,
        c_u,
        b_ut,
        c_ut,
        b_ibin,
        p,
        q,
        alpha_p,
        time_index,
    ):
        """ Initialise with these parameters
        """
        super().__init__(
            b_u=b_u,
            alpha_u=alpha_u,
            b_i=b_i,
            c_u=c_u,
            b_ut=b_ut,
            c_ut=c_ut,
            b_ibin=b_ibin,
            p=p,
            q=q,
            alpha_p=alpha_p,
        )

        # Values from the Row
        self.User = user
        self.Movie = movie
        self.BinVal = binval
        self.Time = time
        self.Rating = rating
        self.time_index = time_index

    def __repr__(self):
        return "< Row Settings >"

    def set_dev(self, dev):
        self.Dev = dev
