#include "lists.h"
int check_cycle(listint_t *list)
{
	listint_t *aux2 = list;
	listint_t *aux1 = list;

	while (list)
	{
		if (aux1->next)
			aux1 = aux1->next;
		if (aux2->next)
		{
			aux2 = aux2->next;
			if (aux2->next)
				aux2 = aux2->next;
			else
				return (0);
		}
		else
			return(0);
		if (aux1 == aux2)
			return (1);
	}	
	return (0);
}
