#include<iostream>
using namespace std;
int bsearch(int a[],int l,int h,int k);
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
int bsearch(int a[],int l,int r,int k)
{	
    if (r >= l) { 
        int mid = l + (r - l) / 2; 
        if (a[mid] == k) 
            return mid; 
        if (a[mid] > k) 
            return bsearch(a, l, mid - 1, k); 
        return bsearch(a, mid + 1, r, k); 
    } 
	return -1;
}
