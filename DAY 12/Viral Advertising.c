#include<stdio.h>
int main()
{
    int n,i,x,s=0;
    scanf("%d",&n);
    int a[20002],b[20002];
    a[0]=5;
    for(i=0;i<n;i++)
    {
        x=a[i]/2;
        s+=x;
        a[i+1]=x*3;
    }
    printf("%d",s);
}


