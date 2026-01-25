#include <iostream>
#include <string>
#include <stack>

using namespace std;

/* 
< 가 나오면 > 가 나올 때까지 그대로 출력
공백 나오면 이전까지 나온 문자 뒤집기
stack 사용
push() / pop() 반환없이 삭제 / top() 삭제없이 반환 / empty() / size() 
*/

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string S;
    // 공백 포함 한 줄 전체 읽기
    getline(cin, S);
    S += '\n';

    bool is_tag = false;

    stack<char> st;

    for (char ch : S) {
        // 태그 시작 시 이전까지 쌓인 것들 출력 
        if (ch == '<') {
            while (!st.empty()) {
                cout << st.top();
                st.pop();
            }
            is_tag = true;
            cout << ch;
        }
        // 태그 끝
        else if (ch == '>') {
            cout << ch;
            is_tag = false;
        }
        // 태그 안이라면
        else if (is_tag) {
            cout << ch;
        }
        else {
            // 공백, 줄바꿈 문자열 구분
            if (ch == ' ' || ch == '\n') {
                while (!st.empty()) {
                    cout << st.top();
                    st.pop();
                }
                // 공백도 출력
                if (ch == ' ') {
                    cout << ch;
                }
            }
            else {
                st.push(ch);
            }
        }
    }
    return 0;
}