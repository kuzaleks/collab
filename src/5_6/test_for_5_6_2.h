// Unittests for task:  part B lab 5 ex 6 variant 2

#ifndef TEST_FOR_5_6_2_H
#define TEST_FOR_5_6_2_H

#include <stdlib.h>
#include <time.h>

#include <cxxtest/TestSuite.h>
#include "shared_for_tests_5_6.h"
#include "header_with_custom_functions.h"


class testSuiteOne : public CxxTest::TestSuite
{
    public:
    void testAddition(void)
    {
        CShared::bestCaseTime(binaryInsertionSort, 100);
        CShared::worstCaseTime(binaryInsertionSort, 100);
        CShared::randomCaseTime(binaryInsertionSort, 100, 100);
    }
};

#endif // TEST_FOR_5_6_2_H
