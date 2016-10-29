import os
import subprocess
import sys

from subprocess import check_output, Popen, PIPE


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

#TODO: find method to replace [1,2..12] -> sys.argv 
def test_start():
    for variant in [1, 2, 10]:
        for input_arg in getParam(variant):
            generic_test_lab(getPath(variant), input_arg[0], input_arg[1])

def getPath(var):
    return 'examples_of_labs/1_2/1.2.' + str(var) + '.cpp'

  
def getParam(var):
    param = {};
    param = {
        1: [[[10, 10, 10], 'No'], [[10, -10, -10], 'No'], [[10, -5, -5], 'Yes']],
        2: [[[10, 5, -5], 'No'], [[10, -1, -1], 'No'], [[10, 1, -1], 'Yes'],
         [[10, 2.928932188, -2.928932188], 'Yes']],
        3: [[[10, 5, 6, -6], 'Yes'], [[10, 7, 9, 2], 'No'], [[10, 5, -3, 3], 'Yes'], 
         [[10, 5, 3, -3], 'No'], [[10, 5, 0, 0], 'Yes']],
        4: [[[20, 10, -1, 3], 'No'], [[10,5 , 3, 3], 'No'], [[10, 4, 3, 3], 'Yes'], 
         [[15, 10, 9, 8], 'Yes'], [[15, 12, 10, 11], 'Yes']],
        5: [[[10, 5, -5], 'Yes'], [[10, 7.07, -7.07], 'Yes'], [[12, -1, 9], 'No'], 
         [[12, -7, 1], 'Yes'], [[12, -8, 1], 'No']],
        6: [[[-2, -2], 'Yes'], [[-2, -1.9], 'No'], [[-2, -0.1], 'No'],
         [[-1.41, -1.4], 'Yes'], [[5, -2], 'No']],
        7: [[[10, -5, 5], 'Yes'], [[10, -10, 10.1], 'No'], [[10, 10, -10], 'Yes'],
         [[10, 0, 0], 'Yes'], [[10, 21, 23], 'No']],
        8: [[[10, 10, 10], 'Yes'], [[10, -10, -10], 'Yes'], [[10, 10, 5], 'Yes'], 
         [[10, 0, 0], 'No'], [[10, 10, 0], 'Yes'], [[10, -5, 6], 'No']],
        9: [[[10, -13, -2], 'Yes'], [[10, -13, -7], 'Yes'], [[10, -15, -15], 'No'],
         [[10, 4, 5], 'No'], [[10, 20, 20], 'Yes'], [[10, 15, 15], 'Yes']],
        10: [[[0, 0], 'No'], [[5, 5], 'No'], [[2, 2], 'Yes'],
         [[2, -2], 'Yes'], [[4, 3], 'Yes'], [[2, -1], 'No']],
        11: [[[10, 5, 0], 'Yes'], [[10, 5, -7], 'Yes'], [[10, -5, -4], 'No'],
         [[10, 5, 9], 'No'], [[10, 5, 9], 'No'], [[10, -10, 3], 'No']],
        12: [[[10, 1, 1], 'Yes'], [[10, 5, 5], 'No'], [[3.16, 1, 3], 'No'],
         [[10, -5, -5], 'Yes'], [[10, 1, -3], 'No'], [[10, 1, 3.1], 'Yes']],
    }
    return param[var]