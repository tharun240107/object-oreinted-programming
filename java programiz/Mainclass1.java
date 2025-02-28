class person {
private int age;
public int getAge(){
return age;
}
public void setAge(int age){
this.age=age;
}
}
class Main{
public static void main(String[]args){
person p1=new person();
p1.setAge(24);
System.out.println("My age is"+p1.getAge());
}
}