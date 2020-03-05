#include <iostream>
using namespace std;

void hanoi(int num, int start, int etc, int end);
int counter(int num);

int main(){
    std::ios_base::sync_with_stdio(false);
    int num;
    cin >> num;
    cout << counter(num) << '\n';
    hanoi(num,1,2,3);
    return 0;
}

int counter(int num){
    int stacker = 1;
    for(int i=1;i<num;i++){stacker = 2*stacker+1;}
    return stacker;
}

void hanoi(int num, int start, int etc,int end){
    if (num==1)
    {
        cout<<start<<" "<<end<<"\n";
    }
    else
    {
        hanoi(num-1,start,end,etc);
        cout<<start<<" "<<end<<"\n";
        hanoi(num-1,etc,start,end);
    }
}