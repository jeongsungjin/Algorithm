#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int dp[n];

    dp[1] = 1;
    dp[2] = 2;

    for(int i = 3; i <= n; i++) {
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007;
    }
    cout << dp[n];
}
//파이썬으로 푸니까 런타임에러가 뜨네 ㅋㅋ