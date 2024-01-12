#include "lists.h"

/**
 * dlistint_len - returns the number of elements in
 * a double linked list
 *
 * @j: head of the list
 * Return: the number of nodes
 */
size_t dlistint_len(const dlistint_t *j)
{
	int count;

	count = 0;

	if (j == NULL)
		return (count);

	while (j->prev != NULL)
		j = j->prev;

	while (j != NULL)
	{
		count++;
		j = j->next;
	}

	return (count);
}