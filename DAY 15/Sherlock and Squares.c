#include<math.h>
#include<stdio.h>
int main()
{
    int t,n,res;
    scanf("%d",&t);
    while(t--)
    {
        int n1,n2,x;
        scanf("%d%d",&n1,&n2);
        res = (int)sqrt(n2)-(int)sqrt(n1);
        if(n1 == (int)sqrt(n1)*(int)sqrt(n1))  
        ++res;  
        printf("%d\n",res);
        res=0;
    }
}
