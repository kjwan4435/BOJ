#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string str; // RDD 문자
int arr_size; // 배열 사이즈
string str_arr; // 배열 문자로 읽기

int* StoiArr(string str){
    int* arr = new int[arr_size]; // 배열 사이즈 기준으로 배열 동적할당
    int str_len = str.length(); 
    string temp_str = "";
    int count = 0;
    for (int i=1; i<str_len; i++){
        if (str_arr[i] == ']') {
            if (temp_str != "") arr[count] = stoi(temp_str);
            break;
        }
        else if (str_arr[i] == ','){
            arr[count] = stoi(temp_str);
            count+=1;
            temp_str="";
        }
        else temp_str += str_arr[i];
    }
    return arr;
}

int main(void){
    int n;
    cin>>n;
    for (int z=0; z<n; z++){
        cin>>str; 
        int len = str.length(); // 문자길이
        cin >> arr_size;
        cin >> str_arr;

        // 배열 숫자 배열로 리턴하자!
        int* arr = StoiArr(str_arr);

        int R_count = 0;
        int start_D = 0;
        int end_D =0;
        bool error = 0;
        for (int i=0; i<len; i++){
            if (str[i] == 'R') R_count +=1;
            else if (str[i] == 'D') {
                if (arr_size-(start_D+end_D) == 0){
                    cout << "error" << '\n';
                    error = 1;
                    break;
                }
                if (R_count%2==0) start_D+=1;
                else end_D+=1;
            }
        }
        if (!error){
            if (arr_size-(start_D+end_D) == 0){
                cout << "[]" << '\n';
            }
            else if (R_count%2==0){
                cout << "[";
                for (int i=start_D; i<(arr_size-end_D-1); i++){
                    cout << arr[i] << ",";
                }
                cout << arr[arr_size-end_D-1] << "]" <<"\n";
            }
            else{
                cout << "[";
                for (int i=(arr_size-end_D-1); i>=start_D+1; i--){
                    cout << arr[i] << ",";
                }
                cout << arr[start_D] << "]" <<"\n";
            }
        }
        delete []arr;
    }
    return 0;
}