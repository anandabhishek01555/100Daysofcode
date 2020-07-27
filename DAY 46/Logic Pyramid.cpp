#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
    int n,i,j,k,t;
    cin>>t;
    while(t>0)
    {
    int t1=6,t2=22;
    cin>>n;
    cout.fill('0');
    for(i=1;i<=n;i++)
    {
        for(k=0;k<n-i;k++)
        cout<<"   ";
        for(j=1;j<=i;j++)
        {cout<<setw(5)<<t1<<" ";
        t1=t1+t2;
        t2=t2+16;}
        cout<<"\n";
    }
    t-=1;
    }
}
