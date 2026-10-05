import java.util.Scanner;
// Shifting left/right by k is multiplication/division by 2 to the power k.
public class Q16_ShiftMultiplyDivide { public static void main(String[] a) { Scanner s=new Scanner(System.in); int n=s.nextInt(),k=s.nextInt(); System.out.println("Multiply: "+(n<<k)); System.out.println("Divide: "+(n>>k)); } }
