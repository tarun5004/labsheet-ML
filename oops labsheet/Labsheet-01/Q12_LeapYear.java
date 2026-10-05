import java.util.Scanner;

// A century is a leap year only when it is also divisible by 400.
public class Q12_LeapYear {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a year: ");
        int year = scanner.nextInt();
        boolean leap = year % 400 == 0 || year % 4 == 0 && year % 100 != 0;
        System.out.println(leap ? "Leap year" : "Not a leap year");
    }
}
