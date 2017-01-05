#!/usr/bin/python

"""Shared methods for tests of task 1.1 of lab 2(difficulty B)
"""


import os
import subprocess

from subprocess import Popen, PIPE


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
    path_to_bin = os.path.join('/tmp', '2_1_1.out')
    print path_to_bin
    try:
        subprocess.check_output(
            ['g++',
             '-std=c++11',
             path_to_src,
             '-o',
             path_to_bin],
            stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError, er:
        print "Compilation stdout output:\n", er.output
        raise
    return path_to_bin
