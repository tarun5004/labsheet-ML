class HospitalSystem { private String[] staff={"Doctor Asha","Pharmacist Kabir"}; void display(){for(String person:staff)System.out.println(person);} }
// A small system object keeps collection logic outside main.
public class Q15_FinalHospitalSystem { public static void main(String[] a){new HospitalSystem().display();} }
