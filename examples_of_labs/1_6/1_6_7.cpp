#include <iostream>

using namespace std;

int main()
{
    int n;
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

    int inversedN = (n ^ (1 << 7)) ^ (1 << 15);
    cout << inversedN + 0 << '\n';

    return 0;
}
