#!/usr/bin/python

'''Unittests for task: part B lab 1 ex 6 variant 4
'''


from shared_for_tests import compile_lab
from shared_for_tests import lab_testing

import sys


def test_lab_1_6_4():
    path_to_bin = compile_lab('examples_of_labs/1_6/1_6.cpp')

    lab_testing(path_to_bin, 0, ['0', '0', '0', '130'])
    lab_testing(path_to_bin, 1, ['1', '0', '0', '131'])
    #lab_testing(path_to_bin, -1, ['1', '1', '1', '-131'])
    #lab_testing(path_to_bin, 32767, ['1', '1', '1', '32637'])
    #lab_testing(path_to_bin, -32764, ['0', '0', '0', '-32634'])
    #lab_testing(path_to_bin, -131, ['1', '1', '1', '-1'])
    #lab_testing(path_to_bin, 8141, ['1', '1', '0', '8015'])
