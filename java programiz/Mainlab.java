import java.util.Scanner;
class simpleinterest{
public static void main(String[]args){
Scanner input=new Scanner(System.in);
System.out.print("Enter the principal amount:");
double principal=input.nextDouble();
System.out.print("Enter the rateofinterest:");
double rateofinterest=input.nextDouble();
System.out.print("Enter the time in years:");
double time=input.nextDouble();
double simpleinterest=(principal*rateofinterest*time)/100;
System.out.println("The simpleinterest is:"+simpleinterest);
System.out.println("T.v.Tharun");
}
}


