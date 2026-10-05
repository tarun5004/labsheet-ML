import java.util.Scanner;

// Relational operators always produce a boolean result.
public class Q04_RelationalOperators {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter two numbers: ");
        int first = scanner.nextInt();
        int second = scanner.nextInt();
        System.out.println("first > second: " + (first > second));
        System.out.println("first < second: " + (first < second));
        System.out.println("first == second: " + (first == second));
        System.out.println("first != second: " + (first != second));
    }
}
