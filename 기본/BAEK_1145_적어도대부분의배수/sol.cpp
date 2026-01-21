#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<int> arr(5);

    for (int i=0; i<5; i++) {
        cin >> arr[i];
    }

    int num = 1;

    while (true) {
        int count = 0;

        for (int i=0; i<5; i++) {
            if (num%arr[i]==0) {
                count++;
            }
        }

        if (count >= 3) {
            cout << num << "\n";
            break;
        }
        num++;
    }
    return 0;
}
