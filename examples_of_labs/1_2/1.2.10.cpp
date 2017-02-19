#include <iostream>

using namespace std;

int main()
{
	double x, y;
	cin >> x >> y;
	if(x >= 0 && y >= 0 && y <= x && 
		y >= (x-2)*(x-2) - 3)
		cout << "Yes" << endl;
	else if(x >= 0 && y <= 0 && x + y <= 0 && 
		y >= (x-2)*(x-2) - 3)
		cout << "Yes" << endl;
	else cout << "No" << endl;
}