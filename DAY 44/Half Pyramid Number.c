#include<stdio.h>
int main()
{
    int n,i,j,x=1;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        for(j=0;j<=i;j++)
        {
            printf("%d ",x);
            x+=1;
        }
        x=1;
        printf("\n");
    }
}
