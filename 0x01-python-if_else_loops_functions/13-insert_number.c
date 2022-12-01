#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node -  inserts a number into a sorted singly linked list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	while (current->next != NULL)
	{
		if (new->n < current->next->n && new->n > current->n)
		{
			new->next = current->next;
			current->next = new;
		}
		current = current->next;
	}

	return (new);
}
