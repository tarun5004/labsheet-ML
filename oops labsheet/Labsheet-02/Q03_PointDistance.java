import java.util.Scanner;
// The distance formula is the Pythagorean theorem applied to x and y differences.
public class Q03_PointDistance { public static void main(String[] a) { Scanner s=new Scanner(System.in); double x1=s.nextDouble(),y1=s.nextDouble(),x2=s.nextDouble(),y2=s.nextDouble(); System.out.println(Math.hypot(x2-x1,y2-y1)); } }
