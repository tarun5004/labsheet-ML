import java.util.Scanner;
// Keep the largest and second-largest values updated in one pass.
public class Q23_SecondLargest { public static void main(String[] a){Scanner s=new Scanner(System.in);int[] v=new int[5];for(int i=0;i<5;i++)v[i]=s.nextInt();int largest=Integer.MIN_VALUE,second=Integer.MIN_VALUE;for(int n:v){if(n>largest){second=largest;largest=n;}else if(n>second&&n!=largest)second=n;}System.out.println(second);} }
