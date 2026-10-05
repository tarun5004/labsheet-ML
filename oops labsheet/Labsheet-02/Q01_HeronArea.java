import java.util.Scanner;
// Heron's formula uses the semi-perimeter to find a triangle area.
public class Q01_HeronArea { public static void main(String[] a) { Scanner s=new Scanner(System.in); double x=s.nextDouble(),y=s.nextDouble(),z=s.nextDouble(); double p=(x+y+z)/2; System.out.println(Math.sqrt(p*(p-x)*(p-y)*(p-z))); } }
