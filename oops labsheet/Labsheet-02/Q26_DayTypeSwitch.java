import java.util.Scanner;
// switch groups Saturday and Sunday as weekend cases.
public class Q26_DayTypeSwitch { public static void main(String[] a) { Scanner s=new Scanner(System.in); int day=s.nextInt(); switch(day){case 6:case 7:System.out.println("Weekend");break;case 1:case 2:case 3:case 4:case 5:System.out.println("Weekday");break;default:System.out.println("Invalid day");} } }
