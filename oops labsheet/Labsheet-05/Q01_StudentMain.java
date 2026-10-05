class Student { String name; int rollNo; double marks; Student(){name="Aarav";rollNo=1;marks=82.5;} void displayDetails(){System.out.println(name+" "+rollNo+" "+marks);} }
// main only creates the object; Student owns its display logic.
public class Q01_StudentMain { public static void main(String[] a){new Student().displayDetails();} }
