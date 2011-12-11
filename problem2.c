#include<stdio.h>

int main()
{
	int a = 1;
	int b = 2;
	int c = a+b;
	int sum = 2;
	while(c<4000000)
	{
		if((c%2)==0)
			sum+=c;
		a=b;
		b=c;
		c=a+b;
	}
	
	printf("Sum of even fibonacci terms less than 4 million : %d\n", sum);
	return 0;
}

