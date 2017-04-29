#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int k, l, m, n;
    cin >> k >> l >> m >> n;
    if((k <= 0 || k > 8) || (l <= 0 || l > 8) ||
       (m <= 0 || m > 8) || (n <= 0 || n > 8))
       cout << "No" << endl;
    else if((abs(m - k) == 2 && abs(n - l) == 1) || 
            (abs(n - l) == 2 && abs(m - k) == 1))
        cout << "Yes" << endl;
    else
        cout << "No" << endl;
}