#include <iostream>

using namespace std;

int main()
{
	double R, x, y;
	cin >> R >> x >> y;
	if(((x >= 0 && y >= 0) || (x>= 0 && y <= 0)) && x*x+y*y<=R*R)
		cout << "Yes" << endl;
	else if(x <= 0 && y >= 0 && y + x >= 0)
		cout << "Yes" << endl;
	else if(x <= 0 && y <= 0 && y <= x)
		cout << "Yes" << endl;
	else 
		cout << "No" << endl;
}