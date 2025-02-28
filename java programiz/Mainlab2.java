import java.util.Scanner;
class factorial{
public static void main(String[]args){
Scanner input=new Scanner(System.in);
System.out.print("Enter a number:");
int number= input.nextInt();
System.out.println("The factorial of"+ number+" is:"+factorial(number));
System.out.println("T.v.Tharun");
} 
public static  long factorial(int n){
 long fact=1;
for(int i=1;i<=n;i++){
fact*=i;
} 
return fact;
}
}



