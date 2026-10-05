class Patient { String classify(int age){return age>=18?"Adult":"Minor";} }
// The method contains the decision so main only coordinates the example.
public class Q05_PatientEligibility { public static void main(String[] a){Patient p=new Patient();System.out.println(p.classify(20));} }
