#include <iostream>
using namespace std;
int tc;
int N;
int M;
 
int solve(int n, int m, int now) {
    if (m==0) {
        return now;
    }
    return solve(n,m-1,now*n);
}
int main() {
    int T = 10;
    for (int i=0; i<T; i++) {
        cin >> tc;
        cin >> N >> M;
        int ans = solve(N,M,1);
        cout << "#" << tc << " " << ans << "\n";
    }
    return 0;
}