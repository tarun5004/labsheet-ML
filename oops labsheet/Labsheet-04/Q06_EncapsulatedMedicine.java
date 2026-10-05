class Product { private String name="Paracetamol"; private double price=50; void display(){System.out.println(name+" "+price);} }
// private fields can be used by the class's own method but not directly by main.
public class Q06_EncapsulatedMedicine { public static void main(String[] a){new Product().display();} }
