class Person { protected String name; protected int age; Person(String name,int age){this.name=name;this.age=age;} }
class Employee extends Person { private int employeeId; Employee(String name,int age,int employeeId){super(name,age);this.employeeId=employeeId;} }
class Manager extends Employee { private int teamSize; Manager(String name,int age,int employeeId,int teamSize){super(name,age,employeeId);this.teamSize=teamSize;} void displayManager(){System.out.println(name+" "+age+" team="+teamSize);} }
public class Q15_MultilevelMain { public static void main(String[] a){new Manager("Neha",40,10,6).displayManager();} }
