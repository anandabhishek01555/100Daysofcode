#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int a,b;
    cin>>a>>b;
	int M=1000000007;
	int x=(a%M+b%M)%M;
	cout<<x;
}
