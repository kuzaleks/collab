#!/usr/bin/python

"""Unittests for task: part B lab 2 ex 1.1
"""

from shared_for_tests import compile_lab
from shared_for_tests import lab_verification

import pytest


variants = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

expected_results = [
    ({
        '516891': ['True'],
        '593231': ['True'],
        '577934': ['True'],
        '895888': ['False'],
        '293864': ['False'],
        '904898': ['False'],
        '434838': ['False'],
    }, 'examples_of_labs/2_1_1/2_1_1__1.cpp'),
    ({  # TODO: see var 1
        '607277': ['True'],
        '439393': ['True'],
        '844788': ['True'],
        '777777': ['False'],
        '444888': ['False'],
        '959595': ['False'],
        '742692': ['False'],
    }, 'examples_of_labs/2_1_1/2_1_1__2.cpp'),
    ({
        '321123': ['True'],
        '205502': ['True'],
        '842248': ['True'],
        '888888': ['True'],
        '848967': ['False'],
        '843368': ['False'],
        '996043': ['False'],
    }, 'examples_of_labs/2_1_1/2_1_1__3.cpp'),
    ({
        '139504': ['True'],
        '135792': ['True'],
        '246875': ['True'],
        '516835': ['False'],
        '137759': ['False'],
        '939395': ['False'],
        '888888': ['False'],
    }, 'examples_of_labs/2_1_1/2_1_1__4.cpp'),
    ({  # TODO: see var 1
        '': ['True'],
        '': ['True'],
        '': ['True'],
        '': ['True'],
        '': ['False'],
        '': ['False'],
        '': ['False'],
    }, 'examples_of_labs/2_1_1/2_1_1__5.cpp'),
    ({  # TODO: equals to var 4
        '': ['True'],
        '': ['True'],
        '': ['True'],
        '': ['True'],
        '': ['False'],
        '': ['False'],
        '': ['False'],
    }, 'examples_of_labs/2_1_1/2_1_1__6.cpp'),
    ({  # TODO: equals to var 1
        '': ['True'],
        '': ['True'],
        '': ['True'],
        '': ['True'],
        '': ['False'],
        '': ['False'],
        '': ['False'],
    }, 'examples_of_labs/2_1_1/2_1_1__7.cpp'),
    ({  # TODO: see var 5
        '': ['True'],
        '': ['True'],
        '': ['True'],
        '': ['True'],
        '': ['False'],
        '': ['False'],
        '': ['False'],
    }, 'examples_of_labs/2_1_1/2_1_1__8.cpp'),
    ({  # TODO: num 'k'
        '': ['True'],
        '': ['True'],
        '': ['True'],
        '': ['True'],
        '': ['False'],
        '': ['False'],
        '': ['False'],
    }, 'examples_of_labs/2_1_1/2_1_1__9.cpp'),
    ({  # TODO: equals to var 8
        '': ['True'],
        '': ['True'],
        '': ['True'],
        '': ['True'],
        '': ['False'],
        '': ['False'],
        '': ['False'],
    }, 'examples_of_labs/2_1_1/2_1_1__10.cpp'),
    ({  # TODO: num 'm'
        '': ['True'],
        '': ['True'],
        '': ['True'],
        '': ['True'],
        '': ['False'],
        '': ['False'],
        '': ['False'],
    }, 'examples_of_labs/2_1_1/2_1_1__11.cpp'),
    ({  # TODO: num 'k'
        '': ['True'],
        '': ['True'],
        '': ['True'],
        '': ['True'],
        '': ['False'],
        '': ['False'],
        '': ['False'],
    }, 'examples_of_labs/2_1_1/2_1_1__12.cpp'),
]


@pytest.mark.parametrize('data,path_to_lab', expected_results, ids=variants)
def test_something(data, path_to_lab):
    path_to_bin = compile_lab(path_to_lab)
    for i in data:
        lab_verification(path_to_bin, [i], data[i])
