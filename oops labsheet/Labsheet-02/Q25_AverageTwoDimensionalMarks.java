// A nested for-each visits every row and every mark in a 2-D array.
public class Q25_AverageTwoDimensionalMarks { public static void main(String[] a) { int[][] marks={{70,80,90},{60,75,85}}; int total=0,count=0; for(int[] row:marks)for(int mark:row){total+=mark;count++;} System.out.println((double)total/count); } }
