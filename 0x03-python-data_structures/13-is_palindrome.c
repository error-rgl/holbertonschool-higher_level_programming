#include "lists.h"

/**
 * compare - compares each int of the list
 *
 * @h1: head of the first half
 * @h2: head of the second half
 * Return: 1 if are equals, 0 if not
 */
int compare(listint_t **h1, listint_t *h2)
{
	if (h2 == NULL)
		return (1);
	if (compare(h1, h2->next) && (*h1)->n == h2->n)
	{
		*h1 = (*h1)->next;
		return (1);
	}
	return (0);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 *
 * @h1: pointer to head of list.
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palindrome
 */
int is_palindrome(listint_t **h1)
{
	if (!h1 || !(*h1))
		return (1);
	return (compare(h1, *h1));
}
