import java.util.Scanner;

// Character helper methods make the classification readable and safe.
public class Q14_CharacterClassification {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a character: ");
        char character = scanner.next().charAt(0);
        if (Character.isDigit(character)) {
            System.out.println("Digit");
        } else if (Character.isUpperCase(character)) {
            System.out.println("Uppercase letter");
        } else if (Character.isLowerCase(character)) {
            System.out.println("Lowercase letter");
        } else {
            System.out.println("Special character");
        }
    }
}
