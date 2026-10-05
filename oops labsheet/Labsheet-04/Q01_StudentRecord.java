class Student { String name; int rollNo; Student(String n,int r){name=n;rollNo=r;} void display(){System.out.println(name+" "+rollNo);} }
// main creates the object; the Student class owns display behavior.
public class Q01_StudentRecord { public static void main(String[] a){new Student("Aarav",1).display();} }
