abstract class Employee { String name; Employee(String name){this.name=name;} abstract double calculateSalary(); abstract void displayInfo(); }
class Manager extends Employee { Manager(String n){super(n);} double calculateSalary(){return 80000;} void displayInfo(){System.out.println("Manager "+name+" "+calculateSalary());} }
class Programmer extends Employee { Programmer(String n){super(n);} double calculateSalary(){return 65000;} void displayInfo(){System.out.println("Programmer "+name+" "+calculateSalary());} }
public class Q10_AbstractEmployees { public static void main(String[] a){Employee[] e={new Manager("Asha"),new Programmer("Ravi")};for(Employee x:e)x.displayInfo();} }
