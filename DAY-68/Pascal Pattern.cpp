#include <iostream>
using namespace std;
void printPascal(int n)
{
int x = n;
for (int line = 1; line <= n; line++)
{
for(int j = x; j > 0; j--)
cout << " ";
x--;
int C = 1;
for (int i = 1; i <= line; i++)
{
cout << C << " ";
C = C * (line - i) / i;
}
cout << endl;
}
}
int main()
{
int x;
//Input number of rows
cin >> x;
printPascal(x);
return 0;
}
