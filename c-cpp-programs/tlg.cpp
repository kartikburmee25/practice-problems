#include<iostream>
using namespace std;

int main()
{
int nr;
cin>>nr;
int p1[nr];
int p2[nr];
int d;
int max1=0,max2=0;

for(int i=0;i<nr;i++)
{

cin>>p1[i]>>p2[i];
d=p1[i]-p2[i];
if(d>=0)
{if(d>max1)max1=d;}
else
{if(d<max2)max2=d;}

}

if(max1>((-1)*max2))
{cout<<1<<" "<<max1;}
else
{cout<<2<<" "<<((-1)*max2);}

return 0;

}



