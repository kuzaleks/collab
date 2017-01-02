#!/usr/bin/python

"""Unittests for task: part B lab 1 ex 6
"""

from shared_for_tests import compile_lab
from shared_for_tests import lab_verification

import pytest


variants = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

expected_results = [
    ({
        '0': ['0', '0', '10'],
        '1': ['1', '0', '11'],
        '-1': ['1', '1', '-11'],
        '10': ['0', '0', '0'],
        '108': ['0', '0', '102'],
        '-52': ['0', '1', '-58'],
        '33': ['1', '0', '43'],
    }, 'examples_of_labs/1_6/1_6_1.cpp'),
    ({
        '0': ['0', '0', '20'],
        '1': ['1', '0', '21'],
        '-1': ['1', '1', '235'],
        '20': ['0', '0', '0'],
        '129': ['1', '1', '149'],
        '255': ['1', '1', '235'],
        '196': ['0', '1', '208'],
    }, 'examples_of_labs/1_6/1_6_2.cpp'),
    ({
        '0': ['0', '0', '0', '72'],
        '1': ['1', '0', '0', '73'],
        '-1': ['1', '1', '1', '-73'],
        '72': ['0', '1', '0', '0'],
        '-10': ['0', '0', '1', '-66'],
        '62': ['0', '1', '0', '118'],
        '41': ['1', '1', '0', '97'],
    }, 'examples_of_labs/1_6/1_6_3.cpp'),
    ({
        '0': ['0', '0', '0', '130'],
        '1': ['1', '0', '0', '131'],
        '-1': ['1', '1', '1', '-131'],
        '128': ['0', '0', '0', '2'],
        '-988': ['0', '0', '1', '-858'],
        '30223': ['1', '1', '1', '30349'],
        '-6847': ['1', '0', '1', '-6717'],
    }, 'examples_of_labs/1_6/1_6_4.cpp'),
    ({
        '0': ['0', '0', '0', '384'],
        '1': ['1', '0', '0', '385'],
        '-1': ['1', '1', '1', '65151'],
        '128': ['0', '1', '0', '256'],
        '384': ['0', '1', '0', '0'],
        '21845': ['1', '0', '0', '21717'],
        '65535': ['1', '1', '1', '65151'],
    }, 'examples_of_labs/1_6/1_6_5.cpp'),
    ({
        '0': ['0', '0', '0', '-32766'],
        '1': ['1', '0', '0', '-32765'],
        '-1': ['1', '1', '1', '32765'],
        '128': ['0', '0', '0', '-32638'],
        '-917': ['1', '0', '1', '31849'],
        '26964': ['0', '1', '0', '-5802'],
        '-6847': ['1', '0', '1', '25923'],
    }, 'examples_of_labs/1_6/1_6_6.cpp'),
    ({
        '0': ['0', '0', '0', '32896'],
        '1': ['1', '0', '0', '32897'],
        '-1': ['1', '1', '1', '-32897'],
        '256': ['0', '0', '0', '33152'],
        '468633677': ['1', '0', '1', '468601037'],
        '-2978656': ['0', '0', '1', '-3011552'],
        '2147483647': ['1', '1', '1', '2147450751'],
    }, 'examples_of_labs/1_6/1_6_7.cpp'),
    ({
        '0': ['0', '0', '32896'],
        '1': ['1', '0', '32897'],
        '-1': ['1', '1', '4294934399'],
        '32897': ['1', '1', '1'],
        '177597': ['1', '1', '144701'],
        '594560': ['0', '0', '627200'],
        '8152429': ['1', '0', '8185325'],
    }, 'examples_of_labs/1_6/1_6_8.cpp'),
    ({
        '0': ['0', '0', '0', '130'],
        '1': ['1', '0', '0', '131'],
        '-1': ['1', '1', '1', '-131'],
        '128': ['0', '0', '0', '2'],
        '-16393': ['1', '0', '1', '-16523'],
        '505568242': ['0', '0', '0', '505568112'],
        '-132354394': ['0', '0', '0', '-132354524'],
    }, 'examples_of_labs/1_6/1_6_9.cpp'),
    ({
        '0': ['0', '0', '0', '1026'],
        '1': ['1', '0', '0', '1027'],
        '-1': ['1', '1', '1', '18446744073709550589'],
        '512': ['0', '0', '0', '1538'],
        '4771': ['1', '1', '0', '5793'],
        '70434916': ['0', '0', '1', '70435942'],
        '342834762': ['0', '1', '0', '342833736'],
    }, 'examples_of_labs/1_6/1_6_10.cpp'),
    ({
        '0': ['0', '0', '0', '3'],
        '1': ['1', '0', '0', '2'],
        '-1': ['1', '1', '1', '-4'],
        '131': ['1', '1', '1', '128'],
        '3': ['1', '1', '0', '0'],
        '51706': ['0', '1', '1', '51705'],
        '413736367': ['1', '1', '1', '413736364'],
    }, 'examples_of_labs/1_6/1_6_11.cpp'),
    ({
        '0': ['0', '0', '0', '32770'],
        '1': ['1', '0', '0', '32771'],
        '-1': ['1', '1', '1', '-32771'],
        '131': ['1', '1', '1', '32897'],
        '32770': ['0', '1', '0', '0'],
        '463104': ['0', '0', '0', '495874'],
        '-726071429': ['1', '1', '0', '-726038663'],
    }, 'examples_of_labs/1_6/1_6_12.cpp'),
]


@pytest.mark.parametrize('data,path_to_lab', expected_results, ids=variants)
def test_something(data, path_to_lab):
    path_to_bin = compile_lab(path_to_lab)
    for i in data:
        lab_verification(path_to_bin, [i], data[i])
