import java.util.Scanner;
// Nested ternary operators choose the smaller value at each comparison.
public class Q12_SmallestOfFour { public static void main(String[] a) { Scanner s=new Scanner(System.in); int w=s.nextInt(),x=s.nextInt(),y=s.nextInt(),z=s.nextInt(); int m=w<x?w:x; m=m<y?m:y; m=m<z?m:z; System.out.println(m); } }
