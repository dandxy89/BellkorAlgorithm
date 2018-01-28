#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Bellkor.Parameters.Gradients
"""
from Bellkor.Base.Generic import Generic


class Gradients(Generic):
    """ Bellkor Gradients
    """

    def __init__(self, b_u, alpha_u, b_i, c_u, b_ut, c_ut, b_ibin, p, q, alpha_p):
        """ Initialise with these parameters
        """
        super().__init__(b_u=b_u, alpha_u=alpha_u, b_i=b_i, c_u=c_u, b_ut=b_ut, c_ut=c_ut,
                         b_ibin=b_ibin, p=p, q=q, alpha_p=alpha_p)

    def __repr__(self):
        return "< Gradients >"
