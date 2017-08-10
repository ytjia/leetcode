// ConvertBinarySearchTree.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

struct BinaryTreeNode
{
	int m_nValue;
	BinaryTreeNode * m_pLeft;
	BinaryTreeNode * m_pRight;
};

void ConvertNode(BinaryTreeNode * pNode, BinaryTreeNode ** pLastNodeInList)
{
	if (pNode == NULL)
		return;

	BinaryTreeNode * pCurrent = pNode;
	if (pCurrent->m_pLeft != NULL)
		ConvertNode(pCurrent->m_pLeft, pLastNodeInList);
	pCurrent->m_pLeft = *pLastNodeInList;
	if (*pLastNodeInList != NULL)
		(*pLastNodeInList)->m_pRight = pCurrent;
	*pLastNodeInList = pCurrent;
	if (pCurrent->m_pRight != NULL)
		ConvertNode(pCurrent->m_pRight, pLastNodeInList);
}

BinaryTreeNode * Convert(BinaryTreeNode * pRoot)
{
	BinaryTreeNode * pLastNodeInList = NULL;
	BinaryTreeNode * pHeadNodeInList = NULL;

	ConvertNode(pRoot, &pLastNodeInList);
	pHeadNodeInList = pLastNodeInList;
	while (pHeadNodeInList != NULL && pHeadNodeInList->m_pLeft != NULL)
	{
		pHeadNodeInList = pHeadNodeInList->m_pLeft;
	}

	return pHeadNodeInList;
}

int _tmain(int argc, _TCHAR* argv[])
{
	return 0;
}

