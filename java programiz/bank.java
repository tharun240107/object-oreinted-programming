import java.util.Scanner;
class BankAccount{
private int accountNumber;
private String accountholder;
private float currentbalance;
public BankAccount(int accountNumber,Strig accountholder,float currentbalance) {
        this.accountNumber =accountNumber;
        this.accountholder= accountholder;
        this.balance= currentbalance;
}
public void deposit(int amount){
Scanner input=new Scanner(System.in);
System.out.println("enter the amount deposit:");
float deposit=input.nextFloat();
currentbalance += amount;
System.out.println("currentbalance:" +currentbalance);
}
public void withdraw(int amount){
Scanner input=new Scanner(System.in);
System.out.println("enter the amount withdrawn:");
float withdrawl=input.nextFloat();
if(amount<currentbalance){
currentbalance -=amount;
System.out.println("currentbalance:" +currentbalance);
}
else
{
System.out.println("insufficentamount");
}
}
public static void Main(String[] args){
BankAccount BA= new BankAccount("hari", 1534210,100000);
BA.withdraw(1000);
}
}