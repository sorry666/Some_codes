#include<stdio.h>  
#include<iostream>
int main(void)  
{  
   using namespace std;
   
    int x, y, temp,num;
    int r;  
    cout<<"��������������"<<endl;  
    cin>>x>>y;  
    //m = x, n = y; 
    if (x>y )
	{
       num=x;
	   x=y;
	   y=num;
	}
    r=x%y;
    temp=y; 
    while (r != 0)  
    {  
        x = y;  
        y = r;
        r=x%y;  
    }  
    cout<<"���Լ����: "<<y<<endl;  
    cout<<"��С��������: "<<(x*temp/y)<<endl;  
    //system("pause");  
    return 0;  
} 
