#include <iostream>
#include <string>
using namespace std;

class Queue{
private:
    const int Q_size;
    int* arr;
    int start;
    int arr_size;
public:
    Queue(): arr_size(0), Q_size(2000001), start(0) {arr = new int[Q_size];}
    void push(int n){
        arr_size += 1;
        arr[(start + arr_size-1)] = n;
    }
    void pop(){
        if (arr_size == 0) cout << -1 << "\n";
        else {
            cout << arr[start] << "\n";
            start += 1;
            arr_size -= 1;
        }
    }
    void front() {
        if (arr_size == 0) cout << -1 << "\n";
        else cout << arr[start] << "\n";
    }
    void back() {
        if (arr_size == 0) cout << -1 << "\n";
        else cout << arr[(start + arr_size-1)] << "\n";
    }
    void size() {cout << arr_size << "\n";}
    void empty() {
        if (arr_size == 0) cout << 1 << "\n";
        else cout << 0 << "\n";
    }
    ~Queue() {delete []arr;}
};

int main(){
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    Queue Q;
    int num;
    cin >> num;
    string str;

    for (int i=0; i<num; i++){
        cin >> str;
        if (str == "push") {
            int input;
            cin >> input;
            Q.push(input);
        }
        else if (str == "pop") Q.pop();
        else if (str == "front") Q.front();
        else if (str == "back") Q.back();
        else if (str == "empty") Q.empty();
        else Q.size();
    }
    return 0;
}