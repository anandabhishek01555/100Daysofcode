#include<stdio.h>
int main()
{
    int n,k,i,j,s,c=0;
    scanf("%d%d",&n,&k);
    int a[n];
    for(i=0;i<n;i++)
    scanf("%d",&a[i]);
    for(i=0;i<n;i++)
    {

        for(j=i+1;j<n;j++)
        {   
            s=0;
            s+=a[i]+a[j];
            if(s%k==0)
            c++;
        }
    }
    printf("%d",c);
}
