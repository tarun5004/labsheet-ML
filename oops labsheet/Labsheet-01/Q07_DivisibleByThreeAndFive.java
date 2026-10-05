import java.util.Scanner;

// && requires both divisibility conditions to be true.
public class Q07_DivisibleByThreeAndFive {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int number = scanner.nextInt();
        System.out.println(number % 3 == 0 && number % 5 == 0
                ? "Divisible by both 3 and 5" : "Not divisible by both");
    }
}
