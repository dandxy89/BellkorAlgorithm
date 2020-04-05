#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Bellkor.Parameters.Generic
"""
from abc import ABCMeta


class Generic:
    """ Generic Collection of Parameters
    """

    b_u = None
    alpha_u = None
    b_i = None
    c_u = None
    b_ut = None
    c_ut = None
    b_ibin = None
    p = None
    q = None
    alpha_p = None

    __metaclass__ = ABCMeta

    def __init__(self, b_u, alpha_u, b_i, c_u, b_ut, c_ut, b_ibin, p, q, alpha_p):
        self.b_u = b_u
        self.alpha_u = alpha_u
        self.b_i = b_i
        self.c_u = c_u
        self.b_ut = b_ut
        self.c_ut = c_ut
        self.b_ibin = b_ibin
        self.p = p
        self.q = q
        self.alpha_p = alpha_p

    def __repr__(self):
        return "< Generic Collection of Parameters >"
