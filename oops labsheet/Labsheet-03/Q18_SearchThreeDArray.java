import java.util.Scanner;
// Store matching coordinates when the requested value is found.
public class Q18_SearchThreeDArray { public static void main(String[] a){Scanner s=new Scanner(System.in);int[][][] v=new int[2][2][2];for(int i=0;i<2;i++)for(int j=0;j<2;j++)for(int k=0;k<2;k++)v[i][j][k]=s.nextInt();int target=s.nextInt();boolean found=false;for(int i=0;i<2;i++)for(int j=0;j<2;j++)for(int k=0;k<2;k++)if(v[i][j][k]==target){System.out.println(i+" "+j+" "+k);found=true;}if(!found)System.out.println("Not found");} }
