#!/usr/bin/python

'''Unittests for task: part B lab 1 ex 6 variant 10
'''


from shared_for_tests import compile_lab
from shared_for_tests import lab_testing

import sys


def test_lab_1_6_10():
    path_to_bin = compile_lab('examples_of_labs/1_6/1_6.cpp')

    lab_testing(path_to_bin, 0, ['0', '0', '0', '1026'])
    lab_testing(path_to_bin, 1, ['1', '0', '0', '1027'])
    #lab_testing(path_to_bin, 32897, ['1', '0', '1', '33923'])
    #lab_testing(path_to_bin, 33923, ['1', '1', '1', '32897'])
    #lab_testing(path_to_bin, 93030418, ['0', '1', '1', '93031440'])
    #lab_testing(path_to_bin, 2627, ['1', '1', '0', '3649'])
    #lab_testing(path_to_bin, 18931, ['1', '1', '0', '19953'])
