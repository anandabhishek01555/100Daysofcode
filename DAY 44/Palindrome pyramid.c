/* C program for Palindrome pyramid pattern printing using numbers */
#include<stdio.h>
#include<stdlib.h>
int main()
{
int i,j,k,l,n;
scanf("%d",&n);
for(i = 1; i <= n; i++)
{
for(j = 1; j <= i; j++)
{
printf("%d ",j);
}
for(l = i-1; l >= 1; l--)
{
printf("%d ",l);
}
printf("\n");
}
return 0;
}





