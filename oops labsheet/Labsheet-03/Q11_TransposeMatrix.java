import java.util.Scanner;
// Transpose exchanges row and column positions: result[j][i] = matrix[i][j].
public class Q11_TransposeMatrix { public static void main(String[] a){Scanner s=new Scanner(System.in);int[][] m=new int[3][3];for(int i=0;i<3;i++)for(int j=0;j<3;j++)m[i][j]=s.nextInt();for(int i=0;i<3;i++){for(int j=0;j<3;j++)System.out.print(m[j][i]+" ");System.out.println();}} }
