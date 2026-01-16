#include <iostream>
#include <string>

using namespace std;

string octToBin[] = {
    "000", "001", "010", "011", "100", "101", "110", "111"
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    cin >> s;

    if (s == "0") {
        cout << "0";
        return 0;
    }

    int firstDigit = s[0] - '0';

    if (firstDigit == 1) cout << "1";
    else if (firstDigit == 2) cout << "10"; 
    else if (firstDigit == 3) cout << "11";
    else cout << octToBin[firstDigit];

    for (int i=1; i<s.length(); i++) {
        cout << octToBin[s[i]-'0'];
    }
    return 0;
}