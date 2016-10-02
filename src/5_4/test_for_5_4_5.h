// Unittests for task:  part B lab 5 ex 4 variant 5
//
// Вычислить корень уравнения f(x) = 0 на отрезке [a; b] с точностью
//  E =10–6, используя  заданный метод (М = 1 – метод половинного
//  деления, М = 2 – метод касательных, М = 3 – метод хорд) для заданных
//  функций.
// Вычисление корня уравнения оформить в виде функции с функциональным
//  параметром, параметры a, b, E, s – в виде аргументов по умолчанию.
// Результат представить в виде таблицы (s – значение параметра,
//  х – вычисленный корень уравнения, f(x) – значение функции в найденной
//  точке х, k_iter – количество итераций цикла для получения корня с
//  заданной точностью):

#ifndef TEST_FOR_5_4_5_H
#define TEST_FOR_5_4_5_H

#include <cmath>
#include <cxxtest/TestSuite.h>
#include "headerWithCustomFunctions.h"
#include "simpleFunctionsForTests.h"

#define MAXIMUM_Deviation 1e-6

typedef double (*Function)(double);
typedef double (*FunctionWithArg)(double, float);

class testSuite : public CxxTest::TestSuite
{
    public:
        // tests of point A
        void testALinear()
        {
            // k_iter used in custom's rootOfEquation(),
            //  value isn't important to us
            int k_iter = 0;
            TS_ASSERT_DELTA(rootOfEquation(linearEquation, 0, 2.1, 1e-6,
             k_iter), 1.0, MAXIMUM_Deviation);
        }

        void testAQuadratic()
        {
            // k_iter used in custom's rootOfEquation()
            int k_iter = 0;
            TS_ASSERT_DELTA(rootOfEquation(quadraticEquation, 0.5, 3.6, 1e-6, k_iter), 2.0, MAXIMUM_Deviation);
        }

        void testACubic()
        {
            // k_iter used in custom's rootOfEquation()
            int k_iter = 0;
            TS_ASSERT_DELTA(rootOfEquation(cubicEquation, 1.1, 5.0, 1e-6,
             k_iter), 3.0, MAXIMUM_Deviation);
        }

        void testACorrectnessOfRoot()
        {
            // k_iter used in custom's rootOfEquation()
            int k_iter = 0;
            // check if f(x) == 0
            TS_ASSERT_LESS_THAN_EQUALS(functionA(rootOfEquation(functionA,
             -3.0, 0.0, 1e-6, k_iter)), MAXIMUM_Deviation);
        }

        void testADeviationOfRoot()
        {
            // k_iter used in custom's rootOfEquation()
            int k_iter = 0;
            TS_ASSERT_DELTA(rootOfEquation(functionA, -3.0, 0.0, 1e-6,
             k_iter), equationRoot(functionA, -3.0, 0.0, 1e-6),
             MAXIMUM_Deviation);
        }

        // tests of point B
        void testBLinear()
        {
            // k_iter used in custom's rootOfEquation()
            //  value isn't important to us
            int k_iter = 0;
            TS_ASSERT_DELTA(rootOfEquation(linearEquation, 0.5, 4.5, 4.0,
             1e-6, k_iter), 1.0, MAXIMUM_Deviation);
        }

        void testBQuadratic()
        {
            // k_iter used in custom's rootOfEquation()
            int k_iter = 0;
            TS_ASSERT_DELTA(rootOfEquation(quadraticEquation, 0.5, 3.7,
             4.0, 1e-6, k_iter), 2.0, MAXIMUM_Deviation);
        }

        void testBCubic()
        {
            // k_iter used in custom's rootOfEquation()
            int k_iter = 0;
            TS_ASSERT_DELTA(rootOfEquation(cubicEquation, 1.0, 5.2, 4.0,
             1e-6, k_iter), 3.0, MAXIMUM_Deviation);
        }

        void testBCorrectnessOfRoot()
        {
            // k_iter used in custom's rootOfEquation()
            int k_iter = 0;
            // check if f(x) == 0
            TS_ASSERT_LESS_THAN_EQUALS(functionB(rootOfEquation(functionB,
             0.5, 0.8, 1.6, 1e-6, k_iter), 1.6), MAXIMUM_Deviation);
        }

        void testBDeviationOfRoot()
        {
            // k_iter used in custom's rootOfEquation()
            int k_iter = 0;
            TS_ASSERT_DELTA(rootOfEquation(functionB, 0.5, 0.8, 1.6, 1e-6,
             k_iter), equationRoot(functionB, 0.5, 0.8, 1.6, 1e-6),
             MAXIMUM_Deviation);
        }

    private:
        // Reference standards functions of finding root
        //  Newton's method
        double equationRoot(Function function, float boundaryA,
         float boundaryB, double accuracyE)
        {
            // 'almostRoot' is approximation of root
            double root = (boundaryA + boundaryB) / 2, almostRoot;
            do
            {
                almostRoot = root;
                root = almostRoot - function(almostRoot) / 
                 derivative(function, almostRoot);
            }
            while(abs(root - almostRoot) > accuracyE);

            // for tracking of values (<iostream> must be included)
            //std::cout << " root = " << root << "  -- ";
            //std::cout << " f(x) = " << function(root) << "\n";

            return root;
        }

        double equationRoot(FunctionWithArg function, float boundaryA,
         float boundaryB, float argument, double accuracyE)
        {
            // 'almostRoot' is approximation of root
            double root = (boundaryA + boundaryB) / 2, almostRoot;
            do
            {
                almostRoot = root;
                root = almostRoot - function(almostRoot, argument) / 
                 derivative(function, almostRoot, argument);
            }
            while(abs(root - almostRoot) > accuracyE);

            // for tracking of values (<iostream> must be included)
            //std::cout << " root = " << root << "  -- ";
            //std::cout << " f(x) = " << function(root, argument) << "\n";

            return root;
        }

        // Reference standards functions of finding the derivative.
        double derivative(Function function, double x)
        {
            return ((function(x + 1e-6) - function(x)) / 1e-6);
        }

        double derivative(FunctionWithArg function, double x, float arg)
        {
            return ((function(x + 1e-6, arg) - function(x, arg)) / 1e-6);
        }
};

#endif // TEST_FOR_5_4_5_H
