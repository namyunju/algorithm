#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int tc=1; tc<=T; tc++) {
        int N, K;
        cin >> N >> K;
        vector<int> dp(K+1, 0);

        for (int i=0; i<N; i++) {
            int v, c;
            cin >> v >> c;

            for (int j=K; j>=v; j--) {
                dp[j] = max(dp[j], dp[j-v]+c);
            }
        }
        cout << "#" << tc << " " << dp[K] << "\n";
    }
    return 0;
}