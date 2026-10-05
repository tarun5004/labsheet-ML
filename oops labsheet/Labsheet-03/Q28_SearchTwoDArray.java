import java.util.Scanner;
// Search records both row and column, which together locate a matrix value.
public class Q28_SearchTwoDArray { public static void main(String[] a){Scanner s=new Scanner(System.in);int[][] m=new int[3][3];for(int i=0;i<3;i++)for(int j=0;j<3;j++)m[i][j]=s.nextInt();int target=s.nextInt();for(int i=0;i<3;i++)for(int j=0;j<3;j++)if(m[i][j]==target)System.out.println("Row "+i+", Column "+j); } }
