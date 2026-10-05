import java.util.Scanner;
// Integer.rotateLeft preserves bits that would otherwise fall off the left side.
public class Q17_CyclicLeftRotate { public static void main(String[] a) { Scanner s=new Scanner(System.in); int n=s.nextInt(); System.out.println(Integer.rotateLeft(n,2)); } }
