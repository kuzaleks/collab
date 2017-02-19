#include <iostream>

using namespace std;

int main()
{
	double R, x, y;
	cin >> R >> x >> y;
	if(x*x+y*y > R*R) cout << "No" << endl;
	else{
		if(x >= 0 && y >= 0 && x*x+y*y <= R*R) cout << "Yes" << endl;
		else if (x <= 0 && y <= 0 && x+y >= -1*R) cout << "Yes" << endl;
		else cout << "No" << endl;
	}

}