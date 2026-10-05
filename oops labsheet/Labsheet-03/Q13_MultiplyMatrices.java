import java.util.Scanner;
// Matrix multiplication uses a third loop for the shared row/column dimension.
public class Q13_MultiplyMatrices { public static void main(String[] a){Scanner s=new Scanner(System.in);int[][] x=new int[3][3],y=new int[3][3],r=new int[3][3];for(int i=0;i<3;i++)for(int j=0;j<3;j++)x[i][j]=s.nextInt();for(int i=0;i<3;i++)for(int j=0;j<3;j++)y[i][j]=s.nextInt();for(int i=0;i<3;i++)for(int j=0;j<3;j++)for(int k=0;k<3;k++)r[i][j]+=x[i][k]*y[k][j];for(int[] row:r){for(int n:row)System.out.print(n+" ");System.out.println();}} }
