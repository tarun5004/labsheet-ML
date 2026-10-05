import java.util.Scanner;
// A matrix is sparse when zero entries outnumber non-zero entries.
public class Q30_SparseMatrix { public static void main(String[] a){Scanner s=new Scanner(System.in);int zero=0,nonZero=0;for(int i=0;i<3;i++)for(int j=0;j<3;j++)if(s.nextInt()==0)zero++;else nonZero++;System.out.println(zero>nonZero?"Sparse":"Not sparse");} }
