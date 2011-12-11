#include<stdio.h>
int main(void)
{
	int sum = 0;
	int i;
	for(i=0; i<1000; i+=3)
		sum+=i;
	for(i=5 ; i<1000; i+=5)
		sum+=i;
	for(i=15 ; i<1000; i+=15)
		sum-=i;
	printf("Sum of all numbers less than 1000 that are divisible by 3 or 5 is : %d", sum);
	return 0;
} 
