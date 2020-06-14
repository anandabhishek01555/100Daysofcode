#include<stdio.h>
int main()
{
    long long int t;
    scanf("%lldd",&t);
    while(t--)
    {
    long long int n,i,j,sum=0,flag=0;
    scanf("%lld",&n);
    long long int a[n][n],b[n];
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            scanf("%lld",&a[i][j]);
        }
    }
        for (i = 0; i < n; ++i) 
        {
            for (j = 0; j < n; ++j) 
            {
                sum = sum + a[i][j] ;
            }
            b[i]=sum;
            // printf("Sum of the %ld row is = %ld\n", i, sum);
            sum = 0;
            // printf("%d ",b[i]);
 
        }
        for (j = 0; j < n; ++j) 
        {
            for (i = 0; i < n; ++i) 
            {
                sum = sum + a[i][j] ;
            }
            
            if(sum==b[j])
            flag+=1;
            // printf("Sum of the %ld row is = %ld\n", j, sum);
            sum = 0;
 
        }
        if(flag==n)
        printf("Possible\n");
        else
        printf("Impossible\n");
    }

}
