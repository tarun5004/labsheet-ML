import java.util.Scanner;
// Nested loops are needed because a matrix has rows and columns.
public class Q07_DisplayMatrix { public static void main(String[] a){Scanner s=new Scanner(System.in);int[][] m=new int[3][3];for(int i=0;i<3;i++)for(int j=0;j<3;j++)m[i][j]=s.nextInt();for(int[] r:m){for(int n:r)System.out.print(n+" ");System.out.println();}} }
