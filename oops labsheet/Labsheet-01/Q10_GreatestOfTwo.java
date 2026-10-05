import java.util.Scanner;

// if-else selects one of the two values, including the equal case.
public class Q10_GreatestOfTwo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter two numbers: ");
        int first = scanner.nextInt();
        int second = scanner.nextInt();
        if (first > second) {
            System.out.println("Greatest: " + first);
        } else if (second > first) {
            System.out.println("Greatest: " + second);
        } else {
            System.out.println("Both numbers are equal.");
        }
    }
}
