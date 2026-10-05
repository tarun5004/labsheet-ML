import java.util.Scanner;
// The compound assignment /= updates the same variable repeatedly.
public class Q06_HalfUsingAssignment { public static void main(String[] a) { Scanner s=new Scanner(System.in); double n=s.nextDouble(); int steps=0; while(n>=1){n/=2;steps++;} System.out.println("Steps: "+steps); } }
