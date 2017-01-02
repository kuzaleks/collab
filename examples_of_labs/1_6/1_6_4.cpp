#include <iostream>

using namespace std;

int main()
{
    short int n;
    cin >> n;

    if ((n & 1) > 0)
        cout << '1' << '\n';
    else
        cout << '0' << '\n';
    if ((n & (1 << 3)) > 0)
        cout << '1' << '\n';
    else
        cout << '0' << '\n';
    if ((n & (1 << 13)) > 0)
        cout << '1' << '\n';
    else
        cout << '0' << '\n';

    short int inversedN = (n ^ (1 << 1)) ^ (1 << 7);
    cout << inversedN + 0 << '\n';

    return 0;
}
