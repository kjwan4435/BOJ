#include <iostream>
#include <string>
using namespace std;
#include <queue>

queue<char> answer;

class Stack{
private:
    const unsigned short stack_size;
    int* arr;
    int arr_size;
    int max;

public:
    Stack(int num): arr_size(0), stack_size(num+1), max(0) {arr = new int[stack_size];}
    void push(int n){
        arr_size += 1;
        if (stack_size == arr_size) cout << "PUSH: STACK IS FULL" << endl;
        else {
            arr[arr_size-1] = n;
            answer.push('+');
        }
        if (max<n) max=n;
    }
    void pop(){
        if (arr_size == 0) cout << "POP: STACK IS EMPTY" << endl;
        else {
            arr_size-=1;
            answer.push('-');
        }
    }
    int top() {
        if (arr_size == 0) return 0;
        else return arr[arr_size-1];
    }
    void size() {cout << arr_size << endl;}
    void empty() {
        if (arr_size == 0) cout << 1 << endl;
        else cout << 0 << endl;
    }
    int GetMax() {return max;}
    ~Stack() {delete []arr;}
};

int main(){
    int num;
    cin >> num;
    Stack stack(num);
    int input[num];
    for (int i=0; i<num; i++){
        cin >> input[i];
    }

    for (int i=0; i<num; i++){
        int top = stack.top();
        int max = stack.GetMax(); // 여태껏 스택에 들어온 값 중에 최댓값.
        if (top>input[i]){
            cout << "NO";
            return 0;
        }
        if (top == input[i]) stack.pop();
        else if (max < input[i]){
            for (int j=0; j<input[i]-max; j++) stack.push(max+j+1);
            stack.pop();
        }
    }

    while(!answer.empty()){
        cout<<answer.front()<<"\n";
        answer.pop();
    }
    return 0;
}
