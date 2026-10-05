import java.util.Scanner;
// Main diagonal uses equal indexes; secondary diagonal indexes add to size-1.
public class Q25_DiagonalSums { public static void main(String[] a){Scanner s=new Scanner(System.in);int[][] m=new int[3][3];for(int i=0;i<3;i++)for(int j=0;j<3;j++)m[i][j]=s.nextInt();int main=0,secondary=0;for(int i=0;i<3;i++){main+=m[i][i];secondary+=m[i][2-i];}System.out.println(main+" "+secondary);} }
