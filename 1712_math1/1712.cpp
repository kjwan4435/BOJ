#include <iostream>
using namespace std;

class Notebook{
private:
    const int fixed;
    const int make;
    const int price;
public:
    Notebook(int a, int b, int c): fixed(a), make(b), price(c) {}
    int BreakPoint();
};

int main(){
    int f, m, p;
    cin>>f>>m>>p;
    Notebook world(f,m,p);
    cout << world.BreakPoint();
    return 0;
}

int Notebook::BreakPoint()
{
    if (price<=make){return -1;}
    else{
        return (fixed/(price-make))+1;
    }
}