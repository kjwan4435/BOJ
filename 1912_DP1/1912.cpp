#include <iostream>
#include <list>
using namespace std;

int main(){
    int num, max;
    cin >> num;
    int array[num], dp[num];
    for (int i=0; i<num; i++) {cin>>array[i];}
    max = dp[0] = array[0];
    for (int i=1; i<num; i++)
    {
        if (dp[i-1]+array[i]>array[i]) dp[i]=dp[i-1]+array[i];
        else dp[i] = array[i];
        if (dp[i] > max) max = dp[i];
    }
    cout << max;
    return 0;
}