#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int k,l,m,n;
	cin >> k >> l >> m >> n;

	if(k > 8 || l > 8 || m > 8 || n > 8){
		cout << "No" << endl;
		return 0;
		//cout << "No" < <endl;
	}
	//k, l - ладья(прямо) 
	//m, n - слон(диагональ)

	//		  ладья                             слон
	if((k == m || l == n) || ((k + l) == (m + n) || (m - k) == (n - l))) 
		cout << "Yes" << endl;
	else{ 
		cout << "No" << endl;
		//if((abs(k - m) < 8 || abs(l - n) < 8) || )
	}

	return 0;
}