import java.util.Scanner;
// This combines a power-of-four bit test, bit toggle, continue, and break.
public class Q30_MixedOperatorsAndControl { public static void main(String[] a) { Scanner s=new Scanner(System.in); int n=s.nextInt(); boolean power=n>0&&(n&(n-1))==0&&(n&0x55555555)!=0; System.out.println("Power of 4: "+power); System.out.println("Third bit toggled: "+(n^(1<<2))); for(int i=1;i<=20;i++){int value=n*i;if(value%48==0)break;if(value%6==0)continue;System.out.println(value);} } }
