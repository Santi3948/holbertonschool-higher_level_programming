#include "lists.h"
int check_cycle(listint_t *list)
{
	listint_t *aux = list;

	while(aux->next)
	{
		if(aux->next != list)
			aux = aux->next;
		else
			return(1);
	}
	return (0);
}
