#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Bellkor.Parameters.Regularisation
"""
from Bellkor.Base.Generic import Generic


class RegularisationRates(Generic):
    """ Bellkor Regularisation Rates
    """

    b_u = 3e-5
    alpha_u = 5e-3
    b_i = 3e-3
    c_u = 3e-5
    b_ut = 5e-2
    c_ut = 5e-2
    b_ibin = 1e-4
    p = 5e-4
    q = 5e-4
    alpha_p = 1e-4

    def __repr__(self):
        return "< Default Regularisation Rates >"
