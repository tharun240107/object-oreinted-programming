import java.util.Scanner;

class BankAccount {
    private int accountNumber;
    private String accountHolder;
    private float currentBalance;

    public BankAccount(int accountNumber, String accountHolder, float currentBalance) {
        this.accountNumber = accountNumber;
        this.accountHolder = accountHolder;
        this.currentBalance = currentBalance;
    }

    public void deposit(int amount) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the amount to deposit:");
        float deposit = input.nextFloat();
        currentBalance += deposit;
        System.out.println("Current Balance: " + currentBalance);
    }

    public void withdraw(int amount) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the amount to withdraw:");
        float withdrawal = input.nextFloat();
        if (withdrawal <= currentBalance) {
            currentBalance -= withdrawal;
            System.out.println("Current Balance: " + currentBalance);
        } else {
            System.out.println("Insufficient funds");
        }
    }

    public static void main(String[] args) {
        BankAccount BA = new BankAccount(1534210, "T.V.Tharun", 100000);
        BA.deposit(5000);  
        BA.withdraw(3000);
    }
}
