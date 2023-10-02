#include "lists.h"

/**
 *check_cycle - a C function that checks if a singly linked list has a cycle
 *@list: pointer to the linked list head node
 *Return: 0 if there is no cycle, 1 if there is a cycle
 *Description: allowed functions write, printf, putchar, puts, malloc, free
 */
int check_cycle(listint_t *list)
{
	listint_t *start = list;
	listint_t *stop = list;

	if (!list)
		return (0);

	while (start && stop && stop->next)
	{
		start = start->next;
		stop = stop->next->next;
		if (start == stop)
			return (1);
	}

	return (0);
}
