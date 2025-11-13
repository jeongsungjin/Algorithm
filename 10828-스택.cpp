#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
    int n;
    cin >> n;
    cin.ignore();
    stack<int> st;

    for(int i = 0; i < n; i++) {
        string cm;
        getline(cin, cm);

        if(cm.substr(0, 4) == "push") {
            int x = stoi(cm.substr(5));
            st.push(x);
        }
        else if(cm == "pop") {
            if(!st.empty()){
                cout << st.top() << endl;
                st.pop();
            }   
            else {
                cout << -1 << endl;
            }
        }
        else if(cm == "size") {
            cout << st.size() << endl;
        }
        else if(cm == "empty") {
            cout << (st.empty() ? 1 : 0) << endl;
        }
        else if(cm == "top") {
            if(!st.empty()) {
                cout << st.top() << endl;
            }
            else {
                cout << -1 << endl;
            }
        }
    }
    return 0;
}