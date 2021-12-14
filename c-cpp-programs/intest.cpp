#include<iostream>
using namespace std;

int main()
{
int count;
int n,k;
int x;
cin>>n>>k;
while(n--)
	{ 
	  cin>>x;
	  if(x%k==0)count++;
	}
cout<<count;
return 0;
}

