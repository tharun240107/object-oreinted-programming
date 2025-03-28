class Student{
String name;
double percentage;
public Student(String name,double percentage){
this.name=name;
this.percentage=percentage;}
public void geteligibility(){
System.out.println(name+"must meet the eligibility requirements");}
}
class UG extends Student{
public UG(String name,double percentage){
super(name,percentage);}
public void geteligibility(){
if (percentage>=60){
System.out.println("person is eligible for ug");}
else{
System.out.println("person is not eligible for ug");}
}
}
class PG extends Student{
public PG(String name,double percentage){
super(name,percentage);}
public void geteligibility(){
if (percentage>=70){
System.out.println("person is eligible for pg");}
else{
System.out.println("person is not eligible for pg");}
}
}
public class Eligibility{
public static void main(String[] args){
Student s=new Student("Marco",79.9);
s.geteligibility();
UG u=new UG("Arjun Reddy",84);
u.geteligibility();
PG p=new PG("Srujan",59);
p.geteligibility();
}
}

