import java.util.Scanner;
// Three positive angles form a triangle exactly when their sum is 180 degrees.
public class Q08_ValidTriangleAngles { public static void main(String[] a) { Scanner s=new Scanner(System.in); int x=s.nextInt(),y=s.nextInt(),z=s.nextInt(); System.out.println(x>0&&y>0&&z>0&&x+y+z==180?"Valid":"Invalid"); } }
