#include<iostream>
using namespace std;
int main()
{
	int a;
	cin>>a;
	for(int i=0;i<(2*a-1);i++)
	{
		for(int j=0;j<(2*a-1);j++)
		{ 
		if(i==0 || i==(2*a-2))
		{
			
			if(j<=a-2)
			{
				cout<<" ";
			}
			else
			{
				cout<<"*";
			}
		}
		else
		{
			 if(i<=a-1)
			 {  
			    if(j==a-i-1){
			    	cout<<"*";
				}
				else if(j<a-i-1)
				{
					cout<<" ";
				}
				else{
					cout<<"~";
				}
			 	
			 }
			 else
			 {
			 	 if(j==i-a+1)
			 	 {
			 	 	cout<<"*";
				  }
				  else if(j<=i-a)
				  {
				  	cout<<" ";
				  }
			 		else{
					 cout<<"~";
					 }
			 
			 }
		}
		}
		cout<<"\n";
	}
}
