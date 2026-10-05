class Account { private double balance; Account(double b){balance=b;} void deposit(double amount){if(amount>0)balance+=amount;} void display(){System.out.println("Balance: "+balance);} }
// Validation inside deposit protects the private balance from bad changes.
public class Q07_BankAccount { public static void main(String[] a){Account account=new Account(1000);account.deposit(500);account.deposit(-20);account.display();} }
