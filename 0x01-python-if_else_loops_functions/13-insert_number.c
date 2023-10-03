#include "lists.h"
/**
 *insert_node - function in C that inserts a number into a
 *sorted singly linked list.
 *@head: double pointer to head of likrd lists
 *@number: integer
 *Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *add;

	add = malloc(sizeof(listint_t));
	if (add)
		return (NULL);
	add->n = number;
	if (node == NULL || node->n >= number)
	{
		add->next = node;
		*head = add;
		return (add);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;
	add->next = node->next;
	node->next = add;

	return (add);
}
