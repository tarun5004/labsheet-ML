import java.util.Scanner;
// for-each visits every array element without managing an index.
public class Q24_ArrayMinMaxForEach { public static void main(String[] a) { Scanner s=new Scanner(System.in); int[] v=new int[5]; for(int i=0;i<v.length;i++)v[i]=s.nextInt(); int min=v[0],max=v[0]; for(int n:v){if(n<min)min=n;if(n>max)max=n;} System.out.println(min+" "+max); } }
