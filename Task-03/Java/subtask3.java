import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);    // inputing values 
        System.out.print("Enter number- ");  
        int n = sc.nextInt(); 

        // Upper half 
        for (int i = 0; i < n; i += 2) {
            for (int j = n - 1; j > i; j--) {
                System.out.print(" ");
            }
            for (int k = 0; k <= i; k++) {
                System.out.print("* ");
            }
            System.out.println();
        }

        // Lower half
        for (int i = n - 3; i >= 0; i -= 2) {
            // Print spaces
            for (int j = n - 1; j > i; j--) {
                System.out.print(" ");
            }
            for (int k = 0; k <= i; k++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}
