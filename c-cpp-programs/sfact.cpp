#include<iostream>
using namespace std;

int factorial(int n)
{
  if(n==1||n==0)
	return 1;
  int x=n*factorial(n-1);
  return x;
}

int main()
{
int t,n;
cin>>t;
while(t--)
{
cin>>n;
cout<<factorial(n)<<endl;
}
return 0;
}
