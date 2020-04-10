#include <iostream>
using namespace std;

int main(){
    int num;
    cin>>num;
    int sum = 0;
    int max = 0;
    int grade[num];
    for (int i=0;i<num;i++){
        scanf("%d", &grade[i]);
        if (grade[i]>max){max = grade[i];}
        sum += grade[i];
    }
    cout << 100*(double)sum/(max*num);
    return 0;
}