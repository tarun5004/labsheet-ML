import java.util.Scanner;

// A remainder of zero means the number is exactly divisible by two.
public class Q03_EvenOrOdd {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int number = scanner.nextInt();
        System.out.println(number % 2 == 0 ? "Even" : "Odd");
    }
}
