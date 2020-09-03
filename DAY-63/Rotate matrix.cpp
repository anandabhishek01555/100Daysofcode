#include<iostream>
using namespace std;
int main()
{
    int i,j,n;
    cin>>n;
    int a[n][n];
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            cin>>a[i][j];
        }
    }
    for(i=n-1;i>=0;i--)
    {
        for(j=0;j<n;j++)
        {
            cout<<a[j][i]<<" ";
        }
        cout<<"\n";
    }
}
