class Pharmacy { String medicineName="Syrup"; double price=100; Pharmacy(){} void displayMedicine(){System.out.println(medicineName+" "+price);} }
public class Q11_DefaultAccessMain { public static void main(String[] a){Pharmacy p=new Pharmacy();System.out.println(p.medicineName);p.displayMedicine();} }
