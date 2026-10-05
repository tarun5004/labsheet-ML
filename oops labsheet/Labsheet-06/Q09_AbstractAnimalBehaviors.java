abstract class Animal { abstract void eat(); abstract void sleep(); }
class Lion extends Animal { void eat(){System.out.println("Lion eats meat");} void sleep(){System.out.println("Lion sleeps in den");} }
class Tiger extends Animal { void eat(){System.out.println("Tiger eats prey");} void sleep(){System.out.println("Tiger sleeps in forest");} }
class Deer extends Animal { void eat(){System.out.println("Deer eats grass");} void sleep(){System.out.println("Deer rests in herd");} }
public class Q09_AbstractAnimalBehaviors { public static void main(String[] a){Animal[] animals={new Lion(),new Tiger(),new Deer()};for(Animal animal:animals){animal.eat();animal.sleep();}} }
