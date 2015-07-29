// ReverseWordsInSentence.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

void Reverse(char * pBegin, char * pEnd)
{
	if (pBegin == NULL || pEnd == NULL)
		return;

	char tmp;
	while (pBegin < pEnd)
	{
		tmp = *pBegin;
		*pBegin = *pEnd;
		*pEnd = tmp;
		pBegin++;
		pEnd--;
	}
}

void ReverseSentence(char * pData)
{
	if (pData == NULL)
		return;

	char * pBegin = pData;
	char * pEnd = pData;
	
	while (*pEnd != '\0')
		pEnd++;
	pEnd--;

	Reverse(pBegin, pEnd);

	pBegin = pEnd = pData;
	while (*pBegin != '\0')
	{
		if (*pBegin == ' ')
		{
			pBegin++;
			pEnd++;
		}
		else if (*pEnd == ' ' || *pEnd == '\0')
		{
			Reverse(pBegin, pEnd - 1);
			pBegin = pEnd;
		}
		else
		{
			pEnd++;
		}
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	char pData[] = "I am a student.";
	ReverseSentence(pData);
	printf_s("%s\n", pData);
	return 0;
}

