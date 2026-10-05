class Employee { protected String name; Employee(String n){name=n;} }
class Pharmacist extends Employee { Pharmacist(String n){super(n);} void display(){System.out.println(name+" is a pharmacist");} }
// Pharmacist inherits common employee data through single inheritance.
public class Q09_EmployeePharmacist { public static void main(String[] a){new Pharmacist("Riya").display();} }
