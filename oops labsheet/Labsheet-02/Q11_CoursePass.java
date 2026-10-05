import java.util.Scanner;
// Parentheses make the required theory/practical OR overall rule explicit.
public class Q11_CoursePass { public static void main(String[] a) { Scanner s=new Scanner(System.in); double theory=s.nextDouble(),practical=s.nextDouble(),overall=s.nextDouble(); System.out.println(theory>=40&&practical>=50||overall>=50?"Pass":"Fail"); } }
