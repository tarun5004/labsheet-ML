import java.util.Scanner;
// Copy only values not already present in the result prefix.
public class Q24_RemoveDuplicates { public static void main(String[] a){Scanner s=new Scanner(System.in);int[] v=new int[6],u=new int[6];int size=0;for(int i=0;i<6;i++)v[i]=s.nextInt();for(int n:v){boolean exists=false;for(int j=0;j<size;j++)if(u[j]==n)exists=true;if(!exists)u[size++]=n;}for(int i=0;i<size;i++)System.out.print(u[i]+" ");} }
