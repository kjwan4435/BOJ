#include <iostream>
using namespace std;

int main(){
    std::ios_base::sync_with_stdio(false);
    int x;
    cin >> x;
    for(int i=1; i<=x; i++){cout<<i<<'\n';}
    return 0;
}