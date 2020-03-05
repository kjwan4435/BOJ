#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void Print(vector<int> &v)
{
    int size = v.size();
    for(int i=0; i<size; i++){cout<<v[i]<<'\n';}
}

int main(void){
    int num, input;
    cin>>num;
    vector<int> v;
    v.reserve(num);
    for (int i=0; i<num; i++){
        cin>>input;
        v.push_back(input);
    }
    sort(v.begin(), v.end());
    Print(v);
    v.clear();
    vector<int>().swap(v);
    return 0;
}