import java.util.Scanner;

// Scanner reads input; arithmetic operators perform the five calculations.
public class Q02_ArithmeticOperations {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter two integers: ");
        int first = scanner.nextInt();
        int second = scanner.nextInt();

        System.out.println("Addition: " + (first + second));
        System.out.println("Subtraction: " + (first - second));
        System.out.println("Multiplication: " + (first * second));
        if (second != 0) {
            System.out.println("Division: " + (first / second));
            System.out.println("Modulus: " + (first % second));
        } else {
            System.out.println("Division and modulus by zero are not allowed.");
        }
    }
}
