// MyTestSuite1.h
#include <cxxtest/TestSuite.h>
#include <headers/func_square.h>

class MyTestSuite1 : public CxxTest::TestSuite
{
public:
    void testAddition(void)
    {
        TS_ASSERT_EQUALS(square(3), 9.0);
    }
};
