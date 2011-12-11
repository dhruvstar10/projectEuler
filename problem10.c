#include<stdio.h>
#include<math.h>



int main()
{
	int sum = 2;
	int num = 3;
	
	for(;num<2000000;num+=2)
	{
		if(Prime(num))
			sum+=num;
	}

	printf("Sum of Primes below 2000000 is : %d", sum);
	return 0;
}
 
bool Prime(int x)
{
	float sq = sqrt(x);
	int sqr = (int) sq;
	int i;
	for(i=2 ; i<=sqr; i++)
	{
		if((x%i)==0)
			return false;
	}

	return true;
}
