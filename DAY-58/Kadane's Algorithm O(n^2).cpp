#include<iostream>
using namespace std;
int main()
{
    int n=5,i,j,s=0,temp,l;
    int a[n]={1,2,3,-2,5};
    l=a[0];
    for(i=0;i<n;i++)
    {
        for(j=i;j<n;j++)
        {
            temp=s;
            s+=a[j];
            if(s>l)
            l=s;
        }
        s=0;
    }
cout<<l;
    
}
