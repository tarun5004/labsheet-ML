import java.util.Scanner;
// The inner scan counts one value; the visited array prevents duplicate reports.
public class Q22_ElementFrequencies { public static void main(String[] a){Scanner s=new Scanner(System.in);int[] v=new int[6];boolean[] done=new boolean[6];for(int i=0;i<6;i++)v[i]=s.nextInt();for(int i=0;i<6;i++){if(done[i])continue;int count=0;for(int j=0;j<6;j++)if(v[i]==v[j]){count++;done[j]=true;}System.out.println(v[i]+": "+count);}} }
