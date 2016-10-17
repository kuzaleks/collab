#!/usr/bin/python

'''Unittests for task: part B lab 1 ex 6 variant 5
'''


from shared_for_tests import compile_lab
from shared_for_tests import lab_testing

import sys


def test_lab_1_6_5():
    path_to_bin = compile_lab('examples_of_labs/1_6/1_6.cpp')

    lab_testing(path_to_bin, 0, ['0', '0', '0', '384'])
    lab_testing(path_to_bin, 1, ['1', '0', '0', '385'])
    #lab_testing(path_to_bin, 384, ['0', '1', '0', '0'])
    #lab_testing(path_to_bin, 32897, ['1', '1', '1', '33025'])
    #lab_testing(path_to_bin, 65535, ['1', '1', '1', '65151'])
    #lab_testing(path_to_bin, 21845, ['1', '0', '0', '21717'])
    #lab_testing(path_to_bin, 43866, ['0', '0', '0', '43738'])
