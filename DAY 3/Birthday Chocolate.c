#include<stdio.h>
int main()
{
	int n,i,d,m,s,temp,c=0,j;
	scanf("%d",&n);
	int a[n];
	for(i=0;i<n;i++)
	scanf("%d",&a[i]);
	scanf("%d%d",&d,&m);
	
	for(i=0;i<n;i++)
	{
		s=0;
		temp=0;
		for(j=i;j<n;j++)
		{
			if(temp<m)
			{
				s+=a[j];
				temp++;
			}
		}
	if(s==d)
	c++;
	}
	printf("%d",c);
}
