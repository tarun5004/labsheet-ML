import java.util.Scanner;
// Compound interest grows the principal by the rate once for every time period.
public class Q02_CompoundInterest { public static void main(String[] a) { Scanner s=new Scanner(System.in); double p=s.nextDouble(),r=s.nextDouble(),t=s.nextDouble(); double amount=p*Math.pow(1+r/100,t); System.out.println("Interest: "+(amount-p)); } }
