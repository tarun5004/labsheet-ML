import java.util.Scanner;
// A 3-D array needs three indexes: layer, row, and column.
public class Q14_DisplayThreeDArray { public static void main(String[] a){Scanner s=new Scanner(System.in);int[][][] v=new int[2][2][2];for(int i=0;i<2;i++)for(int j=0;j<2;j++)for(int k=0;k<2;k++)v[i][j][k]=s.nextInt();for(int[][] layer:v){for(int[] row:layer){for(int n:row)System.out.print(n+" ");System.out.println();}System.out.println();}} }
