#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - insetrs a number into a
 * sorted singly linked list
 *
 * @head: pointer to structure
 * @number: integer
 * Return: structure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *s = malloc(sizeof(listint_t));
	listint_t *h = malloc(sizeof(listint_t));
	listint_t *e = malloc(sizeof(listint_t));

	s = *head;
	if (s->n >= number)
		return (*head);
	while (s != NULL)
	{
		h = s;
		s = s->next;
		if (s->n >= number)
			break;
	}
	e->n = number;
	h->next = e;
	e->next = s;
	return (*head);
}

