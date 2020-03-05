#include <iostream>
#include <queue>
#include <vector>
#define MAX 1000
using namespace std;

int N_build, N_rule;
vector<int> Time_build;
vector<int> Start_build;
vector<int> Dest_build;
vector<int> indeg;
vector<int> timecount;
int win;

void input();

int main(){
    std::ios_base::sync_with_stdio(false);

    int N_test;
    cin>> N_test;
    for (int i=0; i<N_test; i++) {
        input();
        queue<int> Q; 
        for (int i=1; i<=N_build; i++){
            if (indeg[i]==0) Q.push(i);     // Q에 시작점을 다 집어넣음.
        }

        while(!Q.empty()){                  // Q가 빌 때 까지.
            int start = Q.front();          // Q의 제일 처음을 start로 저장.
            timecount[start] += Time_build[start];
            if (start == win) break;
            for (int i=0; i<N_rule; i++){   // start가 시작 빌딩에 있으면 매칭되는 목적 빌딩의 indegree를 1 차감.
                if (start == Start_build[i]){
                    indeg[Dest_build[i]]--;
                    if (timecount[Dest_build[i]] < timecount[start]){
                        timecount[Dest_build[i]] = timecount[start]; // 가장 시간이 오래걸린 애로 update.
                    }
                    if (indeg[Dest_build[i]] == 0) {
                        Q.push(Dest_build[i]); //indeg 0이면 Q에 추가.
                    }
                }
            }
            Q.pop();
        }
        cout << timecount[win] << "\n";
    }

    return 0;
}

void input(){
    Time_build.clear();
    Start_build.clear();
    Dest_build.clear();
    indeg.clear();
    timecount.clear();

    cin >> N_build >> N_rule;

    Time_build.resize(N_build+1);
    Start_build.resize(N_rule);
    Dest_build.resize(N_rule);
    indeg.resize(N_build+1);
    timecount.resize(N_build+1);

    for (int i=1; i<=N_build; i++) {cin>>Time_build[i];}
    for (int i=0; i<N_rule; i++) {
        cin>>Start_build[i]>>Dest_build[i];
        indeg[Dest_build[i]]++;
    }
    cin>>win;
}