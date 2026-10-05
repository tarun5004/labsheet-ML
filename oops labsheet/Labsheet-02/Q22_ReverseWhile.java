import java.util.Scanner;
// Extracting the last digit and dividing by ten reverses an integer.
public class Q22_ReverseWhile { public static void main(String[] a) { Scanner s=new Scanner(System.in); int n=s.nextInt(),r=0; while(n!=0){r=r*10+n%10;n/=10;} System.out.println(r); } }
