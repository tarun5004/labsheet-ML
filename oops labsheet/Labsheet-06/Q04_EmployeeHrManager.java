class Employee { void work(){System.out.println("Employee is working");} double getSalary(){return 40000;} }
class HRManager extends Employee { @Override void work(){System.out.println("HR manager is managing people");} void addEmployee(){System.out.println("Employee added");} }
public class Q04_EmployeeHrManager { public static void main(String[] a){HRManager h=new HRManager();h.work();System.out.println(h.getSalary());h.addEmployee();} }
