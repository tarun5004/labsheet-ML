import java.util.Scanner;
// do-while guarantees the password is requested at least once.
public class Q20_PasswordDoWhile { public static void main(String[] a) { Scanner s=new Scanner(System.in); String password; do{System.out.print("Password: ");password=s.next();}while(!password.equals("java123")); System.out.println("Correct password"); } }
