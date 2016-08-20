// Unittests for task:  part B lab 5 ex 6 variant 5

#ifndef TEST_FOR_5_6_5_H
#define TEST_FOR_5_6_5_H

#include <cxxtest/TestSuite.h>
#include "headerWithCustomFunctions.h"
#include "test_for_5_6.h"

class testSuiteTwo : public testSuiteOne
{
    public:
        virtual void testT()
        {
            TS_ASSERT_LESS_THAN_EQUALS(5, 6);
        }
        virtual void testO()
        {
            TS_ASSERT_LESS_THAN_EQUALS(5, 5);
        }
};

#endif // TEST_FOR_5_6_5_H
