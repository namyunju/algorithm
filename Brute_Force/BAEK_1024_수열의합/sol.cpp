// 수열의 합
// 연속된 수들의 합
// 계단식으로 생각하기
// 길이가 len일 때 
// 총합 = 시작 수 * len + (0+1+2+3+ ... + len-1)
#include <iostream>
#include <vector>
using namespace std;

int N, L;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> L;
    
    for (int len = L; len <= 100; len++) {
        int t = (len*(len-1)) / 2;

        // 시작 수
        if ((N-t)%len == 0 && (N-t)/len >=0){
            int start = (N-t) / len;
            for (int i = start; i<= start+len-1; i++) {
                cout << i << " ";
            }
            return 0;
        }
    }
    cout << -1;
    
    return 0;
}