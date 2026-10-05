class Staff { protected String name; Staff(String n){name=n;} }
class Doctor extends Staff { Doctor(String n){super(n);} void display(){System.out.println("Doctor: "+name);} }
class HospitalPharmacist extends Staff { HospitalPharmacist(String n){super(n);} void display(){System.out.println("Pharmacist: "+name);} }
// Two children share one parent: this is hierarchical inheritance.
public class Q10_HierarchicalStaff { public static void main(String[] a){new Doctor("Asha").display();new HospitalPharmacist("Kabir").display();} }
