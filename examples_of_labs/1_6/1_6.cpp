#include <iostream>

using namespace std;

int main()
{
    unsigned short int number;
    cout << "n = ";
    cin >> number;

    cout<<"0th bit of number: " << (number & 1) << '\n';
    cout<<"7th bit of number: " << (number & (1 << 7)) << '\n';
    cout<<"15th bit of number: " << (number & (1 << 7)) << '\n';

    cout  << "number with 7th and 8th inverted bits: " <<
        ((number ^ (1 << 8)) ^ (1 << 7)) << '\n';

    return 0;
}
