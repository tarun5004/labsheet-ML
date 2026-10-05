import java.util.Scanner;
// Compare matching characters manually so the first different character decides.
public class Q09_StringLexicographicOrder { public static void main(String[] a) { Scanner s=new Scanner(System.in); String x=s.next(),y=s.next(); int n=Math.min(x.length(),y.length()),result=0; for(int i=0;i<n;i++){if(x.charAt(i)!=y.charAt(i)){result=x.charAt(i)<y.charAt(i)?-1:1;break;}} if(result==0) result=Integer.compare(x.length(),y.length()); System.out.println(result<0?x+" comes first":result>0?y+" comes first":"Equal"); } }
