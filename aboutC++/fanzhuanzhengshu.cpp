#include <iostream>
using namespace std;
 
class Integer{
private:
    int _num;
//getLength()函数获取_num长度
    int getLength(){
    }
public:
//Integer类构造函数
    Integer(int num){
    }
//反转_num
    int inversed(){
    }
};
 
int main() {
    int n;
    cin >> n;
    Integer integer(n);
    cout << integer.inversed() << endl;
    return 0;
}