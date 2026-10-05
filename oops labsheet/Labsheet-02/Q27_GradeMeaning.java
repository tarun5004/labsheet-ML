import java.util.Scanner;
// Multiple case labels let several grades share one meaning.
public class Q27_GradeMeaning { public static void main(String[] a) { Scanner s=new Scanner(System.in); char g=Character.toUpperCase(s.next().charAt(0)); switch(g){case 'A':System.out.println("Excellent");break;case 'B':System.out.println("Good");break;case 'C':System.out.println("Average");break;case 'D':System.out.println("Pass");break;case 'E':case 'F':System.out.println("Needs improvement");break;default:System.out.println("Invalid grade");} } }
