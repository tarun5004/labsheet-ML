import java.util.Scanner;
// += accumulates each day's rainfall into one total.
public class Q07_WeeklyRainfall { public static void main(String[] a) { Scanner s=new Scanner(System.in); double total=0; for(int i=1;i<=7;i++) total+=s.nextDouble(); System.out.println("Total: "+total); } }
