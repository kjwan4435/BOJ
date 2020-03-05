#include <iostream>
using namespace std;

int n;

void func(int num, int &count){
    count +=1;
    int x,y;
    x = num/10;
    y = num%10;
    if (y*10+((x+y)%10) == n){
        cout << count;
        exit(0);
    }
    func(y*10+((x+y)%10), count);
}

int main(void){
    cin >> n;
    int count = 0;
    func(n, count);
    return 0;
}