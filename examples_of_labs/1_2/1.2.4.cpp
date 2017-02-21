#include <iostream>

using namespace std;

int main()
{
	double R1, R2, x, y;
	cin >> R1 >> R2 >> x >> y;

	if(((x >= 0 && y >= 0) || (x <= 0 && y <= 0)) && 
		(x*x + y*y >= R2 * R2 && x*x + y*y <= R1*R1))
		cout << "Yes" << endl;
	else 
		cout << "No" << endl;
}