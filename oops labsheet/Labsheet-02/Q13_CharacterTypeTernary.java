import java.util.Scanner;
// Ternary expressions are useful for a short mutually-exclusive classification.
public class Q13_CharacterTypeTernary { public static void main(String[] a) { Scanner s=new Scanner(System.in); char c=s.next().charAt(0); String r=Character.isDigit(c)?"Digit":("aeiouAEIOU".indexOf(c)>=0?"Vowel":Character.isLetter(c)?"Consonant":"Special symbol"); System.out.println(r); } }
