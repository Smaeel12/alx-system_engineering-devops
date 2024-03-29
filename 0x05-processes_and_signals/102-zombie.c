#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>


/**
 * infinite_while - infinite while
 *
 * Return: 0 always.
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
 * main - entry point
 *
 * Return: 0 always.
 */
int main(void)
{
	int i;
	pid_t pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid > 0)
			printf("Zombie process created, PID: %i\n", pid);
		else
			return (0);
	}
	infinite_while();
	return (0);
}
