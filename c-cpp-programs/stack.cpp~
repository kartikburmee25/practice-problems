#include<stdio.h>
#include<iostream>

using namespace std;

int top=0;

int stack_empty(int x[])
{ if (x[0]==false)
	{return true;}
  else
	{return false;}
}


void push (int x[],int e)
{ top=top+1;
  x[top]=e;
}	

int pop(int x[])
{ if (stack_empty(x)==true)
	cout<<"error";
else
	{top=top-1;
	 return x[top+1];
	}
}

int main()
{ int a=10;
int b=20;
int s[10];
int k;

push(s,a);
push(s,b);
push(s,a);

k=pop(s);

cout<< k;

return 0;

}
