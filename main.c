#include<stdio.h>

int global_1;
int global_2;

int main()
{
	foo();
	printf("%x %x\n", global_1, global_2);
	return 0;
}
