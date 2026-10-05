class Pharmacy { static String name="HealthCare"; String location; Pharmacy(String l){location=l;} void display(){System.out.println(name+" - "+location);} }
// static data is shared by every Pharmacy object.
public class Q03_PharmacyStatic { public static void main(String[] a){new Pharmacy("Delhi").display();new Pharmacy("Pune").display();} }
