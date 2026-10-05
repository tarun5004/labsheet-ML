import java.util.Scanner;

// A prime has no divisor between 2 and its square root.
public class Q18_PrimeNumber {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int number = scanner.nextInt();
        boolean prime = number >= 2;
        for (int divisor = 2; divisor * divisor <= number && prime; divisor++) {
            if (number % divisor == 0) prime = false;
        }
        System.out.println(prime ? "Prime" : "Not prime");
    }
}
