#include <iostream>

using namespace std;


int sum(int a, int b)
{
	cout<<a+b<<" ";
	return 0;
}

int main()
{
	 cout<<"hello, world!"<<"\n";
	 int arr[]={10,222,3};
	 for (int i=0;i<2;i++)
	 {
             sum(arr[i],arr[i+1]);
	 }
	 return 0;
}
