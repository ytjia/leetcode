// Skip_List.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#define MAX_LEVEL 10

typedef struct nodeStructure
{
	int key;
	int value;
	nodeStructure * forward[1];
}nodeStructure;

typedef struct skipList
{
	int level;
	nodeStructure * header;
}skipList;

nodeStructure * creatNode(int level, int key, int value)
{
	nodeStructure * ns = (nodeStructure *)malloc(sizeof(nodeStructure) + level * sizeof(nodeStructure *));
	ns->key = key;
	ns->value = value;
	return ns;
}

skipList * creatSkipList()
{
	skipList * sL = (skipList *)malloc(sizeof(skipList));
	sL->level = 0;
	sL->header = creatNode(MAX_LEVEL, 0, 0);
	for (int i = 0; i < MAX_LEVEL; ++i)
	{
		sL->header->forward[i] = NULL;
	}
	return sL;
}

int randomLevel()
{
	int k = 1;
	while (rand() % 2)
	{
		++k;
	}
	k = (k < MAX_LEVEL) ? k : MAX_LEVEL;
	return k;
}

// insert a node
bool insert(skipList * sL, int key, int value)
{
	nodeStructure * update[MAX_LEVEL];
	nodeStructure * p, * q = NULL;
	p = sL->header;
	int k = sL->level;

	for (int i = k - 1; i >= 0; --i)	
	{
		while ((q = p->forward[i]) && q->key < key)
		{
			p = q;
		}
		update[i] = p;
	}

	if (q && q->key == key)
	{
		return false;
	}

	k = randomLevel();
	if (k > sL->level)
	{
		for (int i = sL->level; i < k; ++i)
		{
			update[i] = sL->header;
		}
		sL->level = k;
	}

	q = creatNode(k, key, value);
	for (int i = 0; i < k; ++i)
	{
		q->forward[i] = update[i]->forward[i];
		update[i]->forward[i] = q;
	}
	return true;
}

// delete a node
bool deleteSL(skipList * sL, int key)
{
	nodeStructure * update[MAX_LEVEL];
	nodeStructure * p, * q = NULL;
	p = sL->header;
	int k = sL->level;

	for (int i = k - 1; i >= 0; --i)
	{
		while ((q = p->forward[i]) && (q->key < key))
		{
			p = q;
		}
		update[i] = p;
	}

	if (q && q->key == key)
	{
		for (int i = 0; i < k; ++i)
		{
			if (update[i]->forward[i] == q)
			{
				update[i]->forward[i] = q->forward[i];
			}
		}
		free(q);

		for (int i = k - 1; i >= 0; --i)
		{
			if (sL->header->forward[i] == NULL)
				sL->level--;
		}
		return true;
	}
	else
	{
		return false;
	}
}

// search the value of specified key
int search(skipList * sL, int key)
{
	nodeStructure * p, * q = NULL;
	p = sL->header;
	int k = sL->level;

	for (int i = k - 1; i >= 0; --i)
	{
		while ((q = p->forward[i]) && q->key <= key)
		{
			if (q->key == key)
				return q->value;
			p = q;
		}
	}
	return NULL;
}

// print off the skipList
void printSL(skipList * sL)
{
	nodeStructure * p , * q = NULL;
	p = sL->header;
	int k = sL->level;
	
	for (int i = k - 1; i >= 0; --i)
	{
		q = p->forward[i];
		while (q)
		{
			printf("%d -> ", q->value);
			q = q->forward[i];
		}
		printf("\n");
	}
	printf("\n");
}

int _tmain(int argc, _TCHAR* argv[])
{
	skipList * sL = creatSkipList();
	for (int i = 1; i < 19; ++i)
		insert(sL, i, i * 2);
	printSL(sL);

	int search4 = search(sL, 4);
	printf("search4 = %d\n", search4);

	bool status = deleteSL(sL, 4);
	if (status)
		printf("Delete successfully!\n");

	printSL(sL);
	
	return 0;
}

