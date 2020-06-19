#include <stdio.h>
int main()
{
    int n,i,c=0,flag=0,odd=0;
    scanf("%d",&n);
    int a[n];
    for(i=0;i<n;i++)
    scanf("%d",&a[i]);
    for(i=0;i<n;i++)
    {
        if(a[i]%2!=0)
        odd+=1;
    }
    if(odd%2!=0)
    printf("NO");
    else{
    for(i=0;i<n;i++)
    {
        if(a[i]%2!=0)
        {
            a[i]+=1;
            a[i+1]+=1;
            c+=2;
        }
        else
        continue;
    }
    printf("%d",c);
}
}

