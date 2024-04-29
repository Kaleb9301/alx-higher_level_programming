#!/usr/bin/python3
"""
Defines lazy_matrix function
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matices

    Args:
        m_a: matrix a
        m_b: matrix b

    Returns:
        result of multiplication


    """


    return (np.matmul(m_a, m_b))
