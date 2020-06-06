#include<stdio.h>
int main()
{
    int n,i,k,x;
    scanf("%d%d",&n,&k);
    int a[n];
    for(i=0;i<n;i++)
    scanf("%d",&a[i]);
    for(i=0;i<n;i++)
    {
        if(k<a[i])
        {x=a[i]-k;
        break;}
        else
        x=0;
        
    }
    printf("%d",x);
}
