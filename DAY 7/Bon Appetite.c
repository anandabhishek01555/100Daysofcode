#include<stdio.h>
int main()
{
    int n,k,i,b,s=0,m,x;
    scanf("%d%d",&n,&k);
    int bill[n];
    for(i=0;i<n;i++)
    scanf("%d",&bill[i]);
    scanf("%d",&b);
    for(i=0;i<n;i++)
    {
        s+=bill[i];
    }
    x=s-bill[k];
    m=x/2;
    if(b==m)
    printf("Bon Appetit");
    else
    printf("%d",b-m);
}

