// Each Fibonacci term is the sum of the two terms before it.
public class Q18_FibonacciTwenty { public static void main(String[] a) { int x=0,y=1; for(int i=0;i<20;i++){System.out.print(x+" "); int next=x+y;x=y;y=next;} } }
