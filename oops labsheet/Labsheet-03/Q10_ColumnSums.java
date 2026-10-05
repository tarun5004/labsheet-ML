import java.util.Scanner;
// For a column, the row index changes while the column index stays fixed.
public class Q10_ColumnSums { public static void main(String[] a){Scanner s=new Scanner(System.in);int[][] m=new int[3][3];for(int i=0;i<3;i++)for(int j=0;j<3;j++)m[i][j]=s.nextInt();for(int j=0;j<3;j++){int sum=0;for(int i=0;i<3;i++)sum+=m[i][j];System.out.println(sum);}} }
