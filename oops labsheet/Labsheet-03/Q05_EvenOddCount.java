import java.util.Scanner;
// Modulus classifies every array element as even or odd.
public class Q05_EvenOddCount { public static void main(String[] a){Scanner s=new Scanner(System.in);int[] v=new int[5];int even=0,odd=0;for(int i=0;i<5;i++){v[i]=s.nextInt();if(v[i]%2==0)even++;else odd++;}System.out.println("Even: "+even+", Odd: "+odd);} }
