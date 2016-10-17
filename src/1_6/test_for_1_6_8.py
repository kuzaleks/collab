#!/usr/bin/python

'''Unittests for task: part B lab 1 ex 6 variant 8
'''


from shared_for_tests import compile_lab
from shared_for_tests import lab_testing

import sys


def test_lab_1_6_8():
    path_to_bin = compile_lab('examples_of_labs/1_6/1_6.cpp')

    lab_testing(path_to_bin, 0, ['0', '0', '32896'])
    lab_testing(path_to_bin, 1, ['1', '0', '32897'])
    #lab_testing(path_to_bin, 32897, ['1', '1', '1'])
    #lab_testing(path_to_bin, 8152429, ['1', '0', '8185325'])
    #lab_testing(path_to_bin, -1, ['1', '1', '4294934399'])
    #lab_testing(path_to_bin, 177597, ['1', '1', '144701'])
    #lab_testing(path_to_bin, 594560, ['0', '0', '627200'])
