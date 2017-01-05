#include <iostream>

using namespace std;

int main()
{
    signed long n;
    cin >> n;

    if ((n & 1) > 0)
        cout << '1' << '\n';
    else
        cout << '0' << '\n';
    if ((n & (1 << 1)) > 0)
        cout << '1' << '\n';
    else
        cout << '0' << '\n';
    if ((n & (1 << 7)) > 0)
        cout << '1' << '\n';
    else
        cout << '0' << '\n';

    signed long inversedN = (n ^ (1 << 0)) ^ (1 << 1);
    cout << inversedN + 0 << '\n';

    return 0;
}
