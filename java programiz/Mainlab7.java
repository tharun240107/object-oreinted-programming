
import java.util.Scanner;
class FahrenheitToCelsius{
public static void main(String[]args){
Scanner input=new Scanner(System.in);
System.out.print("Enter temperature in  Fahrenheit:");
double  Fahrenheit = input.nextDouble();
double Celsius =( Fahrenheit-32)*5/9;
System.out.println("Temperature in Celsius:"+Celsius);
System.out.println("T.v.Tharun");
}
}
