#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - insert a node
 * @number: the number
 * @head: the list
 * Return: the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *aux = *head;
	listint_t *node = malloc(sizeof(listint_t));

	if (!node)
		return (NULL);
	node->n = number;
	node->next = NULL;
	if (*head)
	{
		if ((*head)->n > number)
		{
			node->next = (*head);
			*head = node;
				return (node);
		}

		while ((*head)->next && (*head)->next->n < number)
		{
			*head = (*head)->next;
		}
		node->next = (*head)->next;
		(*head)->next = node;
		*head = aux;
		return (node);
	}
		*head = node;
		return (node);
}
