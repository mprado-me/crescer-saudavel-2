# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import unittest
from unittest import TestSuite


def get_test_suite_from_test_cases(test_cases):
    suite = TestSuite()
    for test_class in test_cases:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite


def get_test_suite_from_test_suites(suites):
    return unittest.TestSuite(suites)
