#include<iostream>
#include<stdio.h>


using namespace std;

class queue
{int rear,front;
int queue1[5];

	public:
queue()
{rear=-1;
front=-1;
}

void enq( int x)
{ if (rear>4)
	{rear=front=-1;
	 cout<<"error\n"<<"overflow";
	return;}	

rear+=1;
queue1[rear]=x;
  
cout<<"enqueued "<<x;
}	

void deq()
{ cout<<"dequeued"<<queue1[++front];}

void display()
{for (int i=front+1 ;i<=rear; i++)
	{cout<<queue1[i]<<"\n";}
}
};

int main()
{ int choice;
  queue q1;
	while(1)

	{cout<<"\n 1.insert 2.delete 3.display 4.exit \n"<<"enter choice \n";
	cin>>choice;
	switch(choice)
	
	{ case(1):
		cout<<"enter element\n";
		cin>>choice;
		q1.enq(choice);
		break;
	case(2):
		q1.deq();
		break;
	case(3):
		q1.display();
		break;
	case(4):
		break;
	}
	}
return (0);
	}
 			
