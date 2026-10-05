import java.util.Scanner;

// Nested if-else compares the first candidate with the remaining values.
public class Q11_LargestOfThree {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter three numbers: ");
        int first = scanner.nextInt();
        int second = scanner.nextInt();
        int third = scanner.nextInt();
        int largest;
        if (first > second) {
            largest = first > third ? first : third;
        } else {
            largest = second > third ? second : third;
        }
        System.out.println("Largest: " + largest);
    }
}
