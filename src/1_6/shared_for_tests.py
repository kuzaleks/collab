#!/usr/bin/python

''' Shared methods for tests of task 6 of lab 1(difficulty B)
'''


import os
import re
import subprocess
import sys

from subprocess import check_output, Popen, PIPE


def lab_testing(path_to_bin, arg, expected_output):
    '''
    '''
    task = Popen([path_to_bin], stdout=PIPE, stdin=PIPE, stderr=PIPE)

    out, err = task.communicate(input="\n".join(str(arg)))

    result = re.sub("\n", ' ', out.strip('\n'))# ? is it needed

    output = []
    for i in range(len(expected_output)):
        line = re.search(r'.*bit.*:\s*(\d+)', result)
        output.append(line.group(1))
        result = result[20:]# problem here

    for i in range(len(expected_output)):
        assert result[i] == expected_output[i]


def compile_lab(path_to_src):
    """Returns path to compiled file, compiles using g++"""
    # TODO: change '/temp' and '1_6.out' for more flexibility
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
        raise
    return path_to_bin
