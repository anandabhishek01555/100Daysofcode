#include<iostream>
using namespace std;
int bsearch(int arr[],int l,int h,int k);
int main()
{
	int n,k,i,l=0,h,r;
	cin>>n;
	int a[n];
	for(i=0;i<n;i++)
	cin>>a[i];
	cin>>k;
	h=n-1;
	r=bsearch(a,l,h,k);
	cout<<r;
}
int bsearch(int arr[],int l,int r,int x)
{	
    while (l <= r) { 
        int m = l + (r - l) / 2; 
        if (arr[m] == x) 
            return m; 
        if (arr[m] < x) 
            l = m + 1; 
        else
            r = m - 1; 
    } 

    return -1; 

}
