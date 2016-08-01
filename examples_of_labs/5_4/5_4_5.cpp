// The sample solution of the task B 5.4(5)
//
//  Вычислить корень уравнения f(x) = 0 на отрезке [a; b] с точностью E =10–6,
//  используя  заданный метод (М = 1 – метод половинного деления, М = 2 – метод касательных, М = 3 – метод хорд)   для заданных функций.
//  Вычисление корня уравнения оформить в виде функции с функциональным параметром, параметры a, b, E, s – в виде  аргументов по умолчанию.
//  Результат представить в виде таблицы (s – значение параметра, х – вычисленный корень уравнения,
//   f(x) – значение функции в найденной точке х, k_iter – количество итераций цикла для получения корня с заданной точностью):
//  а) f(x) = (x-1)^2 - 5 ;(2*(x - 1))	a = -3; b = 0;
//  б) f(x) = x^2 - sin(5x^s);(2*x - cos(5x^s)*5s*x^(s-1)) 	a = 0,5; b = 0,8;	s[0,7; 1,6],  delta s = 0,3; M=2.
//  x(n+1) = x(n) - f(x(n)) / f'(x(n))

#include <cmath>
#include <iostream>
#include <iomanip>

using namespace std;

typedef double (*FunDoub)(double);
typedef double (*FunDoubDoub)(double, double);

double functionA(double x)
{
	return ((x - 1) * (x - 1) - 5);
}

double functionB(double x, double s)
{
	return (x * x - sin(5 * pow(x, s)));
}

double functDeriv(FunDoub funct, double x)
{
	return ((funct(x + 1e-6) - funct(x)) / 1e-6);
}

double functDeriv(FunDoubDoub funct, double x, double s)
{
	return ((funct(x + 1e-6, s) - funct(x, s)) / 1e-6);
}

double func(int a, int b, double E, int &iter, FunDoub funct)//!!
{
	double xn, xnn = (a + b) / 2;
	do
	{
		iter++;
		xn = xnn;
		xnn = xn - funct(xn) / functDeriv(funct, xn);
	}
	while(abs(xnn - xn) > E);
	return xnn;
}

double func(double a, double b, double E, int &iter,FunDoubDoub funct, double s)//!!
{
	double xn, xnn = (a + b) / 2;
	do
	{
		iter++;
		xn = xnn;
		xnn = xn - funct(xn, s) / functDeriv(funct, xn, s);
	}
	while(abs(xnn - xn) > E);
	return xnn;
}

/*int main()
{
	cout << "\n a or b? ";
	char decision;
	cin >> decision;
	if (decision == 'a')
	{
		cout << "x	fx		k_iter" << endl;
		double E = 1e-6;
		int k_iter = 0, a = -3, b = 0;
		double x = func(a, b, E, k_iter, functionA);
		double fx = functionA(x);
		if (fx < 1e-15)
				fx = 0;
		cout << setprecision(2) << x << "	" << fx << "		" << k_iter << endl;
	}
	else if (decision == 'b')
	{
		cout << "s	x	fx	k_iter" << endl;
		double E = 1e-6, a = 0.5, b = 0.8;
		int k_iter = 0;
		for (double s = 0.7; s <= 1.6; s += 0.3)
		{
			double x = func(a, b, E, k_iter, functionB, s);
			double fx = functionB(x, s);
			if (fx < 1e-15)
				fx = 0;
			cout.width(2);
			cout << setprecision(2) << s << "	" << x << "	" << fx << "	" << k_iter << endl;
		}
	}
	return 0;
}*/
