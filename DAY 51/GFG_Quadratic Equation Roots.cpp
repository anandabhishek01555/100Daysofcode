#include<bits/stdc++.h> 
using namespace std; 
int main()
{
// Prints roots of quadratic equation ax*2 + bx + x 
  int a,b,c;
  cin>>a>>b>>c;
  int d  = b*b - 4*a*c; 
  double sqrt_val = sqrt(abs(d));   
  int x1=floor((double)(-b + sqrt_val)/(2*a));
  int x2=floor((double)(-b - sqrt_val)/(2*a));
   if((b*b)>=(4*a*c))
   {
        if(x1>x2)
        {
            cout<<x1<<" "<<x2;
        }
        else
        cout<<x2<<" "<<x1;
       
   }
   else
   cout<<"Imaginary";
}
