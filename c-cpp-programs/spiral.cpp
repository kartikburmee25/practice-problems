#include<iostream>
using namespace std;

void spiral(int m,int n,int arr[][n])
{
int dir;
int t=0,b=m-1,l=0,r=n-1;
while(t<=b && l<=r)
	{
	if(dir==0)
		{for(int i=l;i<=r;i++)
			{ cout<<arr[t][i]<<" ";}
		t++;
		}
	else if(dir==1)
		{for(int i=t;i<=b;i++)
			{cout<<arr[i][r]<<" ";}
		r--;
		}
	else if(dir==2)
		{for(int i=r;i>=l;t--)
			{cout<<arr[b][i]<<" ";}
		b--;	
		}
	else if(dir==3)
		{for(int i=b;i>=t;i--)
			{cout<<arr[i][l]<<" ";}
		l++;
		}
	dir=(dir+1)%m;
	}
}

int main()
{
int mat[4][4]={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16};
spiral(4,4,mat);
return 0;
}

