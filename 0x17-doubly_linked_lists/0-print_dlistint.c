#include "lists.h"

/**
 * print_dlistint - prints all the elements of a
 * dlistint_t list
 *
 * @j: head of the list
 * Return: the number of nodes
 */
size_t print_dlistint(const dlistint_t *j)
{
	int count;

	count = 0;

	if (j == NULL)
		return (count);

	while (j->prev != NULL)
		j = j->prev;

	while (j != NULL)
	{
		printf("%d\n", j->n);
		count++;
		j = j->next;
	}

	return (count);
}
