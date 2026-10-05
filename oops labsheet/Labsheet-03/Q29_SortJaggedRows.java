import java.util.Arrays;
// Sorting each row separately preserves the jagged structure.
public class Q29_SortJaggedRows { public static void main(String[] a){int[][] v={{4,1,3},{9,2},{8,7,5,6}};for(int[] row:v){Arrays.sort(row);for(int n:row)System.out.print(n+" ");System.out.println();}} }
