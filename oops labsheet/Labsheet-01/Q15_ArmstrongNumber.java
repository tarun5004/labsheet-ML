import java.util.Scanner;

// For a 3-digit number, Armstrong means the sum of digit cubes equals the number.
public class Q15_ArmstrongNumber {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a 3-digit number: ");
        int number = scanner.nextInt();
        int original = number;
        int sum = 0;
        while (number != 0) {
            int digit = number % 10;
            sum += digit * digit * digit;
            number /= 10;
        }
        System.out.println(original >= 100 && original <= 999 && sum == original
                ? "Armstrong number" : "Not an Armstrong number");
    }
}
