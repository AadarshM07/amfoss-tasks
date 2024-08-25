//Write a program that reads a string from a file named input.txt and writes that string to another file named output.txt.
#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::ifstream input("input.txt");  // Open input file for reading
    std::ofstream output("output.txt"); // Open output file for writing


    std::string line;

    // Read the string from input file and write it to output file
    while (std::getline(input, line)) {
        output << line << std::endl;
    }

    // Close the files
    input.close();
    output.close();

    return 0;
}
