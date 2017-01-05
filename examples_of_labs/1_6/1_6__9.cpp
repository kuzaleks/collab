#include <iostream>

using namespace std;

int main()
{
    signed int n;
    cin >> n;

    if ((n & 1) > 0)
        cout << '1' << '\n';
    else
        cout << '0' << '\n';
    if ((n & (1 << 3)) > 0)
        cout << '1' << '\n';
    else
        cout << '0' << '\n';
    if ((n & (1 << 15)) > 0)
        cout << '1' << '\n';
    else
        cout << '0' << '\n';

    signed int inversedN = (n ^ (1 << 1)) ^ (1 << 7);
    cout << inversedN + 0 << '\n';

    return 0;
}
