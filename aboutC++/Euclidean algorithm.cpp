//////////////////////////////////////
//   Euclidean algorithm
//
//其原理基于两个整数的最大公约数等于其中较小的数和两数的相除余数的最大公约数。
//////////////////////////////////////
#include<stdio.h>  
int main()  
{  
    int x, y, z, m, n;  
    printf("请输入两个数：");  
    scanf_s("%d%d", &x, &y);  
    m = x, n = y;  
    while (y != 0)  
    {  
        z = x%y;  
        x = y;  
        y = z;  
    }  
    printf("最大公约数是: %d\n", x);  
    printf("最小公倍数是: %d\n", m*n / x);  
    system("pause");  
    return 0;  
} 

//假设两数为 x，y。

//先令 z = x % y ;

//之后 y 赋给 x 即令  x = y ;

//再将 z 赋给 y 即令  y = z；

//辗转相减，其终止条件为：y 等于0时。 
//
//