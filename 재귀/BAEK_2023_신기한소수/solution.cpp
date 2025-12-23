#include <iostream>
#include <cmath>
using namespace std;

int N;
bool isPrime(int n) {
    if (n<2) return false;

    for (int i = 2; i*i <=n; i++) {
        if (n%i==0) return false;
    }
    return true;
}

void dfs(int num, int len) {
    if (len == N) {
        cout << num << "\n";
        return;
    }
    for (int i=1; i<=9; i++) {
        if (i%2 ==0) continue;
        int next_num = num*10+i;
        if (isPrime(next_num)) {
            dfs(next_num, len+1);
        }
    }
}

int main() {
    cin >> N;
    dfs(2,1);
    dfs(3,1);
    dfs(5,1);
    dfs(7,1);
    return 0;
}