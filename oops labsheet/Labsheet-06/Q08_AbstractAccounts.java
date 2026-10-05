abstract class BankAccount { protected double balance; BankAccount(double b){balance=b;} abstract void deposit(double a); abstract void withdraw(double a); }
class SavingsAccount extends BankAccount { SavingsAccount(double b){super(b);} void deposit(double a){if(a>0)balance+=a;} void withdraw(double a){if(balance-a>=100)balance-=a;} }
class CurrentAccount extends BankAccount { CurrentAccount(double b){super(b);} void deposit(double a){if(a>0)balance+=a;} void withdraw(double a){if(a>0&&a<=balance)balance-=a;} }
public class Q08_AbstractAccounts { public static void main(String[] a){BankAccount s=new SavingsAccount(500),c=new CurrentAccount(500);s.deposit(100);s.withdraw(450);c.deposit(100);c.withdraw(550);System.out.println(s.balance+" "+c.balance);} }
