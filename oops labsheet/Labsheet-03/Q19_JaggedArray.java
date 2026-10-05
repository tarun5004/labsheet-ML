// Jagged rows may have different lengths because Java stores each row separately.
public class Q19_JaggedArray { public static void main(String[] a){int[][] v={{1,2},{3,4,5},{6,7,8,9}};for(int[] row:v){for(int n:row)System.out.print(n+" ");System.out.println();}} }
