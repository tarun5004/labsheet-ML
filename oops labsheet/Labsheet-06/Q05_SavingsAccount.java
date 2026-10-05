class BankAccount { protected double balance; BankAccount(double b){balance=b;} void deposit(double a){if(a>0)balance+=a;} void withdraw(double a){if(a>0&&a<=balance)balance-=a;} }
class SavingsAccount extends BankAccount { SavingsAccount(double b){super(b);}@Override void withdraw(double a){if(balance-a>=100)balance-=a;else System.out.println("Minimum balance must be 100");} }
// The child override adds the savings-account minimum-balance rule.
public class Q05_SavingsAccount { public static void main(String[] a){SavingsAccount x=new SavingsAccount(500);x.withdraw(450);x.withdraw(300);System.out.println(x.balance);} }
