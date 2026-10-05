import java.util.Scanner;

// Reversing the digits and comparing with the original detects a palindrome.
public class Q17_PalindromeNumber {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter an integer: ");
        int number = scanner.nextInt();
        int original = number;
        int reverse = 0;
        while (number != 0) {
            reverse = reverse * 10 + number % 10;
            number /= 10;
        }
        System.out.println(original == reverse ? "Palindrome" : "Not a palindrome");
    }
}
