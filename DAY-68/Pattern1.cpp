//1
//3*2
//4*5*6
//10*9*8*7
//11*12*13*14*15

#include<iostream>
using namespace std;
int main()
{
    int n,i,j,x=0,y=0;
    cin>>n;
    for(i=1;i<=n;i++)
    {
        x=y;
        for(j=1;j<=i;j++)
        {
            if (i%2==0)
            {
                cout<<x+i;
                x-=1;
                if(j!=i)
                cout<<"*";
                y++;
            }
            else
            {
                x=x+1;
                cout<<x;
                if(j!=i)
                {
                    cout<<"*";
                }
                y++;
            }
        }
        cout<<"\n";
    }
}
