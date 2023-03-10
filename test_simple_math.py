#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 14:01:02 2023

@author: noumanahmad
"""

# test_simple_math.py

import simple_math

def test_simple_add():
    assert simple_math.simple_add(2, 3) == 5
  
def test_simple_sub():
    assert simple_math.simple_sub(5, 3) == 2

def test_simple_mult():
    assert simple_math.simple_mult(2, 3) == 6

def test_simple_div():
    assert simple_math.simple_div(6, 3) == 2

def test_poly_first():
    assert simple_math.poly_first(2, 3, 4) == 11

def test_poly_second():
    assert simple_math.poly_second(2, 3, 4, 5) == 31

print("Successfully run")
