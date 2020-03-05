#include <iostream>
using namespace std;

int main(){
    string str;
    int counter = 0;
    while (true){ //while(cin>>str)
        cin>>str;
        if(cin.eof() == true) {break;}
        counter +=1;
    }
    cout<<counter;
    return 0;
}