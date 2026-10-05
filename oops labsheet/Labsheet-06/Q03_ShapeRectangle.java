class Shape { double getArea(){return 0;} }
class Rectangle extends Shape { private double length,width; Rectangle(double l,double w){length=l;width=w;} @Override double getArea(){return length*width;} }
// The Rectangle implementation supplies the meaningful area calculation.
public class Q03_ShapeRectangle { public static void main(String[] a){System.out.println(new Rectangle(4,5).getArea());} }
