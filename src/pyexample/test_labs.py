"""
"""

import os
import subprocess
import sys

from subprocess import check_output, Popen, PIPE

import pytest


path_to_lab = 'examples_of_labs/sample_plus.cpp'

variants_data = [
    ([10, 2], '12'),
    ([10, 2], '8'),
]

variants = ["1", "2"]


def generic_test_lab(path_to_src, input_args, expected_output):
    """Compliles lab using g++ and runs it passing @input_args
    """
    path_to_bin = os.path.join('/tmp', 'sample.out')
    print path_to_bin
    try:
        comp = subprocess.check_output(
            ['g++',
             path_to_src,
             '-o',
             path_to_bin],
            stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError, e:
        print "Compilation stdout output:\n", e.output
        raise

    task = Popen([path_to_bin], stdout=PIPE, stdin=PIPE, stderr=PIPE)

    out, err = task.communicate(
        input="\n".join(str(arg) for arg in input_args)
    )
    actual_result = out.split()
        
    assert actual_result[-1] == expected_output


@pytest.mark.parametrize('indata,expected', variants_data, ids=variants)
def test_sample_lab(indata, expected):
    """Get data from different variants and pass them to test.
    Run py.test -k <variant> path/to/tests.py

    Please visit 
    http://doc.pytest.org/en/latest/example/parametrize.html#different-options-for-test-ids
    for details.
    """
    generic_test_lab(path_to_lab, indata, expected)
