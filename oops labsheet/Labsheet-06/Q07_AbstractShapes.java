abstract class Shape { abstract double calculateArea(); abstract double calculatePerimeter(); }
class Circle extends Shape { double r; Circle(double r){this.r=r;} double calculateArea(){return Math.PI*r*r;} double calculatePerimeter(){return 2*Math.PI*r;} }
class Triangle extends Shape { double x,y,z; Triangle(double x,double y,double z){this.x=x;this.y=y;this.z=z;} double calculateArea(){double p=(x+y+z)/2;return Math.sqrt(p*(p-x)*(p-y)*(p-z));} double calculatePerimeter(){return x+y+z;} }
public class Q07_AbstractShapes { public static void main(String[] a){Shape c=new Circle(3),t=new Triangle(3,4,5);System.out.println(c.calculateArea()+" "+c.calculatePerimeter());System.out.println(t.calculateArea()+" "+t.calculatePerimeter());} }
