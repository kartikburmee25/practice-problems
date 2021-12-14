#include<iostream>
using namespace std;

int main()
{
int n,q;
cin>>n>>q;
int t;
int arr[n];

for(int i=0;i<n;i++)
{cin>>arr[i];}
int min=arr[0],max=0;

for(int i=0;i<n;i++)
{ if(arr[i]>max)max=arr[i];
if(arr[i]<min)min=arr[i];
}

while(q--)
{ 
cin>>t;
if(t>max || t<min) cout<<"No"<<endl;
else cout<<"Yes"<<endl;
}

return 0;

}

