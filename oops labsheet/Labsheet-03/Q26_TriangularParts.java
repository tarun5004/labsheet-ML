import java.util.Scanner;
// Index comparison separates upper (column >= row) and lower cells.
public class Q26_TriangularParts { public static void main(String[] a){Scanner s=new Scanner(System.in);int[][] m=new int[3][3];for(int i=0;i<3;i++)for(int j=0;j<3;j++)m[i][j]=s.nextInt();System.out.println("Upper:");for(int i=0;i<3;i++){for(int j=0;j<3;j++)System.out.print(j>=i?m[i][j]+" ":"0 ");System.out.println();}System.out.println("Lower:");for(int i=0;i<3;i++){for(int j=0;j<3;j++)System.out.print(i>=j?m[i][j]+" ":"0 ");System.out.println();}} }
