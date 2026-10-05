import java.util.Scanner;
// Accumulating into sum visits every element exactly once.
public class Q03_ArraySum { public static void main(String[] a){Scanner s=new Scanner(System.in);int[] v=new int[5];int sum=0;for(int i=0;i<v.length;i++){v[i]=s.nextInt();sum+=v[i];}System.out.println(sum);} }
