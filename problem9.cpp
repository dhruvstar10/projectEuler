#include<iostream>

using namespace std;

int main()
{
	long a = 1;
	for(;a<500;a++)
		if(((500000-(1000*a))%(1000-a))==0)
			cout<<a<<endl;
			
	return 0;
}
