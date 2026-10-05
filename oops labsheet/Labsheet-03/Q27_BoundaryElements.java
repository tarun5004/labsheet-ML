import java.util.Scanner;
// A cell is on the boundary when it touches any edge of the matrix.
public class Q27_BoundaryElements { public static void main(String[] a){Scanner s=new Scanner(System.in);int[][] m=new int[3][3];for(int i=0;i<3;i++)for(int j=0;j<3;j++)m[i][j]=s.nextInt();for(int i=0;i<3;i++){for(int j=0;j<3;j++)System.out.print(i==0||j==0||i==2||j==2?m[i][j]+" ":"  ");System.out.println();}} }
