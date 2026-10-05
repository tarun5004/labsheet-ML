import java.util.Scanner;
// Logical AND combines the leap-year rule with the requested range.
public class Q10_LeapYearInRange { public static void main(String[] a) { Scanner s=new Scanner(System.in); int y=s.nextInt(),low=s.nextInt(),high=s.nextInt(); boolean leap=y%400==0||y%4==0&&y%100!=0; System.out.println(leap&&y>=low&&y<=high); } }
