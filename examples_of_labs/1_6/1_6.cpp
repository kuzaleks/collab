#include <iostream>

using namespace std;

int main()
{
	unsigned long n;
	cin>>n;

	if ((n & 1) > 0)
		cout << '1' << endl;
	else
		cout << '0' << endl;
	if ((n & (1 << 1)) > 0)
		cout << '1' << endl;
	else
		cout << '0' << endl;
	if ((n & (1 << 15)) > 0)
		cout << '1' << endl;
	else
		cout << '0' << endl;

	cout << ((n ^ (1 << 1)) ^ (1 << 10)) << endl;

    return 0;
}
