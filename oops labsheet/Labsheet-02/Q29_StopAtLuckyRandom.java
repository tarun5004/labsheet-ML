import java.util.Random;
// break exits as soon as a random number satisfies both divisibility rules.
public class Q29_StopAtLuckyRandom { public static void main(String[] a) { Random r=new Random(); while(true){int n=r.nextInt(100)+1;System.out.println(n);if(n%7==0&&n%13==0){System.out.println("Found target");break;}} } }
