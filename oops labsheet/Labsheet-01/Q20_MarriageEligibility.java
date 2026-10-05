import java.util.Scanner;

// Eligibility depends on both gender and the corresponding minimum age.
public class Q20_MarriageEligibility {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter age and gender (M/F): ");
        int age = scanner.nextInt();
        char gender = Character.toUpperCase(scanner.next().charAt(0));
        boolean eligible;
        if (gender == 'M') eligible = age >= 21;
        else if (gender == 'F') eligible = age >= 18;
        else eligible = false;
        System.out.println(eligible ? "Eligible" : "Not eligible");
    }
}
