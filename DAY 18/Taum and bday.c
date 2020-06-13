#include<stdio.h>
int main()
{
    int t;
    scanf("%d",&t);
    while(t--)
    {
    long int b,w,bc,wc,z,total;
    scanf("%ld%ld%ld%ld%ld",&b,&w,&bc,&wc,&z);
    if(bc>wc+z && bc>wc)
    {
        total = wc*w + b*(wc+z);
    }
    else if(wc>bc+z && wc>bc)
    {
        total = w*(bc+z) + b*bc;
    }
    else
    {
        total=w*wc + b* bc;
    }
    printf("%ld\n",total);
    }
}

