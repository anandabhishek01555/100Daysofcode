#include<iostream>
using namespace std;
int main()
{
    int n,i,j,k;
    cin>>n;
    int x=10;
    for(i=0;i<n;i++)
    {
        for(k=0;k<i;k++)
        {
            cout<<"  ";
        }
        for(j=0;j<n-i;j++)
        {
        	cout<<x;
        	x+=10;
		}
        cout<<"\n";
    }

}

