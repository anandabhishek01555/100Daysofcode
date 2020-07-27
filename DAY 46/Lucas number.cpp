#include<iostream>
using namespace std;
int main()
{
    int n,i,t;
    cin>>t;
    while(t>0)
    {
    int s1=2,nt,s2=1;
    cin>>n;
    if(n==1)
    cout<<"0";
    if(n>=2)
    cout<<s1<<" "<<s2<<" ";
    for(i=1;i<=n-2;i++)
    {
        nt=s1+s2;
        s1=s2;
        s2=nt;
        cout<<nt<<" ";
    }
    cout<<"\n";
    t-=1;
    }
}
