#include <iostream>
#include<fstream>
using namespace std;

inline int sum(int x, int y) {return x + y;}
inline int dis(int x, int y) {return x - y;}
inline int mul(int x, int y) {return x * y;}
inline int mod(int x, int y) {return x / y;}
inline int rem(int x, int y) {return x % y;}

int main(void){
    int x, y;
    cin >> x >> y;
    cout << sum(x,y) << '\n' << dis(x,y) << '\n' << mul(x,y) << '\n' << mod(x,y) << '\n' << rem(x,y) << endl;
    return 0;
}