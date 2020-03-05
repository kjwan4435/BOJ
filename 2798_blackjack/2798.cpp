#include <iostream>
#include <cmath>
using namespace std;


int main(){
    int num, M;
    cin>>num>>M;
    int card[num];
    for (int i=0; i<num; i++)
    {
        cin>>card[i];
    }
    int answer = card[0] + card[1] + card[2];

    for (int i=0; i<num; i++)
    {
        for (int j=i+1; j<num; j++)
        {
            for (int k=j+1; k<num; k++)
            {
                if (abs(card[i]+card[j]+card[k]-M) < abs(answer-M) && card[i]+card[j]+card[k] <= M)
                {
                    answer = card[i]+card[j]+card[k];
                }
            }
        }
    }
    cout<<answer;
    return 0;
}