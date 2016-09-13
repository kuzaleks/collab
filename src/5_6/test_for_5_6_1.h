// Unittests for task:  part B lab 5 ex 6 variant 1

#ifndef TEST_FOR_5_6_1_H
#define TEST_FOR_5_6_1_H

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
        CShared::bestCaseTime(bubbleSort, 100);
        CShared::worstCaseTime(bubbleSort, 100);
        CShared::randomCaseTime(bubbleSort, 100, 100);
    }
};

#endif // TEST_FOR_5_6_1_H
