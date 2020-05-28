
#include <stdio.h>
int lcm(int *a, int n);
int gcd(int *b, int m);
int main()
{
  int result, size,m,n,result1,j,i;
  scanf("%d%d",&n,&m);
  int a[n],b[m];
  for(i=0;i<n;i++)
  scanf("%d",&a[i]);
  for(i=0;i<m;i++)
  scanf("%d",&b[i]);
  result = lcm(a, n);
  result1 = gcd(b, m);
        int count = 0;
        for(i = result;i<=result1; i+=result)
        {
            if(result1%i==0){ count++;}
        }
        printf("%d ",count);
}
int lcm(int *a, int n)
{
    int i =0;
    int m = a[0];
    while (1) {
    for (i = 0; i < n; i++) {
        if(m % a[i]) break;
      }
      if( i == n) break;
      m++;
    }
 return m;
}
int gcd(int *b, int m)
{ 
    int gcd,i;
    gcd=b[0];
    int j=1;
    while(j<m)
    {
       if(b[j]%gcd==0)
       {
           j++;
       }
       else
       {
           gcd=b[j]%gcd;
           i++;
       }
    }
return gcd;
}

