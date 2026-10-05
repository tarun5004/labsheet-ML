import java.util.Scanner;

// Explicit casting converts a double to an int and removes its decimal part.
public class Q05_ExplicitTypeCasting {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a decimal number: ");
        double original = scanner.nextDouble();
        int converted = (int) original;
        System.out.println("Original: " + original);
        System.out.println("Converted: " + converted);
    }
}
