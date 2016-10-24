#include <iostream>

using namespace std;

int main()
{
	long n;
	cin>>n;

	if ((n & 1) > 0)
		cout << '1' << endl;
	else
		cout << '0' << endl;
	if ((n & (1 << 1)) > 0)
		cout << '1' << endl;
	else
		cout << '0' << endl;
	if ((n & (1 << 7)) > 0)
		cout << '1' << endl;
	else
		cout << '0' << endl;

	long inv = (n ^ (1 << 1)) ^ (1 << 15);
	cout << inv << endl;

    return 0;
}
