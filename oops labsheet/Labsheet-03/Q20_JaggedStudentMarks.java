// Each student row contains only the subjects that student took.
public class Q20_JaggedStudentMarks { public static void main(String[] a){int[][] marks={{80,75},{65,70,72},{90,88,91,85}};for(int i=0;i<marks.length;i++){System.out.print("Student "+(i+1)+": ");for(int n:marks[i])System.out.print(n+" ");System.out.println();}} }
