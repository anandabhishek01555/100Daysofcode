#include<iostream>
using namespace std;
int main()
{
    int t,n,i,j;
    cin>>t;
    while(t>0)
    {
        int x=1;
        cin>>n;
        for(i=0;i<n;i++)
        {
            x=1;
            for(j=0;j<=i;j++)
            {
                cout<<x<<" ";
                x++;
            }
            cout<<"\n";
        }
        t-=1;
    }
}





