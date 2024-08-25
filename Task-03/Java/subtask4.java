import java.io.File;
import java.io.FileWriter;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Read the number
        Scanner fileScanner = new Scanner(new File("input.txt"));
        int n = fileScanner.nextInt(); 
        fileScanner.close();
        
        StringBuilder output = new StringBuilder();

        // Upper half of the diamond
        for (int i = 1; i <= n; i += 2) {
            output.append(" ".repeat((n - i) / 2));
            output.append("*".repeat(i)).append("\n");
        }

        // Lower half of the diamond
        for (int i = n - 2; i >= 1; i -= 2) {
            output.append(" ".repeat((n - i) / 2));
            output.append("*".repeat(i)).append("\n");
        }

        // Write the diamond pattern to output.txt
        FileWriter fileWriter = new FileWriter("output.txt");
        fileWriter.write(output.toString());
        fileWriter.close();
    }
}