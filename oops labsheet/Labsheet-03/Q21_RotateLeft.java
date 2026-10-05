import java.util.Scanner;
// Save the first item, shift the remaining items left, then put it at the end.
public class Q21_RotateLeft { public static void main(String[] a){Scanner s=new Scanner(System.in);int[] v=new int[5];for(int i=0;i<5;i++)v[i]=s.nextInt();int first=v[0];for(int i=0;i<4;i++)v[i]=v[i+1];v[4]=first;for(int n:v)System.out.print(n+" ");} }
