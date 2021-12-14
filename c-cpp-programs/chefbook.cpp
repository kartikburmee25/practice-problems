#include<iostream>
#include<string>
#include<algorithm>

using namespace std;

struct post
{ 
string f;
int p;
string s;
};

bool sorter(const post &lhs, const post &rhs)
{ return lhs.p<rhs.p; }

bool sorter2(const post &lhs, const post &rhs)
{ return lhs.p<rhs.p; }


int csp=0;

int main()
{
int n,m,i,j;
cin>>n>>m;
int tmp;
int arrr[100001] = {0};
    
    for( i=1; i <= n; i++)
    {
        cin >> tmp;
        arrr[tmp] = 1;
    }


post arr_post[1001];
post arr_spost[1001];

for(i=0;i<m;i++)
{
	  int k;
	  cin>>k;
	  int flag=0;
	  
	 if(arrr[k]==1)

			{
			 
			 arr_spost[csp].f=k;
			 cin>>arr_spost[csp].p;
			 cin>>arr_spost[csp].s;
			 csp++;
			}
	else
	{
	  
	  arr_post[i-csp].f=k;
	  cin>>arr_post[i-csp].p;
	  cin>>arr_post[i-csp].s;
	}
}

sort(arr_spost,arr_spost+n,sorter);

sort(arr_post,arr_spost+(m-n),sorter2);

for( i=n-1;i<=0;i--)
{cout<<arr_spost[i].s<<endl;}

for( i=m-n-1;i<=0;i--)
{cout<<arr_post[i].s<<endl;}
	
	


return 0;

}





			
		 
	  
	


