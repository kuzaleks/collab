#include <iostream>

using namespace std;

int main()
{
    unsigned long n;
    cin >> n;

    if ((n & 1) > 0)
        cout << '1' << '\n';
    else
        cout << '0' << '\n';
    if ((n & (1 << 1)) > 0)
        cout << '1' << '\n';
    else
        cout << '0' << '\n';
    if ((n & (1 << 15)) > 0)
        cout << '1' << '\n';
    else
        cout << '0' << '\n';

    unsigned long inversedN = (n ^ (1 << 1)) ^ (1 << 10);
    cout << inversedN + 0 << '\n';

    return 0;
}
