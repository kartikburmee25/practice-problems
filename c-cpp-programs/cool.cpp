#include<iostream>

using namespace std;

int main()
{
int arr[] = {453,23,12,567,5632,23,100,5};

int min = 0;
for (int i=0; i<sizeof(arr)/sizeof(int); i++)
{
	if(arr[i]<arr[min])
		{
		min=i;
		}
}
cout<< arr[min] <<endl;

return 0;

}

