#include <stdio.h>

int main() {
    
    FILE *input ;  
    FILE*output;
    char c;  
    input = fopen("input.txt","r") ; 
    output = fopen("output.txt","w");
    
    while ((c = fgetc(input)) != EOF) {
        fputc(c, output);
    }
    fclose(input);
    fclose(output);

    return 0;
}