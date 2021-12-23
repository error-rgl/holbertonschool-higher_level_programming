#include "lists.h"

/**
 * check_cycle - checks if a singly linked
 * list has a cycle in it.
 * @list: pointer to the list
 * Return: 0 if there is no cycle,
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *rabit = list;
	listint_t *turtle = list;

	if (!list)
		return (0);

	while (turtle && rabit && rabit->next)
	{
		turtle = turtle->next;
		rabit = rabit->next->next;

		if (turtle == rabit)
			return (1);
	}
	return (0);
}
