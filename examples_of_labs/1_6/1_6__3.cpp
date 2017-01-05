#include <iostream>

using namespace std;

int main()
{
    int number;
    cin >> number;
    signed char n = static_cast<signed char>(number);

    if ((n & 1) > 0)
        cout << '1' << '\n';
    else
        cout << '0' << '\n';
    if ((n & (1 << 3)) > 0)
        cout << '1' << '\n';
    else
        cout << '0' << '\n';
    if ((n & (1 << 7)) > 0)
        cout << '1' << '\n';
    else
        cout << '0' << '\n';

    signed char inversedN = (n ^ (1 << 3)) ^ (1 << 6);
    cout << inversedN + 0 << '\n';

    return 0;
}
