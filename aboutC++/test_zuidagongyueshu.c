# include <stdio.h>  
  
int  main(void)  
{  
    int x, y,temp,num1,num2;  
    int r;   
    printf("������������������\n");  
    scanf("%d %d", &num1, &num2); 
	if (num1>num2 )
	{
       x=num1;
	   num1=num2;
	   num2=x;
	}

    r = num1 % num2;  
    temp = num2;  
    while(r!=0)  
    {  
        num1 = num2;  
        num2 = r;  
        r = num1 % num2;  
    }  
    printf("���ǵ����Լ��Ϊ��%d\n", num2);  
    printf("���ǵ���С������Ϊ��%d\n", num1*temp/num2);  
      
    return 0;  
}  
