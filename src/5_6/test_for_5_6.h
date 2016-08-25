// Unittests for task:  part B lab 5 ex 6
//
// Дан массив чисел произвольной длины. Отсортировать массив заданными
//  методами. Для каждого метода сортировки определить число сравнений и
//  перемещений (перестановок с одного места на другое) элементов в 
//  процессе выполнения программы. Для тестирования программы заполнять
//  массив значениями тремя способами:
//   по возрастанию,  по убыванию, случайным образом. 
// Сравнение элементов массива оформить отдельной функцией.
// Каждый метод сортировки, каждый способ заполнения массивов оформить
//  отдельными функциями. Функции оформить в виде отдельного файла. 
// Сравнить экспериментальные результаты с известными теоретическими
//  оценками этих показателей для заданных методов сортировки. 

#ifndef TEST_FOR_5_6_H
#define TEST_FOR_5_6_H

#include <stdlib.h>
#include <time.h>

#include <cxxtest/TestSuite.h>
#include "headerWithCustomFunctions.h"

typedef void (*SortFunction)(int *array, int size,
 int &comparisons, int &movements);
typedef void (*QSortFunction)(int *array, int left, int right,
 int &comparisons, int &movements);

class testSuiteOne : public CxxTest::TestSuite
{
    public:

    protected:
        // Quicksort takes arguments different from other sorts
        //  which we test, so we overload functions of cases.
//        void /*_*/(SortFunction sort, /*complexity,*/
//         clock_t (*situation)(SortFunction sort, int size))
//        {
//            TIME = situation(sort, 10);
//            TIME = situation(sort, 100);
//            TIME = situation(sort, 1000);
//            TIME = situation(sort, 10000);
//            TIME = situation(sort, 100000);
//        }

        clock_t bestCaseTime(SortFunction sort, int size)
        {
            int *array = new int[size];
            fillingIncrease(array, size);

            clock_t startTime = clock();
            int comparisons = 0, movements = 0;
            sort(array, size, comparisons, movements);
            clock_t endTime = clock();

            TS_ASSERT(isSorted(array, size));
            delete [] array;

            return endTime - startTime;
        }

        clock_t bestCaseTime(QSortFunction sort, int size)
        {
            int *array = new int[size];
            fillingIncrease(array, size);

            clock_t startTime = clock();
            int comparisons = 0, movements = 0;
            sort(array, 0, size - 1, comparisons, movements);
            clock_t endTime = clock();

            TS_ASSERT(isSorted(array, size));
            delete [] array;

            return endTime - startTime;
        }

        clock_t worstCaseTime(SortFunction sort, int size)
        {
            int *array = new int[size];
            fillingDecrease(array, size);

            clock_t startTime = clock();
            int comparisons = 0, movements = 0;
            sort(array, size, comparisons, movements);
            clock_t endTime = clock();

            TS_ASSERT(isSorted(array, size));
            delete [] array;

            return endTime - startTime;
        }

        clock_t worstCaseTime(QSortFunction sort, int size)
        {
            int *array = new int[size];
            fillingDecrease(array, size);

            clock_t startTime = clock();
            int comparisons = 0, movements = 0;
            sort(array, 0, size - 1, comparisons, movements);
            clock_t endTime = clock();

            TS_ASSERT(isSorted(array, size));
            delete [] array;

            return endTime - startTime;
        }

        clock_t randomCaseTime(SortFunction sort, int size, int lim)
        {
            int *array = new int[size];
            fillingRandomly(array, size, lim);

            clock_t startTime = clock();
            int comparisons = 0, movements = 0;
            sort(array, size, comparisons, movements);
            clock_t endTime = clock();

            TS_ASSERT(isSorted(array, size));
            delete [] array;

            return endTime - startTime;
        }

        clock_t randomCaseTime(QSortFunction sort, int size, int lim)
        {
            int *array = new int[size];
            fillingRandomly(array, size, lim);

            clock_t startTime = clock();
            int comparisons = 0, movements = 0;
            sort(array, 0, size - 1, comparisons, movements);
            clock_t endTime = clock();

            TS_ASSERT(isSorted(array, size));
            delete [] array;

            return endTime - startTime;
        }

        bool isSorted(int *array, int size)
        {
            for (int i = 0; i < size - 1; ++i)
                if (array[i] > array[i + 1])
                    return false;

            return true;
        }

        void fillingIncrease(int *array, int size)
        {
            for (int i = 0; i < size; i++)
                array[i] = i;
        }

        void fillingDecrease(int *array, int size)
        {
            for (int i = 0; i < size; i++)
                array[i] = size - i;
        }

        void fillingRandomly(int *array, int size, int lim)
        {
            srand((unsigned)time( NULL ));
            for (int i = 0; i < size; i++)
            {
                int sign = rand() % 2;
                if (sign == 0)
                    sign = -1;
                array[i] = rand() % lim * sign;
            }
        }
};

#endif // TEST_FOR_5_6_H
