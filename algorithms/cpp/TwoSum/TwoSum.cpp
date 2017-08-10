// TwoSum.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

// Solution for a sorted vector.
//class Solution {
//public:
//    vector<int> twoSum(vector<int> &numbers, int target) {
//        // Start typing your C/C++ solution below
//        // DO NOT write int main() function
//
//		vector<int> result;
//		vector<int>::iterator iter1 = numbers.begin(), iter2 = numbers.end() - 1;
//		while (iter1 < iter2)
//		{
//			if (*iter1 + *iter2 == target)
//			{
//				result.push_back(iter1 - numbers.begin() + 1);
//				result.push_back(iter2 - numbers.begin() + 1);
//				return result;
//			}
//			else if (*iter1 + *iter2 < target)
//			{
//				iter1++;
//			}
//			else
//			{
//				iter2--;
//			}
//		}
//		return result;
//    }
//};

class Solution {
public:
    vector<int> twoSum(vector<int> &numbers, int target) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function

		vector<int> result;
		vector<int>::iterator iter = numbers.begin();
		map<int, int> mapnum;
		for (; iter < numbers.end(); ++iter)
		{
			if (mapnum[target - *iter])
			{
				result.push_back(mapnum[target - *iter]);
				result.push_back(iter - numbers.begin() + 1);
				return result;
			}
			else
			{
				mapnum[*iter] = iter - numbers.begin() + 1;
			}
		}
		return result;
    }
};

int _tmain(int argc, _TCHAR* argv[])
{
	vector<int> numbers;
	for (int i = 0; i < 20; i += 2)
	{
		numbers.push_back(i);
	}
	int target = 14;
	Solution s;
	vector<int> result = s.twoSum(numbers, target);

	return 0;
}

