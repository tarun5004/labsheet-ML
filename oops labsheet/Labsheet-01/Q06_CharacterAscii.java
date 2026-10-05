import java.util.Scanner;

// char can be converted to int to display its Unicode/ASCII code value.
public class Q06_CharacterAscii {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a character: ");
        char character = scanner.next().charAt(0);
        System.out.println("Code value: " + (int) character);
    }
}
