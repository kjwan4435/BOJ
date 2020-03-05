#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int N_card;
vector<int> card;
queue<int> answer;

int GCD(int x, int y){
    if (x%y==0) return y;
    else return GCD(y, x%y);
}

int main(){
    cin >> N_card;
    card.resize(N_card);
    for (int i=0; i<N_card; i++) cin>>card[i];
    sort(card.begin(), card.end());

    int gcd = card[1] - card[0];
    for (int i=2; i<N_card; i++) gcd = GCD(gcd, card[i]-card[i-1]);

    vector<int> gcd_vector; //두번째 수와 첫번째 수의 차이
    for (int i=1; i<=gcd; i++){ 
        if (gcd%i==0){
            if (i>gcd/i) break;
            gcd_vector.push_back(i);
            if (i==gcd/i) break;
            gcd_vector.push_back(gcd/i);
        }
    }

    sort(gcd_vector.begin(), gcd_vector.end(), greater<int>());

    while(!gcd_vector.empty()){
        if(gcd_vector.back()!=1) cout << gcd_vector.back() << " ";
        gcd_vector.pop_back();
    }

    return 0;
}