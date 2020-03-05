#include <iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int num;
    cin>>num;
    for (int i=0; i<num; i++) {
        int x,y;
        cin >> x>>y;
        cout << x+y << '\n';
    }
    return 0;
}