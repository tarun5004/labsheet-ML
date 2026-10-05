import java.util.Scanner;
// Copying each index creates a separate destination array.
public class Q06_CopyArray { public static void main(String[] a){Scanner s=new Scanner(System.in);int[] source=new int[5],copy=new int[5];for(int i=0;i<5;i++){source[i]=s.nextInt();copy[i]=source[i];}for(int n:copy)System.out.print(n+" ");} }
