import java.util.Scanner;

// This exercise applies one rate to the selected income slab.
public class Q16_IncomeTax {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter annual income: ");
        double income = scanner.nextDouble();
        double rate;
        if (income <= 250000) rate = 0;
        else if (income <= 500000) rate = 0.05;
        else if (income <= 1000000) rate = 0.20;
        else rate = 0.30;
        System.out.println("Tax: " + income * rate);
    }
}
