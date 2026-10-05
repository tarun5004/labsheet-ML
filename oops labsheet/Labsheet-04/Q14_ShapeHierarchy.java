class Shape { double area(){return 0;} }
class Rectangle extends Shape { double l,w; Rectangle(double l,double w){this.l=l;this.w=w;} double area(){return l*w;} }
class Circle extends Shape { double r; Circle(double r){this.r=r;} double area(){return Math.PI*r*r;} }
// Overriding lets each child calculate its own shape-specific area.
public class Q14_ShapeHierarchy { public static void main(String[] a){Shape[] shapes={new Rectangle(4,5),new Circle(3)};for(Shape shape:shapes)System.out.println(shape.area());} }
