#include<iostream>
#include<algorithm>
#include<stdio.h>
using namespace std;
int main()
{
	int n,i;
	cin>>n;
	int a[n];
	for(i=0;i<n;i++)
	cin>>a[i];
	sort(a,a+n);
	cout<<n<<endl;
	for(i=0;i<n-1;i++){
	if(a[i]!=a[i+1])
	cout<<n-(i+1)<<endl;
}
}
