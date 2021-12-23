#include "lists.h"

/**
 * insert_node - inserts a new node at a given position.
 * @head: head of a list.
 * @number: index of the list where the new node is added.
 *
 * Return: the address of the new node, or NULL if it
 * failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp;
	listint_t *new_node;
	listint_t *prv_node;

	tmp = *head;
	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	while (tmp != NULL)
	{
		if (tmp->n > number)
			break;
		prv_node = tmp;
		tmp = tmp->next;
	}
	new_node->n = number;

	if (*head == NULL)
	{
		new_node->next = NULL;
		*head = new_node;
	}
	else
	{
		new_node->next = tmp;
		if (tmp == *head)
			*head = new_node;
		else
			prv_node->next = new_node;
	}

	return (new_node);
}
