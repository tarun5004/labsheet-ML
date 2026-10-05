import java.util.Scanner;
// Same-size matrices can be added cell by cell.
public class Q12_AddMatrices { public static void main(String[] a){Scanner s=new Scanner(System.in);int[][] x=new int[3][3],y=new int[3][3];for(int i=0;i<3;i++)for(int j=0;j<3;j++)x[i][j]=s.nextInt();for(int i=0;i<3;i++)for(int j=0;j<3;j++)y[i][j]=s.nextInt();for(int i=0;i<3;i++){for(int j=0;j<3;j++)System.out.print((x[i][j]+y[i][j])+" ");System.out.println();}} }
