import os
import subprocess
import sys
import pytest

from subprocess import check_output, Popen, PIPE

variants_data = [
        ([[[10, 10, 10], 'No'], [[10, -10, -10], 'No'], [[10, -5, -5], 'Yes']]),
        ([[[10, 5, -5], 'No'], [[10, -1, -1], 'No'], [[10, 1, -1], 'Yes'],
         [[10, 2.928932188, -2.928932188], 'Yes']]),
        ([[[10, 5, 6, -6], 'Yes'], [[10, 7, 9, 2], 'No'], [[10, 5, -3, 3], 'Yes'], 
         [[10, 5, 3, -3], 'No'], [[10, 5, 0, 0], 'Yes']]),
        ([[[20, 10, -1, 3], 'No'], [[10,5 , 3, 3], 'No'], [[10, 4, 3, 3], 'Yes'], 
         [[15, 10, 9, 8], 'Yes'], [[15, 12, 10, 11], 'Yes']]),
        ([[[10, 5, -5], 'Yes'], [[10, 7.07, -7.07], 'Yes'], [[12, -1, 9], 'No'], 
         [[12, -7, 1], 'Yes'], [[12, -8, 1], 'No']]),
        ([[[-2, -2], 'Yes'], [[-2, -1.9], 'No'], [[-2, -0.1], 'No'],
         [[-1.41, -1.4], 'Yes'], [[5, -2], 'No']]),
        ([[[10, -5, 5], 'Yes'], [[10, -10, 10.1], 'No'], [[10, 10, -10], 'Yes'],
         [[10, 0, 0], 'Yes'], [[10, 21, 23], 'No']]),
        ([[[10, 10, 10], 'Yes'], [[10, -10, -10], 'Yes'], [[10, 10, 5], 'Yes'], 
         [[10, 0, 0], 'No'], [[10, 10, 0], 'Yes'], [[10, -5, 6], 'No']]),
        ([[[10, -13, -2], 'Yes'], [[10, -13, -7], 'Yes'], [[10, -15, -15], 'No'],
         [[10, 4, 5], 'No'], [[10, 20, 20], 'Yes'], [[10, 15, 15], 'Yes']]),
        ([[[0, 0], 'No'], [[5, 5], 'No'], [[2, 2], 'Yes'],
         [[2, -2], 'Yes'], [[4, 3], 'Yes'], [[2, -1], 'No']]),
        ([[[10, 5, 0], 'Yes'], [[10, 5, -7], 'Yes'], [[10, -5, -4], 'No'],
         [[10, 5, 9], 'No'], [[10, 5, 9], 'No'], [[10, -10, 3], 'No']]),
        ([[[10, 1, 1], 'Yes'], [[10, 5, 5], 'No'], [[3.16, 1, 3], 'No'],
         [[10, -5, -5], 'Yes'], [[10, 1, -3], 'No'], [[10, 1, 3.1], 'Yes']]),
    ]

"""If num of variant without 0 then test starts for variants 
   with the same numbers
"""
variants = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

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
        
    assert out.strip() == expected_output

@pytest.mark.parametrize('indata', variants_data, ids=variants)
def test_start(indata):
    for inp in indata:
        generic_test_lab(getPath(), inp[0], inp[1])

def getPath():
    return '/home/apache/collab/examples_of_labs/1_2/1.2.2.cpp'