import java.util.Scanner;

// Passing requires at least 40% in every subject, not only in the total.
public class Q09_MarksResult {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter marks for three subjects: ");
        double first = scanner.nextDouble();
        double second = scanner.nextDouble();
        double third = scanner.nextDouble();
        double total = first + second + third;
        double percentage = total / 3;
        boolean passed = first >= 40 && second >= 40 && third >= 40;
        System.out.println("Total: " + total);
        System.out.println("Percentage: " + percentage);
        System.out.println(passed ? "Pass" : "Fail");
    }
}
