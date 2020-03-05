#include <iostream>
using namespace std;

class Clock
{
private:
    int time;
    int hour;
    int min;
public:
    Clock(int h, int m)
    {
        time = 60*h + m;
        hour = h;
        min = m;
    }
    void set_clock();
    void show();
};

int main(){
    int x,y;
    cin >> x >> y;
    Clock sangeun(x,y);
    sangeun.set_clock();
    sangeun.show();
    return 0;
}

void Clock::set_clock(){
    time = time - 45;
    if(time > 60*24)
    {
        time = time - 60*24;
    }
    else if(time < 0)
    {
        time = time + 60*24;
    }
    hour = time / 60;
    min = time % 60;
}

void Clock::show(){cout << hour << " " << min << endl;}