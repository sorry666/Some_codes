# include <stdio.h>  
  
int  main(void)  
{  
    int x, y,temp,num1,num2;  
    int r;   
    printf("请输入两个正整数：\n");  
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
    printf("它们的最大公约数为：%d\n", num2);  
    printf("它们的最小公倍数为：%d\n", num1*temp/num2);  
      
    return 0;  
}  
