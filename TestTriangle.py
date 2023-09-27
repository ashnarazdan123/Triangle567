# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(
            classifyTriangle(3, 4, 5), "Right", "3,4,5 is a Right triangle"
        )

    def testRightTriangleB(self):
        self.assertEqual(
            classifyTriangle(5, 3, 4), "Right", "5,3,4 is a Right triangle"
        )

    def testEquilateralTriangles(self):
        self.assertEqual(
            classifyTriangle(1, 1, 1), "Equilateral", "1,1,1 should be equilateral"
        )

    def testInvalidTrianglesA(self):
        self.assertEqual(
            classifyTriangle(0, 0, 1), "InvalidInput", "0,0,1 should be invalid"
        )

    def testInvalidTrianglesA(self):
        self.assertEqual(
            classifyTriangle(1, 2, 3), "NotATriangle", "1,2,3 should not be a triangle"
        )

    def testInvalidTrianglesB(self):
        self.assertEqual(
            classifyTriangle(1, 2, 4), "NotATriangle", "1,2,4 should not be a triangle"
        )

    def testInvalidTrianglesC(self):
        self.assertEqual(
            classifyTriangle(-1, 3, 1), "InvalidInput", "-1,3,1 should be invalid"
        )

    def testInvalidTrianglesD(self):
        self.assertEqual(
            classifyTriangle(0, 0, 0), "InvalidInput", "0,0,0 should be invalid"
        )

    def testInvalidTrianglesE(self):
        self.assertEqual(
            classifyTriangle(1.5, 6, 7),
            "InvalidInput",
            "1.5,6,7 should be invalid",
        )

    def testIsocelesTrianglesA(self):
        self.assertEqual(
            classifyTriangle(3, 3, 1), "Isoceles", "3,3,1 should be isosceles"
        )

    def testIsocelesTrianglesB(self):
        self.assertEqual(
            classifyTriangle(1, 3, 3), "Isoceles", "1,3,3 should be isosceles"
        )

    def testIsocelesTrianglesC(self):
        self.assertEqual(
            classifyTriangle(3, 1, 3), "Isoceles", "3,1,3 should be isosceles"
        )

    def testScaleneTriangles(self):
        self.assertEqual(
            classifyTriangle(7, 3, 6), "Scalene", "7,3,6 should be scalene"
        )


if __name__ == "__main__":
    print("Running unit tests")
    unittest.main()
