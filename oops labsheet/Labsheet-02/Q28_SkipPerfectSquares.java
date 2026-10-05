// continue skips only perfect squares and lets the loop print other numbers.
public class Q28_SkipPerfectSquares { public static void main(String[] a) { for(int n=1;n<=50;n++){int root=(int)Math.sqrt(n);if(root*root==n)continue;System.out.print(n+" ");} } }
