import java.util.Scanner;
class TriangleArea{
public static void main(String[]args){
Scanner input=new Scanner(System.in);
System.out.print("Enter the length of side a :");
double a= input.nextDouble();
System.out.print("Enter the length of side b :");
double b= input.nextDouble();
System.out.print("Enter the length of side c:");
double c= input.nextDouble();
double s=(a+b+c)/2;
double area= Math.sqrt(s*(s-a)*(s-b)*(s-c));
System.out.println("T.v.Tharun");
if(Double.isNaN(area)) {
 System.out.println("The entered sides do not form a valid triangle.");
}else {
System.out.println("The area of the triangle is:"+area);
}
}
}