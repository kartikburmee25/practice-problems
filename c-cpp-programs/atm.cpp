#include<iostream>
#include<iomanip>
#include<sstream>

using namespace std;

int main()
{
int x; float y;
cin>>x>>y;
float balance;
cout.setf(ios::fixed);
if(x%5==0)
{
if((x+0.50)<=y)
	{ balance=y-x-0.50;
	  cout<<setprecision(2)<<balance;
	}
else
	{ cout<<setprecision(2)<<y; }
}
else
	{
	  cout<<setprecision(2)<<y;
	}
return 0;
}
