#include<stdio.h>
#include"giants.h"

int main()
{
	giant x = newgiant(600851475143), y = newgiant(600851475143), z = newgiant(2), a = newgiant(INFINITY);
	
	for(; gcompg(x,z)>0 ; iaddg(1,z))
	{
		gtog(x, a);
		modg(z, a);
		if(gcompg(a,0)==0)
		{
			gtog(z,y);
			divg(z,x);
			iaddg(-1,z);
		}
		
	}
	gout(z);
	return 0;
}
		
