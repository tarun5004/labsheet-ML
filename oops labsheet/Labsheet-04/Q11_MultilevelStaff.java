class Person { protected String name; Person(String n){name=n;} }
class StaffMember extends Person { StaffMember(String n){super(n);} }
class Manager extends StaffMember { Manager(String n){super(n);} void display(){System.out.println("Manager: "+name);} }
// Manager receives the Person state through the complete inheritance chain.
public class Q11_MultilevelStaff { public static void main(String[] a){new Manager("Neha").display();} }
