#include <iostream>
using namespace std;

class One{
private:
    const int x;
public:
    One(int a): x(a) {}
    int Onehandler();
    int numOne();
};

int main(){
    int a;
    cin>>a;
    One Q1(a);
    cout<<Q1.numOne();
    return 0;
}

int One::Onehandler(){
    int counter=0;
    for(int i=100; i<=x; i++){
        int _00 = i/100;
        int _0 = (i-(_00*100))/10;
        int _ = i-((_00*100)+(_0*10));
        if((_00-_0)==_0-_){
            counter+=1;
        }
    }
    return counter;
}

int One::numOne(){
    if(x<100){return x;}
    else{return 99+Onehandler();}
}