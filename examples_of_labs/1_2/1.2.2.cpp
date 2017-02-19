#include <iostream>

using namespace std;

int main()
{
	double R, x, y;
	cin >> R >> x >> y;

	if(x >= 0 && y <= 0 && 
		((x-R)*(x-R) + (y + R)*(y + R) >= R*R) && 
		(x <= R) && (y >= -1*R))
		cout << "Yes" << endl;
	else if(x <= 0 && y >= 0 && 
		((x + R)*(x + R) + (y - R)*(y - R) >= R*R) && 
		(x >= -1*R) && (y <= R))
		cout << "Yes" << endl;
	else 
		cout << "No" << endl;

}