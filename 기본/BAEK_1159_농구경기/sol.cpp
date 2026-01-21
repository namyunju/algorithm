#include <iostream>
#include <string>   // c++은 int, double, char 정도가 기본
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    // 각 성의 등장 횟수를 기록
    // a가 0, b가 1, ... z가 25 
    // 사전식 배열
    int cnt[26] = {0};

    for (int i=0; i<N; i++) {
        string name;
        cin >> name;

        // 이름 첫 글자 
        // -'a'를 이용해 문자를 0~25 사이의 숫자로 변환
        cnt[name[0]-'a']++;
    }

    // 동일 성 5명 이상 여부
    bool possible = false;

    for (int i=0; i<26; i++) {
        if (cnt[i] >= 5) {
            // 다시 숫자를 문자로 바꾸어 줌
            // (char) 
            cout << (char)(i+'a');
            possible = true;
        }
    }
    
    // 불가능한 경우
    if (!possible) {
        cout << "PREDAJA";
    }
    return 0;
}
