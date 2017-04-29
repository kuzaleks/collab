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
    else if(k == m || l == n ||
            (abs(m-k) == abs(n - l)))
        cout << "Yes" << endl;
    else
        cout << "No" << endl;
}