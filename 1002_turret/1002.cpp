#include <iostream>
#include <cmath>
using namespace std;

class Turret{
private:
    int x, y;
    int r;
public:
    Turret(int x, int y, int r): x(x), y(y), r(r) {}
    int getX() {return x;}
    int getY() {return y;}
    int getR() {return r;}
    int marine_detection(Turret others);
};

int main(){
    int num;
    cin >> num;
    for (int i=0; i<num; i++){
        int x,y,r,_x,_y,_r;
        cin >> x >> y >> r >> _x >> _y >> _r;
        Turret Jo(x,y,r); //조규현의 터렛 생성
        Turret Baek(_x,_y,_r); //백승환의 터렛 생성
        cout << Jo.marine_detection(Baek) << '\n'; //두 터렛의 교점 출력
    }
    return 0;
}

int Turret::marine_detection(Turret others){
    int _x = others.getX();
    int _y = others.getY();
    int _r = others.getR();
    double d = sqrt(pow(x-_x,2)+pow(y-_y,2)); //두 원점 사이를 계산, 이때 자료형이 double임을 조심하자.
    if (x==_x && y==_y){
        if(r==_r) {return -1;} // 두 원의 중심이 동일하고, 반지름이 같다면 류재명이 존재할 수 있는 좌표의 개수는 무한대
        else {return 0;}}
    else if ((r+_r)>d && abs(r-_r)<d){return 2;} //교점이 두 개인 경우
    else if ((r+_r)==d || abs(r-_r)==d){return 1;} //교점이 한 개인 경우
    else {return 0;}
}