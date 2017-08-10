// PairsofParentheses.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

void printPar(int left, int right, string & str)
{
	if (left < 0 || left > right)
		return;
	if (left == 0 && right == 0)
	{
		cout << str << endl;
	}
	else
	{
		if (left > 0)
		{
			str.append("(");
			printPar(left - 1, right, str);
			str.pop_back();
		}
		if (left < right)
		{
			str.append(")");
			printPar(left, right - 1, str);
			str.pop_back();
		}
	}

}

int _tmain(int argc, _TCHAR* argv[])
{
	int count;
	cin >> count;
	string str;
	printPar(count, count, str);

	return 0;
}

