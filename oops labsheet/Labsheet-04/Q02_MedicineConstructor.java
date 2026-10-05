class Medicine { String name; double price; Medicine(String name,double price){this.name=name;this.price=price;} void display(){System.out.println(name+" "+price);} }
// this distinguishes constructor parameters from instance variables.
public class Q02_MedicineConstructor { public static void main(String[] a){new Medicine("Vitamin C",120).display();} }
