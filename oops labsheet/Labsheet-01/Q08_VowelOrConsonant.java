import java.util.Scanner;

// A vowel check is done after converting the input to lowercase.
public class Q08_VowelOrConsonant {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter an alphabet: ");
        char character = Character.toLowerCase(scanner.next().charAt(0));
        if (character >= 'a' && character <= 'z') {
            System.out.println("aeiou".indexOf(character) >= 0 ? "Vowel" : "Consonant");
        } else {
            System.out.println("Please enter an alphabet.");
        }
    }
}
