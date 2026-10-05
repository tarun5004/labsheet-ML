class Vehicle { void drive(){System.out.println("Driving a vehicle");} }
class Car extends Vehicle { @Override void drive(){System.out.println("Repairing a car");} }
public class Q02_VehicleCar { public static void main(String[] a){new Car().drive();} }
