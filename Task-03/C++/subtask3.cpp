#include <iostream>
#include <string>

using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows for the diamond pattern: ";
    cin >> n;
    // Print the upper half of the diamond
    for (int i = 1; i <= n; i += 2) {
        cout << string((n - i) / 2, ' ') << string(i, '*') << '\n';
    }

    // Print the lower half of the diamond
    for (int i = n - 2; i >= 1; i -= 2) {
        cout << string((n - i) / 2, ' ') << string(i, '*') << '\n';
    }

    return 0;
}
