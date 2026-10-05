abstract class Animal { abstract void sound(); }
class Lion extends Animal { void sound(){System.out.println("Lion roars");} }
class Tiger extends Animal { void sound(){System.out.println("Tiger growls");} }
// Abstract classes define required behavior; concrete children implement it.
public class Q06_AbstractAnimals { public static void main(String[] a){new Lion().sound();new Tiger().sound();} }
