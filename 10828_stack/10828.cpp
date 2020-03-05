#include <iostream>
#include <string>
using namespace std;

class Stack{
private:
    const unsigned short stack_size;
    int* arr;
    int arr_size;
public:
    Stack(): arr_size(0), stack_size(10001) {arr = new int[stack_size];}
    void push(int n){
        arr_size += 1;
        if (stack_size == arr_size){
            cout << "STACK IS FULL" << endl;
        }
        else {
            arr[arr_size-1] = n;
        }
    }
    void pop(){
        if (arr_size == 0) cout << -1 << endl;
        else {
            cout << arr[arr_size-1] << endl;
            arr_size-=1;
        }
    }
    void top() {
        if (arr_size == 0) cout << -1 << endl;
        else cout << arr[arr_size-1] << endl;
    }
    void size() {cout << arr_size << endl;}
    void empty() {
        if (arr_size == 0) cout << 1 << endl;
        else cout << 0 << endl;
    }
    ~Stack() {delete []arr;}
};
int main(){
    Stack stack;
    int num;
    cin >> num;
    string str;

    for (int i=0; i<num; i++){
        cin >> str;
        if (str == "push") {
            int input;
            cin >> input;
            stack.push(input);
        }
        else if (str == "pop") stack.pop();
        else if (str == "top") stack.top();
        else if (str == "empty") stack.empty();
        else if (str == "size") stack.size();
        else cout << "WRONG INPUT" << endl;
    }
    return 0;
}