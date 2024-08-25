#include <stdio.h>

int main() {
    int n;

    // Get the number of rows 
    printf("Enter the number of rows for the diamond pattern: ");
    scanf("%d", &n);

    // Upper half
    for (int i = 1; i <= n; i += 2) {
        for (int j = 0; j < (n - i) / 2; j++) printf(" ");
        for (int k = 0; k < i; k++) printf("*");
        printf("\n");
    }

    // Lower half
    for (int i = n - 2; i >= 1; i -= 2) {
        for (int j = 0; j < (n - i) / 2; j++) printf(" ");
        for (int k = 0; k < i; k++) printf("*");
        printf("\n");
    }

    return 0;
}