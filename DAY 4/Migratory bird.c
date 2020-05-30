#include<stdio.h>
int main()
{
    int n,i,c=1,j,temp=1,x;
    scanf("%d",&n);
    int a[n];
    for(i=0;i<n;i++)
    scanf("%d",&a[i]);
    for(i=0;i<n;i++)
    {   
        if(c>temp)
        {
            temp=c;
            x=a[i-1];
        }
        for(j=i+1;j<n;j++)
        {
            if(a[i]==a[j])
            {
                c+=1;
            }
        }
    }
    printf("%d",x);
}
