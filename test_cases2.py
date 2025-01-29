#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample5 (self):
                self.assertEqual (1998, calc(2, 999))
        
        def test_sample6 (self):
                self.assertEqual (800, calc(2,400))

        def test_sample7 (self):
                self.assertEqual (-1, calc(1,999.1))
        
        def test_sample8 (self):
                self.assertEqual (-1, calc('A',800))


