#include<iostream>
using namespace std;
int main()
{
	int n,i,j,mi,temp;
	cin>>n;
	int a[i];
	for(i=0;i<n;i++)
	cin>>a[i];
	for(i=0;i<n-1;i++)
	{
		mi=i;
		for(j=i+1;j<n;j++)
		{
			if(a[j]<a[mi])
			mi=j;			
		}
		temp=a[i];
		a[i]=a[mi];
		a[mi]=temp;
	}
	for(i=0;i<n;i++)
	{
		cout<<a[i]<<" ";
	}
}
