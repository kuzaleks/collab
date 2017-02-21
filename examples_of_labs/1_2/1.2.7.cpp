#include <iostream>

using namespace std;

int main()
{
	//TODO: проверить
	double R, x, y;
	cin >> R >> x >> y;
	if(x <= 0 && y >= 0 && (x+R)*(x+R) + y*y <= R*R) cout << "Yes" << endl;
	else if(x >= 0 && y <= 0 && (x-R)*(x-R) + y*y <= R*R) cout << "Yes" << endl;
	else cout << "No" << endl;
}