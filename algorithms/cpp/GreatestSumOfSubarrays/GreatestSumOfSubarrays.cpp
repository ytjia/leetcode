// GreatestSumOfSubarrays.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

int a[100010];

struct MaxSum
{
	int maxSum;
	int beg;
	int end;
};

int _tmain(int argc, _TCHAR* argv[])
{
	struct MaxSum max;
	int n, sum, newbeg;
	while (scanf_s("%d", &n) && n != 0)
	{
		max.maxSum = -2000;
		max.beg = max.end = 0;
		sum = 0;
		newbeg = 0;
		for (int i = 0; i < n; ++i)
		{
			scanf_s("%d", &a[i]);
		}

		for (int i = 0; i < n; ++i)
		{
			sum += a[i];
			if (sum < 0)
			{
				if (sum > max.maxSum)
				{
					max.maxSum = sum;
					max.beg = max.end = i;
				}
				sum = 0;
				newbeg = i + 1;
			}
			else
			{
				if (sum > max.maxSum)
				{
					max.maxSum = sum;
					max.beg = newbeg; 
					max.end = i;
				}
			}
		}

		cout << max.maxSum << " " << max.beg << " " << max.end << endl;
	}
	return 0;
}

