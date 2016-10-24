#!/usr/bin/python

"""Shared methods for tests of task 6 of lab 1(difficulty B)
"""


import os
import subprocess
import sys

from subprocess import check_output, Popen, PIPE


def lab_verification(path_to_bin, args, expected_output):
    """Run compiled lab and
    compares received results with expected
    """
    task = Popen([path_to_bin], stdout=PIPE, stdin=PIPE, stderr=PIPE)

    out, err = task.communicate(
        input="\n".join(str(arg) for arg in args)
    )
    output = out.split()

    for i in range(len(expected_output)):
        assert output[i] == expected_output[i]


def compile_lab(path_to_src):
    """Returns path to compiled file
    compiles using g++
    """
    # ? maybe change '/temp' and '1_6.out' for more flexibility
    path_to_bin = os.path.join('/tmp', '1_6.out')
    print path_to_bin
    try:
        comp = subprocess.check_output(
            ['g++',
             '-std=c++11',
             path_to_src,
             '-o',
             path_to_bin],
            stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError, er:
        print "Compilation stdout output:\n", er.output
        raise# ? is it needed here
    return path_to_bin
