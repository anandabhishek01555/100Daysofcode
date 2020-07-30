#include<iostream>
using namespace std;
int main()
{
    int t,n,i,j,c;
    cin>>t;
    while(t>0)
    {
        char x='A';
        cin>>n;
        for(i=0;i<n;i++)
        {
        	x='A';
            for(j=0;j<=i;j++)
            {
                cout<<x<<" ";
                x=int(x);
                x++;
            }
            cout<<"\n";
        }
        t-=1;
    }
}





