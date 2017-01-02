#include <iostream>

using namespace std;

int main()
{
    signed short int n;
    cin >> n;

    if ((n & 1) > 0)
        cout << '1' << '\n';
    else
        cout << '0' << '\n';
    if ((n & (1 << 2)) > 0)
        cout << '1' << '\n';
    else
        cout << '0' << '\n';
    if ((n & (1 << 15)) > 0)
        cout << '1' << '\n';
    else
        cout << '0' << '\n';

    signed short int inversedN = (n ^ (1 << 1)) ^ (1 << 15);
    cout << inversedN + 0 << '\n';

    return 0;
}
