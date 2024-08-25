#include <stdio.h>

int main() {
    FILE *inputFile = fopen("input.txt", "r");
    FILE *outputFile = fopen("output.txt", "w");
    int n;
    
     if (inputFile == NULL || outputFile == NULL) {
        perror("Error opening file");
        return 1;
    }
    // Upper half
    for (int i = 1; i <= n; i += 2) {
        for (int j = 0; j < (n - i) / 2; j++) fprintf(outputFile, " ");
        for (int k = 0; k < i; k++) fprintf(outputFile, "*");
        fprintf(outputFile, "\n");
    }
    // Lower half
    for (int i = n - 2; i >= 1; i -= 2) {
        for (int j = 0; j < (n - i) / 2; j++) fprintf(outputFile, " ");
        for (int k = 0; k < i; k++) fprintf(outputFile, "*");
        fprintf(outputFile, "\n");
    }
    // Close files
    fclose(inputFile);
    fclose(outputFile);

    return 0;
}

