#include <iostream>
using namespace std;

int main()
{
    int n1,n2,n3;
    cin >> n1 >> n2 >> n3;
    if((n1>=n2 && n2>=n3) || (n3>=n2 && n2>=n1)){cout<<n2;}
    else if((n1>=n3 && n3>=n2) || (n2>=n3 && n3>=n1)){cout<<n3;}
    else {cout<<n1;}
    return 0;
}