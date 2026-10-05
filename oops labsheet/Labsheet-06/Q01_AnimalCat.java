class Animal { void makeSound(){System.out.println("Animal sound");} }
class Cat extends Animal { @Override void makeSound(){System.out.println("Cat says: Meow");} }
// Overriding lets the child replace inherited behavior.
public class Q01_AnimalCat { public static void main(String[] a){new Cat().makeSound();} }
