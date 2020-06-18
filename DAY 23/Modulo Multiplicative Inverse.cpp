#include <stdio.h>
int main()
{
    int a,m,t,i,x,flag=0;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&a,&m);
    for(i=1;i<m;i++)
    {
        x=i*a;
        if(x%m==1)
        {
            printf("%d\n",i);
            flag+=1;
            break;
        }
        
    }
    if(flag==0)
    printf("-1");
    }
}

