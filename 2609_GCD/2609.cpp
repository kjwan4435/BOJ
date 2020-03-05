#include <iostream>
using namespace std;

int GCD(int x, int y){
    if (x%y==0) return y;
    else return GCD(y, x%y);
}

int main(void){
    int x,y;
    cin >>x>>y;
    cout << GCD(x,y) << '\n' << x*y/GCD(x,y);
    return 0;
}