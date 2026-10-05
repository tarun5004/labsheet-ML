// The helper method makes the digit-cube test reusable inside the for loop.
public class Q19_ArmstrongOneToThousand { static boolean armstrong(int n){int original=n,sum=0;do{int d=n%10;sum+=d*d*d;n/=10;}while(n>0);return sum==original;} public static void main(String[] a){for(int n=1;n<=1000;n++)if(armstrong(n))System.out.print(n+" ");} }
