#include <iostream>

using namespace std;

int main()
{
    int number;
    cin >> number;
    char n = static_cast<char>(number);

    if ((n & 1) > 0)
        cout << '1' << '\n';
    else
        cout << '0' << '\n';
    if ((n & (1 << 7)) > 0)
        cout << '1' << '\n';
    else
        cout << '0' << '\n';

    char inversedN = (n ^ (1 << 1)) ^ (1 << 3);
    cout << inversedN + 0 << '\n';

    return 0;
}
