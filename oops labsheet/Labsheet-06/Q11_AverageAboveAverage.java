import java.util.Scanner;
// this lets the object store its own ten-number data before calculating results.
class NumberAnalyzer { private double[] numbers=new double[10]; void read(Scanner s){for(int i=0;i<numbers.length;i++)numbers[i]=s.nextDouble();} void analyze(){double total=0;for(double n:numbers)total+=n;double average=total/numbers.length;int above=0;for(double n:numbers)if(n>average)above++;System.out.println("Average: "+average);System.out.println("Above average: "+above);} }
public class Q11_AverageAboveAverage { public static void main(String[] a){NumberAnalyzer analyzer=new NumberAnalyzer();analyzer.read(new Scanner(System.in));analyzer.analyze();} }
