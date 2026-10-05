import java.util.Scanner;
// XOR can swap two integers without a third storage variable.
public class Q14_XorSwap { public static void main(String[] a) { Scanner s=new Scanner(System.in); int x=s.nextInt(),y=s.nextInt(); x^=y;y^=x;x^=y; System.out.println(x+" "+y); } }
