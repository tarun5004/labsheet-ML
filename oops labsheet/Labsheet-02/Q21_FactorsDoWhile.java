import java.util.Scanner;
// A do-while loop checks every possible divisor at least once.
public class Q21_FactorsDoWhile { public static void main(String[] a) { Scanner s=new Scanner(System.in); int n=s.nextInt(),d=1; do{if(n%d==0)System.out.print(d+" ");d++;}while(d<=n); } }
