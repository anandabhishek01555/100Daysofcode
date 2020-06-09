
#include<stdio.h>
int main()
{
    int t;
    scanf("%d",&t);
    while(t--)
    {
        int n,r,c=0,temp;
        scanf("%d",&n);
        temp=n;
        while(temp!=0)
        {
            r=temp%10;
            if(r!=0)
            {
            if(n%r==0)
            c+=1;
            }
            temp/=10;
            
        }
        printf("%d\n",c);
}
}
