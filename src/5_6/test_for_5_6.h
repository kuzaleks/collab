// Unittests for task:  part B lab 5 ex 6
//
// Дан массив чисел произвольной длины. Отсортировать массив заданными  методами.
// Для каждого метода сортировки определить число сравнений и перемещений (перестановок с одного места на другое)
//  элементов в процессе выполнения программы. Для тестирования программы заполнять массив значениями тремя способами:
//   по возрастанию,  по убыванию, случайным образом. 
// Сравнение элементов массива оформить отдельной функцией. Каждый метод сортировки,
//  каждый способ заполнения массивов  оформить отдельными функциями. Функции оформить в виде отдельного файла. 
// Сравнить экспериментальные результаты с известными теоретическими  оценками этих показателей для заданных методов сортировки. 

#ifndef TEST_FOR_5_6_H
#define TEST_FOR_5_6_H

#include <stdlib.h>
#include <time.h>

#include <cxxtest/TestSuite.h>
#include "headerWithCustomFunctions.h"

typedef void (*SortFunction)(int *array, int size, int &comparisons, int &movements);
typedef void (*QSortFunction)(int *array, int left, int right, int &comparisons, int &movements);

class testSuiteOne : public CxxTest::TestSuite
{
    public:
        void testTypicalCase()
        {
            differentCases(quickSort, 50, 77);
        }

        void testLessTrivialCase()
        {
            differentCases(quickSort, 5e4, 1000);
        }

    protected:
        // Quicksort takes arguments different from other sorts which we test, so we overload functions of cases.
        void differentCases(SortFunction sort, int dimension, int lim)
        {
            bestCase(sort, dimension);
            worstCase(sort, dimension);
            randomCase(sort, dimension, lim);
        }

        void differentCases(QSortFunction sort, int dimension, int lim)
        {
            bestCase(sort, dimension);
            worstCase(sort, dimension);
            randomCase(sort, dimension, lim);
        }

        void bestCase(SortFunction sort, int size)
        {
            int *array = new int[size];
            fillingArrayIncrease(array, size);
            int comparisons = 0, movements = 0;
            sort(array, size, comparisons, movements);
            TS_ASSERT(arraySorted(array, size));
            // количество перемещений не должно превосходить M(min)
            //TS_ASSERT_LESS_THAN_EQUALS(movements, M(min));

            delete [] array;
        }

        void bestCase(QSortFunction sort, int size)
        {
            int *array = new int[size];
            fillingArrayIncrease(array, size);
            int comparisons = 0, movements = 0;
            sort(array, 0, size - 1, comparisons, movements);
            TS_ASSERT(arraySorted(array, size));
            // количество перемещений не должно превосходить M(min)
            //TS_ASSERT_LESS_THAN_EQUALS(movements, M(min));

            delete [] array;
        }

        void worstCase(SortFunction sort, int size)
        {
            int *array = new int[size];
            fillingArrayDecrease(array, size);
            int comparisons = 0, movements = 0;
            sort(array, size, comparisons, movements);
            TS_ASSERT(arraySorted(array, size));
            // количество перемещений не должно превосходить M(max)
            //TS_ASSERT_LESS_THAN_EQUALS(movements, M(max));

            delete [] array;
        }

        void worstCase(QSortFunction sort, int size)
        {
            int *array = new int[size];
            fillingArrayDecrease(array, size);
            int comparisons = 0, movements = 0;
            sort(array, 0, size - 1, comparisons, movements);
            TS_ASSERT(arraySorted(array, size));
            // количество перемещений не должно превосходить M(max)
            //TS_ASSERT_LESS_THAN_EQUALS(movements, M(max));

            delete [] array;
        }

        void randomCase(SortFunction sort, int size, int lim)
        {
            int *array = new int[size];
            fillingArrayRandomly(array, size, lim);
            int comparisons = 0, movements = 0;
            sort(array, size, comparisons, movements);
            TS_ASSERT(arraySorted(array, size));
            // количество перемещений не должно превосходить M(cp)
            //TS_ASSERT_LESS_THAN_EQUALS(movements, M(cp));

            delete [] array;
        }

        void randomCase(QSortFunction sort, int size, int lim)
        {
            int *array = new int[size];
            fillingArrayRandomly(array, size, lim);
            int comparisons = 0, movements = 0;
            sort(array, 0, size - 1, comparisons, movements);
            TS_ASSERT(arraySorted(array, size));
            // количество перемещений не должно превосходить M(cp)
            //TS_ASSERT_LESS_THAN_EQUALS(movements, M(cp));

            delete [] array;
        }


        bool arraySorted(int *array, int size)
        {
            for (int i = 0; i < size - 1; ++i)
                if (array[i] > array[i + 1])
                    return false;

            return true;
        }


        void fillingArrayIncrease(int *array, int size)
        {
            for (int i = 0; i < size; i++)
                array[i] = i;
        }

        void fillingArrayDecrease(int *array, int size)
        {
            for (int i = 0; i < size; i++)
                array[i] = size - i;
        }

        void fillingArrayRandomly(int *array, int size, int lim)
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
