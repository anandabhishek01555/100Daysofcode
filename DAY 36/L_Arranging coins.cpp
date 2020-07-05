#include<iostream>
using namespace std;
int main()
{
	int n,i=1,c=0;
	cin>>n;
	while(n>=0)
	{
		n=n-i;
		
		c++;
		i++;
	}
	cout<<c-1;
}
