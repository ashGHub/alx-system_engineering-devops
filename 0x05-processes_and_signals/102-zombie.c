#include "unistd.h"
#include "stdio.h"

/**
 * infinite_while - loops infinitly
 * Return: always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - start 5 zombie process
 * Return: always 0
 */
int main(void)
{
	int i;
	pid_t pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid != 0)
		{
			printf("Zombie process created, PID: %i\n", (int)pid);
			infinite_while();
		}
	}
	return (0);
}
