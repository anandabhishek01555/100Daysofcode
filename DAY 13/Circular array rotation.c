#include<stdio.h>
int main()
{
    int n,k,i,last,m,q;
    scanf("%d%d%d",&n,&k,&q);
    int a[n],b[q];
    for(i=0;i<n;i++)
    scanf("%d",&a[i]);
    while(k--)
    {
    last=a[n-1];
    for(i=n-1;i>0;i--)
    {
        a[i]=a[i-1];
        
    }
    a[0]=last;
    }
    for(m=0;m<q;m++)
    scanf("%d",&b[m]);
    for(m=0;m<q;m++)
    printf("%d\n",a[b[m]]);
}

