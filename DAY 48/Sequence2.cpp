#include<iostream>
using namespace std;
int main()
{
    int n,i,j;
    cin>>n;
    int x=n+1;
    int k=x;
    for(i=0;i<n;i++)
    {
        for(j=0;j<n-i;j++)
        {
        	
        	cout<<x;
        	x++;
		}
		x-=1;
        cout<<"\n";
    }
}

