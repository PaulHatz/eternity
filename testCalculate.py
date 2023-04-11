import unittest
import math

import sys
import os
import inspect


import functions.formulas as f

class Testftions(unittest.TestCase):

    def test_factorial(self):
        self.assertAlmostEqual(f.factorial(5), math.factorial(5))
        self.assertAlmostEqual(f.factorial(0), math.factorial(0))
        self.assertAlmostEqual(f.factorial(12), math.factorial(12))
        self.assertAlmostEqual(f.factorial(21), math.factorial(21))

    def test_sqrt(self):
        self.assertAlmostEqual(f.calc_sqrt(5), math.sqrt(5))
        self.assertAlmostEqual(f.calc_sqrt(0), math.sqrt(0))
        self.assertAlmostEqual(f.calc_sqrt(12), math.sqrt(12))
        self.assertAlmostEqual(f.calc_sqrt(64), math.sqrt(64))
    
    def test_log(self):
        self.assertAlmostEqual(f.calc_log(10, 3), math.log(3, 10))
#        self.assertAlmostEqual(f.calc_log(10, 0), math.log(0, 10))
        self.assertAlmostEqual(f.calc_log(10, 2), math.log(2, 10))
        self.assertAlmostEqual(f.calc_log(10, 7), math.log(7, 10))

    def test_logbx(self):
        self.assertAlmostEqual(f.calc_log(5, 3), math.log(3, 5))
        self.assertAlmostEqual(f.calc_log(2, 6), math.log(6, 2))
        self.assertAlmostEqual(f.calc_log(12, 4), math.log(4, 12))
        self.assertAlmostEqual(f.calc_log(4, 4), math.log(4, 4))
    
    def test_gamma(self):
        self.assertAlmostEqual(f.gamma(2), math.gamma(2))
        self.assertAlmostEqual(f.gamma(7), math.gamma(7))
        self.assertAlmostEqual(f.gamma(19), math.gamma(19))
        self.assertAlmostEqual(f.gamma(11), math.gamma(11))
    
    def test_sin(self):
        self.assertAlmostEqual(f.sint(5), math.sin(5))
        self.assertAlmostEqual(f.sint(0), math.sin(0))
        self.assertAlmostEqual(f.sint(12), math.sin(12))
        self.assertAlmostEqual(f.sint(0.5), math.sin(0.5))

    def test_cos(self):
        self.assertAlmostEqual(f.cost(5), math.cos(5))
        self.assertAlmostEqual(f.cost(0), math.cos(0))
        self.assertAlmostEqual(f.cost(12), math.cos(12))
        self.assertAlmostEqual(f.cost(0.5), math.cos(0.5))

    def test_tan(self):
        self.assertAlmostEqual(f.tant(5), math.tan(5))
        self.assertAlmostEqual(f.tant(1), math.tan(1))
        self.assertAlmostEqual(f.tant(12), math.tan(12))
        self.assertAlmostEqual(f.tant(0.5), math.tan(0.5))

    def test_sinh(self):
        self.assertAlmostEqual(f.sinh(5), math.sinh(5))
        self.assertAlmostEqual(f.sinh(0), math.sinh(0))
        self.assertAlmostEqual(f.sinh(12), math.sinh(12))
        self.assertAlmostEqual(f.sinh(0.5), math.sinh(0.5))

if __name__ == '__main__':
    unittest.main()