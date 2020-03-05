#include <iostream>
#include <array>
using namespace std;

void Print(array<int, 10001> &arr)
{
    for (int i=0; i<10001; i++) 
    {
        if (arr[i] != 0)
        {
            for (int j=0; j<arr[i]; j++) {cout << i <<'\n';}
        }
    }
}

int main(){
    std::ios_base::sync_with_stdio(false);
    int num, input;
    array<int, 10001> NUM;
    NUM.fill(0);
    cin>>num;
    for (int i=0; i<num; i++)
    {
        cin>>input;
        NUM[input]++;
    }
    Print(NUM);
}