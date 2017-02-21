#include <iostream>

using namespace std;

int main()
{
	double R, x, y;
	cin >> R >> x >> y;
	if(x*x + y*y > R*R) cout << "No" << endl;
	else{
		if(x <= 0 && y <= 0) 
			cout << "Yes" << endl; 
		else if(x >= 0 && y >= 0 && y >= (x-1)*(x-1))
			cout << "Yes" << endl;
		else cout << "No" << endl;
	}
}