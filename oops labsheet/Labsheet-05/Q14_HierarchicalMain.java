class Person { protected String name; protected int age; Person(String name,int age){this.name=name;this.age=age;} void displayPerson(){System.out.println(name+" "+age);} }
class Doctor extends Person { private String specialization; Doctor(String name,int age,String specialization){super(name,age);this.specialization=specialization;} void displayDoctor(){displayPerson();System.out.println(specialization);} }
class Nurse extends Person { private String ward; Nurse(String name,int age,String ward){super(name,age);this.ward=ward;} void displayNurse(){displayPerson();System.out.println(ward);} }
public class Q14_HierarchicalMain { public static void main(String[] a){new Doctor("Asha",35,"Cardiology").displayDoctor();new Nurse("Isha",28,"Ward A").displayNurse();} }
