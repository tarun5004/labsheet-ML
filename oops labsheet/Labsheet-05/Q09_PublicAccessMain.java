class Hospital { public String hospitalName="City Hospital"; public String hospitalCode="CH01"; public Hospital(){} public void displayHospital(){System.out.println(hospitalName+" "+hospitalCode);} }
public class Q09_PublicAccessMain { public static void main(String[] a){Hospital h=new Hospital();System.out.println(h.hospitalName);System.out.println(h.hospitalCode);h.displayHospital();} }
