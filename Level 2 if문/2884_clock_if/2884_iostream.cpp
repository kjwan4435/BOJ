#include <iostream>
using namespace std;

class Clock
{
private:
    int hour;
    int min;
public:
    void set_clock(int m=45);
    friend ostream& operator<<(ostream&, const Clock&);
    friend istream& operator>>(istream&, Clock& clk);
};

int main(){
    Clock sangeun;
    cin>>sangeun;
    sangeun.set_clock(45);
    cout << sangeun;
    return 0;
}

void Clock::set_clock(int m){
    min -= m;
    if(hour*60+min > 60*24) {hour = hour - 24;}
    else if(hour*60+min < 0) {hour = hour + 24;}
    hour = (hour*60+min) / 60;
    min = (hour*60+min) % 60;
}

ostream& operator<<(ostream& os, const Clock& clk)
{
    os<<clk.hour<<" "<<clk.min<<endl;
    return os;
}

istream& operator>>(istream& is, Clock& clk)
{
    is>>clk.hour>>clk.min;
    return is;
}