import os
import subprocess
import sys
import pytest

from subprocess import check_output, Popen, PIPE

variants_data = [
        ([[[8, 4, 6, 2], 'Yes'], [[2, 2, 6, 6], 'Yes'], [[2, 6, 4, 7], 'No'], 
         [[1, 5, 4, 7], 'Yes'], [[2, 2, 6, 2], 'Yes'], [[2, 9, 6, 2], 'No']]),
        ([[[8, 4, 6, 2], 'Yes'], [[2, 2, 6, 6], 'Yes'], [[2, 6, 4, 7], 'No'], 
         [[1, 5, 4, 7], 'Yes'], [[2, 2, 6, 2], 'Yes'], [[2, 9, 6, 2], 'No']]),
        ([[[8, 4, 6, 2], 'Yes'], [[2, 2, 6, 6], 'Yes'], [[2, 6, 4, 7], 'No'], 
         [[1, 5, 4, 7], 'Yes'], [[2, 2, 6, 2], 'Yes'], [[2, 9, 6, 2], 'No']]),
        ([[[8, 4, 6, 2], 'Yes'], [[2, 2, 6, 6], 'Yes'], [[2, 6, 4, 7], 'No'], 
         [[2, 5, 4, 7], 'Yes'], [[2, 2, 6, 2], 'Yes'], [[2, 9, 6, 2], 'No']]),
        ([[[8, 4, 6, 2], 'Yes'], [[2, 2, 6, 6], 'Yes'], [[2, 6, 4, 7], 'No'], 
         [[1, 5, 4, 7], 'Yes'], [[2, 2, 6, 2], 'Yes'], [[2, 9, 6, 2], 'No']]),
        ([[[8, 4, 6, 2], 'Yes'], [[2, 2, 6, 6], 'Yes'], [[2, 6, 4, 7], 'No'], 
         [[1, 5, 4, 7], 'Yes'], [[2, 2, 6, 2], 'Yes'], [[2, 9, 6, 2], 'No']]),
        ([[[8, 4, 6, 2], 'Yes'], [[2, 2, 6, 6], 'Yes'], [[2, 6, 4, 7], 'No'], 
         [[1, 5, 4, 7], 'Yes'], [[2, 2, 6, 2], 'Yes'], [[2, 9, 6, 2], 'No']]),
        ([[[8, 4, 6, 2], 'Yes'], [[2, 2, 6, 6], 'Yes'], [[2, 6, 4, 7], 'No'], 
         [[1, 5, 4, 7], 'Yes'], [[2, 2, 6, 2], 'Yes'], [[2, 9, 6, 2], 'No']]),
        ([[[8, 4, 6, 2], 'Yes'], [[2, 2, 6, 6], 'Yes'], [[2, 6, 4, 7], 'No'], 
         [[1, 5, 4, 7], 'Yes'], [[2, 2, 6, 2], 'Yes'], [[2, 9, 6, 2], 'No']]),
        ([[[8, 4, 6, 2], 'Yes'], [[2, 2, 6, 6], 'Yes'], [[2, 6, 4, 7], 'No'], 
         [[1, 5, 4, 7], 'Yes'], [[2, 2, 6, 2], 'Yes'], [[2, 9, 6, 2], 'No']]),
        ([[[8, 4, 6, 2], 'Yes'], [[2, 2, 6, 6], 'Yes'], [[2, 6, 4, 7], 'No'], 
         [[1, 5, 4, 7], 'Yes'], [[2, 2, 6, 2], 'Yes'], [[2, 9, 6, 2], 'No']]),
        ([[[8, 4, 6, 2], 'Yes'], [[2, 2, 6, 6], 'Yes'], [[2, 6, 4, 7], 'No'], 
         [[1, 5, 4, 7], 'Yes'], [[2, 2, 6, 2], 'Yes'], [[2, 9, 6, 2], 'No']]),
    ]

"""If num of variant without 0 then test starts for variants 
   with the same numbers
"""
variants = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

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
    return "/home/apache/collab/examples_of_labs/1_4/1.4.4.cpp"
