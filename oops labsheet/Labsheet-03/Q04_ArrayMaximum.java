import java.util.Scanner;
// Start with the first value so negative arrays also work correctly.
public class Q04_ArrayMaximum { public static void main(String[] a)
    {
        Scanner s=new Scanner(System.in);int[] 
        v=new int[5];for(int i=0;i<5;i++)v[i]=s.nextInt();int max=v[0];
        for(int n:v)if(n>max)max=n;
        System.out.println(max);
    } 
}
