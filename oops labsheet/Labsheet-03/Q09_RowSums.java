import java.util.Scanner;
// Reset sum for each row so every row gets its own result.
public class Q09_RowSums { public static void main(String[] a){Scanner s=new Scanner(System.in);int[][] m=new int[3][3];for(int i=0;i<3;i++)for(int j=0;j<3;j++)m[i][j]=s.nextInt();for(int[] r:m){int sum=0;for(int n:r)sum+=n;System.out.println(sum);}} }
