#include<stdio.h>
int main()
{
    int n,m,i,j,k,s=0,max=0;
    scanf("%d%d%d",&k,&n,&m);
    int a[n],b[m];
    for(i=0;i<n;i++)
    scanf("%d",&a[i]);
    for(j=0;j<m;j++)
    scanf("%d",&b[j]);
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            if(a[i]+b[j]>max && a[i]+b[j]<=k)
            max=a[i]+b[j];
            else if(a[i]+b[j]>k)
            {
                s++;
            }
            
        }
    }
    if(s==n*m)
    printf("-1");
    else
    printf("%d",max);
}
