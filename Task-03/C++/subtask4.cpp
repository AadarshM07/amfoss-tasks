//sub-task 4  AM@FOSS
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    int n;

    // Open input file for reading
    ifstream inputFile("input.txt");

    // Read the number from the input file
    inputFile >> n;
    inputFile.close();

    // Open output file for writing
    ofstream outputFile("output.txt");
    // Generate and write the diamond pattern to the output file
    for (int i = 1; i <= n; i += 2) {
        outputFile << string((n - i) / 2, ' ') << string(i, '*') << '\n';
    }

    for (int i = n - 2; i >= 1; i -= 2) {
        outputFile << string((n - i) / 2, ' ') << string(i, '*') << '\n';
    }

    outputFile.close();

    return 0;
}
