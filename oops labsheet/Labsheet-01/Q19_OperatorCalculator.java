import java.util.Scanner;

// The switch selects the operation represented by the entered operator.
public class Q19_OperatorCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter two numbers and an operator (+ - * /): ");
        double first = scanner.nextDouble();
        double second = scanner.nextDouble();
        char operator = scanner.next().charAt(0);
        if (operator == '+' || operator == '-' || operator == '*' || operator == '/') {
            if (operator == '/' && second == 0) System.out.println("Cannot divide by zero.");
            else if (operator == '+') System.out.println(first + second);
            else if (operator == '-') System.out.println(first - second);
            else if (operator == '*') System.out.println(first * second);
            else System.out.println(first / second);
        } else {
            System.out.println("Invalid operator.");
        }
    }
}
