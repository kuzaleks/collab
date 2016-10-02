// The sample solution of the task B 2.5(4)
//
// 4. Дано натуральное число n. Выяснить, можно ли представить n! в виде произведения трех последовательных целых чисел.

#include <iostream>
#include <climits>

using namespace std;

int factorial(int n)
{
    int result = 1;
    for (int i = 1; i <= n; i++)
    {
        if (result * (i + 1) - INT_MAX > 0) {
            result = 0;
            break;
        }
        result *= i;
    }
    return result;
}

bool multiplication(int n)
{
    const int num = 3;
    int array[num];
    for (int i = 0; i < num; i++)
        array[i] = i + 1;
    int mult = 1;
    for (int i = 0; i < num; i++)
        mult *= array[i];
    while(mult < n)
    {
        mult /= array[0];
        for (int i = 0; i < num; i++)
            array[i]++;
        mult *= array[num - 1];
    }
    //cout << " numbers:\n";
    //for (int i = 0; i < num; i++)
    //    cout << " " << array[i];
    if (mult == n)
        return true;
    else
        return false;
}

// main() is commented out to solve the problem with multiple definition of `main' (main defined in generated runner.cpp)
/*int main()
{
    for (int i = 3; i <= 12; i++)
    {
        cout << i << ": ";
        if (multiplication(factorial(i)))
            cout << " TRUE\n";
        else
            cout << " FALSE\n";
    }

	return 0;
}*/
