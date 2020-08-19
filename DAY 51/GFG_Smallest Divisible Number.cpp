#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,n;
    cin>>t;
    while(t>0)
    {
        cin>>n;
        int i,ans=1;
        for(i=1;i<=n;i++)
            ans=(ans*i)/(__gcd(ans, i)); 
        cout<<ans<<endl;
        t--;
    }
}
