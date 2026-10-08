import java.util.Scanner;
// Walking from the last index to zero displays the array in reverse.
public class Q02_ReverseArray { public static void main(String[] a)
    {Scanner s=new Scanner(System.in);int[] v=new int[10];
        for(int i=0;i<10;i++)v[i]=s.nextInt();
        for(int i=9;i>=0;i--)System.out.print(v[i]+" ");
    } 
}
