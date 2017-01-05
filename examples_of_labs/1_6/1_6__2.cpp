#include <iostream>

using namespace std;

int main()
{
    int number;
    cin >> number;
    unsigned char n = static_cast<unsigned char>(number);

    if ((n & 1) > 0)
        cout << '1' << '\n';
    else
        cout << '0' << '\n';
    if ((n & (1 << 7)) > 0)
        cout << '1' << '\n';
    else
        cout << '0' << '\n';

    unsigned char inversedN = (n ^ (1 << 2)) ^ (1 << 4);
    cout << inversedN + 0 << '\n';

    return 0;
}
