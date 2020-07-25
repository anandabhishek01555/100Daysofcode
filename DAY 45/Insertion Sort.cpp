#include<iostream>
using namespace std;
int main()
{
	int n,i,j,k;
	cin>>n;
	int a[n];
	for(i=0;i<n;i++)
	cin>>a[i];
	for(i=1;i<n;i++)
	{
	    k=a[i];
		j=i-1;
		while(j>=0 && a[j]>k)
		{
			a[j+1]=a[j];
			j=j-1;
		}
		a[j+1]=k;
	}
	for(i=0;i<n;i++)
	cout<<a[i]<<" ";
}
