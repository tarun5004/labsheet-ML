import java.util.Scanner;
// A sign condition classifies every value while traversing all dimensions.
public class Q16_ThreeDPositiveNegative { public static void main(String[] a){Scanner s=new Scanner(System.in);int positive=0,negative=0;for(int i=0;i<2;i++)for(int j=0;j<2;j++)for(int k=0;k<2;k++){int n=s.nextInt();if(n>=0)positive++;else negative++;}System.out.println("Positive: "+positive+", Negative: "+negative);} }
