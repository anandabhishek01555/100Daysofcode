#include <stdio.h>
int main()
{
int m, n, i, gcd,x=1;
scanf("%d%d", &m, &n);
for(i=1; i <=m && i <= n; ++i)
{
// Checks if i is factor of both integers
if(m%i==0 && n%i==0)
gcd = i;
}
printf( "%d", gcd);
printf("\n");
x=m*n;
printf("%d",x/gcd);

return 0;
}
