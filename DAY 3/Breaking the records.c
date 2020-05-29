#include<stdio.h>
int main()
{
    int max,min,i,n,cm=0,cn=0;
    scanf("%d",&n);
    int a[n];
    for(i=0;i<n;i++)
    scanf("%d",&a[i]);
    max=a[0];
    min=a[0];
    for(i=0;i<n;i++)
    {
        if(a[i]>max)
        {
            cm++;
            max=a[i];
        }
        if(a[i]<min)
        {
            cn++;
            min=a[i];
        }
    }
    printf("%d",cm);
    printf(" %d",cn);
}

