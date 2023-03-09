"""
A collection of simple math operations
"""


"""
This is the name of this file in python simple_math.py
===============

A simple module for basic mathematical operations and polynomial functions.

Functions
---------
simple_add(a, b):
    Add two numbers `a` and `b` and return the result.

simple_sub(a, b):
    Subtract `b` from `a` and return the result.

simple_mult(a, b):
    Multiply `a` and `b` and return the result.

simple_div(a, b):
    Divide `a` by `b` and return the result.

poly_first(x, a0, a1):
    Evaluate a first degree polynomial with coefficients `a0` and `a1` at `x`.

poly_second(x, a0, a1, a2):
    Evaluate a second degree polynomial with coefficients `a0`, `a1`, and `a2` at `x`.

Examples
--------
>>> simple_add(2, 3)
5
>>> simple_mult(-1, 5)
-5
>>> poly_first(2, 1, 2)
5

Notes
-----
This module assumes that the input arguments are numeric types and does not perform any input validation.
"""

def simple_add(a, b):
    return a + b

def simple_sub(a, b):
    return a - b

def simple_mult(a, b):
    return a * b

def simple_div(a, b):
    return a / b

def poly_first(x, a0, a1):
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    return poly_first(x, a0, a1) + a2*(x**2)
