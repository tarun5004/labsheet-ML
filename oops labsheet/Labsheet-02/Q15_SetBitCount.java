import java.util.Scanner;
// n & (n - 1) removes the lowest set bit on every loop.
public class Q15_SetBitCount { public static void main(String[] a) { Scanner s=new Scanner(System.in); int n=s.nextInt(),count=0; while(n!=0){n&=n-1;count++;} System.out.println(count); } }
