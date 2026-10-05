import java.util.Scanner;
// Initialize max from the first value to handle any integer range.
public class Q17_ThreeDMaximum { public static void main(String[] a){Scanner s=new Scanner(System.in);int max=Integer.MIN_VALUE;for(int i=0;i<2;i++)for(int j=0;j<2;j++)for(int k=0;k<2;k++){int n=s.nextInt();if(n>max)max=n;}System.out.println(max);} }
