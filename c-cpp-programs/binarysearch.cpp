#include<iostream>
using namespace std;

int b_search(int *arr,int size,int x)
{
int start=0,end=size-1,mid;
while(start<=end)
{
mid=(start+end)/2;
if(arr[mid]==x) return mid;
else if(x<arr[mid]) end=mid-1;
else start=mid+1;

}
return -1;
}

int main()
{int index;
int arr[]={1,6,3,22,7,99,26,16,90};
int size=sizeof(arr)/sizeof(int);
index=b_search(arr,size,90);
cout<<index<<endl;

return 0;

}

