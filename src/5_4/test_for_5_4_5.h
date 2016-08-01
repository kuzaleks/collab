// Unittests for task:  part B lab 5 ex 4 variant 5
//
//  Вычислить корень уравнения f(x) = 0 на отрезке [a; b] с точностью E =10–6,
//   используя  заданный метод (М = 1 – метод половинного деления, М = 2 – метод касательных, М = 3 – метод хорд) для заданных функций.
//  Вычисление корня уравнения оформить в виде функции с функциональным параметром, параметры a, b, E, s – в виде аргументов по умолчанию.
//  Результат представить в виде таблицы (s – значение параметра, х – вычисленный корень уравнения,
//   f(x) – значение функции в найденной точке х, k_iter – количество итераций цикла для получения корня с заданной точностью):

#ifndef TEST_FOR_5_4_5_H
#define TEST_FOR_5_4_5_H

#include <cmath>
#include <cxxtest/TestSuite.h>
#include "headerWithCustomFunctions.h"

typedef double (*Function)(double);
typedef double (*FunctionWithArg)(double, float);

class testSuite : public CxxTest::TestSuite
{
    public:
        // for testFunction

    private:
        double derivativeOfFunction(Function function, double x)
        {
            return ((function(x + 1e-6) - function(x)) / 1e-6);
        }

        double derivativeOfFunction(FunctionWithArg function, double x, float argument)
        {
            return ((function(x + 1e-6, argument) - function(x, argument)) / 1e-6);
        }

        // reference standards functions of finding root
        // М = 2 – метод касательных
        double findingOfRoot(Function function, float boundaryA, float boundaryB, double accuracyE)
        {
            double root = (boundaryA + boundaryB) / 2, almostRoot;  // 'almostRoot' is approximation of root which help us find root
            do
            {
                almostRoot = root;
                root = almostRoot - function(almostRoot) / derivativeOfFunction(function, almostRoot);
            }
            while(abs(root - almostRoot) > accuracyE);

            return root;
        }
    
        double findingOfRoot(FunctionWithArg function, float boundaryA, float boundaryB, double s, double accuracyE)
        {
            double root = (boundaryA + boundaryB) / 2, almostRoot;  // 'almostRoot' is approximation of root which help us find root
            do
            {
                almostRoot = root;
                root = almostRoot - function(almostRoot, s) / derivativeOfFunction(funct, almostRoot, s);
            }
            while(abs(root - almostRoot) > accuracyE);

            return root;
        }
};

#endif // TEST_FOR_5_4_5_H
