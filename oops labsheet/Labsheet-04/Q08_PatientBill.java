class Bill { private double consultation,medicine; void setFees(double c,double m){consultation=c;medicine=m;} double total(){return consultation+medicine;} }
// Calculation belongs to the Bill object instead of being repeated in main.
public class Q08_PatientBill { public static void main(String[] a){Bill bill=new Bill();bill.setFees(300,450);System.out.println(bill.total());} }
