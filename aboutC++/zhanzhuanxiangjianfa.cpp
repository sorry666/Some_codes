///////////////////////////////////////
//尼考曼彻斯法(辗转相减法)
//
///////////////////////////////////////////
#include<stdio.h>  
int main()  
{  
    int x, y, m, n;  
    printf("请输入两个数：");  
    scanf_s("%d%d", &x, &y);  
    m = x, n = y;  
    while (x!=y)  
    {  
        if (x>y)  
            x = x-y;  
        else  
            y = y-x;  
    }  
    printf("最大公约数是: %d\n", x);  
    printf("最小公倍数是: %d\n", m*n / x);  
    system("pause");  
    return 0;  
}  

//假设两数为 x, y。

//当 x > y 时，令 x = x - y;

//反之，则令 y = y - x;

//之后一直辗转相减，直至 x = y 时，终止。