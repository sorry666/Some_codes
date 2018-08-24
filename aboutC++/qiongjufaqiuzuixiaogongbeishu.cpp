/////////////////////////////
//穷举法求最大公约数，最小公倍数
//
//
////////////////////////////
#include<stdio.h>  
int main()  
{  
    int x, y, i, m, n;  
    printf("请输入两个数：");  
    scanf_s("%d%d", &x, &y);  
    m = x, n = y;  
    for (i = 1; i <= x; i++)  
    {  
        if (x%i == 0 && y%i == 0)  
    }  
    for (i = x; i > 0; i--)  
    {  
        if (x%i == 0 && y%i == 0)  
    }  
    printf("最大公约数是: %d\n", i);  
    printf("最小公倍数是: %d\n", m*n / i);  
    system("pause");  
    return 0;  
}  


