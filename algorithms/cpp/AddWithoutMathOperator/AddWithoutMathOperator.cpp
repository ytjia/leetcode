// AddWithoutMathOperator.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
using namespace std;

int add(int a, int b);
int _tmain(int argc, _TCHAR* argv[])
{
	int a, b;
	cin >> a >> b;

	int c = add(a, b);
	cout << c;

	return 0;
}

int add(int a, int b)
{
	char * c;
	c = (char *) a;
	int res = (int)&c[b];
	return res;
}

