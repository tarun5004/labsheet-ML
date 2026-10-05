import java.util.Scanner;
// A number is palindromic when its reverse equals its original value.
public class Q23_PalindromeWhile { public static void main(String[] a) { Scanner s=new Scanner(System.in); int n=s.nextInt(),original=n,r=0; while(n!=0){r=r*10+n%10;n/=10;} System.out.println(original==r?"Palindrome":"Not palindrome"); } }
