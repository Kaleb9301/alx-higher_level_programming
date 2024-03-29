#include "lists.h"

/**
 * check_cycle - a function that checks a linked list for a cycle
 * @list: poninter to head of list
 *
 * Return: 0 if there is no cycle
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
