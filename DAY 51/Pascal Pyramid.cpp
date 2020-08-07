#include<iostream>
using namespace std;
long factorial(int n);
int main()
{
    int n,i,j,k,x=1;
    cin>>n;
    for(i=0;i<n;i++)
    {
        for(j=0;j<n-i-1;j++)
        {
            cout<<" ";
        }
        for(k=0;k<=i;k++)
        {
            cout<<factorial(i)/(factorial(k)*factorial(i-k))<<" ";
        }
        cout<<"\n";
    }
}
long factorial(int n)
{
          int c;
          long int result = 1;
          for (c = 1; c <= n; c++)
                   result = result*c;
          return result;
}
