#include <iostream>

using namespace std;

int main()
{
    long n;
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

    long inversedN = (n ^ (1 << 1)) ^ (1 << 15);
    cout << inversedN + 0 << '\n';

    return 0;
}
