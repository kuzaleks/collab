// Unittests for task:  part B lab 2 ex 5 variant 4
//  4. Дано натуральное число n. Выяснить, можно ли представить n! в виде произведения трех последовательных целых чисел.

#include <cxxtest/TestSuite.h>
#include "headerWithCustomFunctions.h"

class testSuite : public CxxTest::TestSuite
{
    public:
        void testValidityOfInputValue(int n) //TODO I don't know how to check inputted value
        {
            TS_ASSERT(n >= min_);
            TS_ASSERT(n <= max_);
        }

        void testFactorialFunction()
        {
            for (int n = min_; n <= max_; n++)
                TS_ASSERT_EQUALS(factorial(n), factorialFunction(n));  // factorial(int) is a factorial custom function
        }

    private:
      // 'Etalon' function of factorial calculation.
        int factorialFunction(int n)
        {
            int result = 1;
            for (int i = 2; i <= n; i++)
                result *= i;

            return result;
        }

    public:
        testSuite()
        {
            min_ = 3;   // multiplicand = k * (k - 1) * (k - 2) and if k < 3 => multiplicand = 0
            max_ = 12;  // 12! = 479001600 and 13! > INT_MAX so max value of n = 12
        }

    private:
        int min_;
        int max_;
};
