#include<stdio.h>
int main()
{
    int n,i,j,visited=-1,c;
    scanf("%d",&n);
    int a[n],b[n];
    for(i=0;i<n;i++)
    {   
        scanf("%d",&a[i]);
        b[i]=0;
    }
    for(i=0;i<n;i++)
    {
        c=1;
        for(j=i+1;j<n;j++)
        {
            if(a[i]==a[j])
            {
                c+=1;
                b[j]=visited;
            }
        }
        
        if(b[i]!=visited)
        b[i]=c;
    }
    
    for(i=0;i<n;i++)
    {
        if(b[i]!=visited)
        printf("%d ",b[i]);
    }
}
