#include <iostream>

using namespace std;

int main()
{
	double R, x, y;
	cin >> R >> x >> y;
	if(x >= 0 && y >= 0 && x*x+y*y >= R*R && x <= 2*R && y <= 2*R) 
		cout << "Yes" << endl;
	else if (x <= 0 && y <= 0 && x+y >= -2*R) cout << "Yes" << endl;
	else cout << "No" << endl;

}