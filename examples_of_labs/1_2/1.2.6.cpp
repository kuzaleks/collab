#include <iostream>

using namespace std;

int main()
{
	double x, y;
	cin >> x >> y;
	if(x >= 0 && y >= 0 && y <= x && 
	   y <= -x*x + 2 && x*x <= 2 - y) cout << "Yes" << endl;
	else if(x <= 0 && y <= 0 && y >= x && 
	   y <= -x*x + 2 && x*x <= 2 - y) cout << "Yes" << endl;
	else cout << "No" << endl;
}